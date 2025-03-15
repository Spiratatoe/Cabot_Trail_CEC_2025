# Code was generated with teh help of ChatGPT
# Link to the prompt: https://chatgpt.com/share/67d5d53a-d7b0-800c-bccb-a6066ddf5969
import tensorflow as tf
from tensorflow.keras import layers, models, callbacks
from tensorflow.keras.applications import MobileNetV2

# Enable XLA compilation for speed
tf.config.optimizer.set_jit(True)

# Load MobileNetV2 without the top layer
base_model = MobileNetV2(weights="imagenet", include_top=False, input_shape=(224, 224, 3))

# Build classification head to categorize as "yes" or "no"
# The output layer has 2 units for binary classification
x = layers.GlobalAveragePooling2D()(base_model.output)
x = layers.Dense(128, activation="relu")(x)
output = layers.Dense(2, activation="softmax")(x)

# Create and compile model
model = models.Model(inputs=base_model.input, outputs=output)
model.compile(optimizer="adam", loss="sparse_categorical_crossentropy", metrics=["accuracy"])

# Set dataset parameters
AUTOTUNE = tf.data.AUTOTUNE
img_size = (224, 224)
batch_size = 30

# Load dataset
dataset = tf.keras.preprocessing.image_dataset_from_directory(
    "CEC_2025", image_size=img_size, batch_size=batch_size, shuffle=True, seed=42
)

# Get total dataset size in batches
dataset_size = len(dataset)  # This returns number of batches, NOT images
print(f"Total dataset size (batches): {dataset_size}")

# Compute dataset sizes (based on batches)
train_size = int(0.60 * dataset_size)  # 60% for training
val_size = int(0.15 * dataset_size)  # 15% for validation
test_size = dataset_size - train_size - val_size  # Remaining 25% for testing

print(f"Train dataset size: {train_size}, Validation dataset size: {val_size}, Test dataset size: {test_size}")

# Normalize images
normalization_layer = tf.keras.layers.Rescaling(1.0 / 255)


def preprocess(x, y):
    return normalization_layer(x), y  # Keep shape (batch_size, 224, 224, 3)


# Split dataset properly
train_dataset = (
    dataset.take(train_size).map(preprocess, num_parallel_calls=AUTOTUNE).cache().shuffle(1000).prefetch(AUTOTUNE)
)
val_dataset = (
    dataset.skip(train_size).take(val_size).map(preprocess, num_parallel_calls=AUTOTUNE).cache().prefetch(AUTOTUNE)
)
test_dataset = dataset.skip(train_size + val_size).map(preprocess, num_parallel_calls=AUTOTUNE).prefetch(AUTOTUNE)

# Verify dataset sizes
train_batches = len(list(train_dataset))
val_batches = len(list(val_dataset))
test_batches = len(list(test_dataset))
print(f"Train batches: {train_batches}, Validation batches: {val_batches}, Test batches: {test_batches}")

# Ensure step counts to avoid "Unknown" issue
steps_per_epoch = train_size
val_steps = val_size

# Define checkpoint callback to save model per epoch
checkpoint_callback = callbacks.ModelCheckpoint(
    filepath="brain_mri_classifier_epoch_{epoch:02d}.keras",
    save_best_only=False,  # Saves every epoch
    save_weights_only=False,
    verbose=1,
)

# Train the model
history = model.fit(
    train_dataset,
    validation_data=val_dataset,
    epochs=30,
    steps_per_epoch=steps_per_epoch,  # Explicit step count
    validation_steps=val_steps,  # Fix validation step count
    callbacks=[checkpoint_callback],
)

# Evaluate on test set
test_loss, test_acc = model.evaluate(test_dataset)
print(f"Test accuracy: {test_acc:.4f}, Test loss: {test_loss:.4f}")

# Save the trained model
model.save("brain_mri_classifier.keras")
