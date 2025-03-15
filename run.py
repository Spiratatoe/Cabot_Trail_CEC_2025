import tensorflow as tf
from tensorflow.keras.preprocessing import image
import numpy as np
import os
from os import path
from csvexport import *



# Initialize lists to hold data
dataset_dir = os.getenv('CEC_2025_dataset') 
outputList =[["Image Name","Yes/No","Certainty"]]

# Evaluate on test data (if available)
model = tf.keras.models.load_model("brain_mri_classifier_epoch_11.keras")
class_names = ["no", "yes"]

# Loop through subdirectories in the dataset directory
subdir_path = os.path.join(dataset_dir, 'CEC_test')

#Modified from ChatGPT
if os.path.isdir(subdir_path):
    subdir_path_list = os.listdir(subdir_path)
    for brain in subdir_path_list:
        brainPath = path.join(subdir_path,brain)
        print(brainPath)
        img = image.load_img(brainPath, target_size=(224, 224)) 
        img_array = image.img_to_array(img)
        img_array = np.expand_dims(img_array, axis=0)  # Add batch dimension
        img_array = img_array / 255.0  # Normalize (same preprocessing as training)
        # Make prediction
        predictions = model.predict(img_array)

        # Get the class with the highest probability
        predicted_class = class_names[np.argmax(predictions)]
        confidence = np.max(predictions)          
        csv_array_appender(brain,predicted_class,confidence,outputList)
        print(f"Predicted class: {predicted_class} with {confidence:.2f} confidence")  

#Export to CSV
csv_output(outputList)

