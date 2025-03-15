import csv
import time
import tensorflow as tf
from tensorflow.keras.preprocessing import image
import numpy as np
import os
import random
import glob
import matplotlib.pyplot as plt
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score

def csv_output(output_text):
    with open("cabot_trail_output.csv", 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerows(output_text)

def csv_array_appender(imageName, yesNo, error, array):
    error = error * 100
    errorPercentage = f"{error:.2f}%"
    array.append([imageName, yesNo, errorPercentage])

# Initialize lists to hold data
dataset_dir = os.getenv('CEC_2025_dataset')
outputList = [["Image Name", "Yes/No", "Certainty"]]

batch_size = 32
batch_images = []
batch_names = []

# Map for target labels
label_map = {'no': 0, 'yes': 1}

# Load the model
model = tf.keras.models.load_model("brain_mri_classifier_epoch_11.keras")
class_names = ["no", "yes"]

# Set random seed for reproducibility
random.seed(time.time())

# Get all image paths recursively
all_image_paths = glob.glob(os.path.join(dataset_dir, "**", "*.png"), recursive=True)

# Randomly select 1000 images
selected_image_paths = random.sample(all_image_paths, 1000)

# Loop through images and predict
for brainPath in selected_image_paths:
    try:
        img = image.load_img(brainPath, target_size=(224, 224))
        img_array = image.img_to_array(img) / 255.0  # Normalize

        batch_images.append(img_array)
        batch_names.append(os.path.basename(brainPath))

        if len(batch_images) >= batch_size:
            batch_images_np = np.array(batch_images)
            predictions = model.predict(batch_images_np)

            for i, pred in enumerate(predictions):
                predicted_class = class_names[np.argmax(pred)]
                confidence = np.max(pred)
                csv_array_appender(batch_names[i], predicted_class, confidence, outputList)

            batch_images = []
            batch_names = []

    except Exception as e:
        print(f"Error processing {brainPath}: {e}")

# Process remaining images
if batch_images:
    batch_images_np = np.array(batch_images)
    predictions = model.predict(batch_images_np)

    for i, pred in enumerate(predictions):
        predicted_class = class_names[np.argmax(pred)]
        confidence = np.max(pred)
        csv_array_appender(batch_names[i], predicted_class, confidence, outputList)

csv_output(outputList)

# Compute Metrics
y_true = []
y_pred = []

for row in outputList[1:]:  # Skip header
    y_true.append(1 if "yes" in row[0].lower() else 0)
    y_pred.append(1 if row[1] == "yes" else 0)

accuracy = accuracy_score(y_true, y_pred)
precision = precision_score(y_true, y_pred)
recall = recall_score(y_true, y_pred)
f1 = f1_score(y_true, y_pred)

# Plot Metrics
metrics = ["Accuracy", "Precision", "Recall", "F1 Score"]
values = [accuracy, precision, recall, f1]

plt.figure(figsize=(8, 6))
plt.bar(metrics, values, color=["blue", "green", "red", "purple"])
plt.ylim(0, 1)
plt.ylabel("Score")
plt.title("Model Performance Metrics")
plt.xticks(rotation=45)
plt.grid(axis="y", linestyle="--", alpha=0.7)

# Show the plot
plt.show()