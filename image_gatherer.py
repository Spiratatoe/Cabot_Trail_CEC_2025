
from os import path
import os
import shutil
import random


def yoink():
    dataset_dir = os.getenv('CEC_2025_dataset')  # Retrieves the path from the environment variable

    # Initialize lists to hold data
    image_paths = []
    targets = []

    total_images = 0

    # Map for target labels
    label_map = {'no': 0, 'yes': 1, 'CEC_test': 2}

    # Loop through subdirectories in the dataset directory
    for subdir in os.listdir(dataset_dir):
        subdir_path = path.join(dataset_dir, subdir)

        if os.path.isdir(subdir_path):
            subdir_path_list = os.listdir(subdir_path)
            for image in subdir_path_list:
                image_paths.append(path.join(subdir_path, image))
                targets.append(label_map[subdir])

            total_images += len(subdir_path_list)
            print(f"Number of images in '{subdir}' directory: {len(subdir_path_list)}")

    print(f'Total number of images: {total_images}')

# chat gpt code used to quickly set up the files for training and testing
# “ChatGPT,” Chatgpt.com, 2025. https://chatgpt.com/ (accessed Mar. 15, 2025).
'''
hey, i have a folder, in that folder there is two folders : yes & no in those 2 folders theres images, i want to create a python script that randomly selects a percentage of images and puts in a train, test and val folder specifically 6153 in train and 1026 in val and test
'''
def image_selector():

    # Define paths
    base_dir = os.getenv('CEC_2025_dataset')   # Change to the actual base directory
    source_yes = os.path.join(base_dir, "yes")
    source_no = os.path.join(base_dir, "no")

    # Destination folders
    train_dir = os.path.join(base_dir, "train")
    val_dir = os.path.join(base_dir, "val")
    test_dir = os.path.join(base_dir, "test")

    # Create the directories if they don't exist
    for folder in [train_dir, val_dir, test_dir]:
        os.makedirs(os.path.join(folder, "yes"), exist_ok=True)
        os.makedirs(os.path.join(folder, "no"), exist_ok=True)

    # Get list of images
    yes_images = [img for img in os.listdir(source_yes) if img.lower().endswith(('.png', '.jpg', '.jpeg'))]
    no_images = [img for img in os.listdir(source_no) if img.lower().endswith(('.png', '.jpg', '.jpeg'))]

    # Shuffle the images
    random.shuffle(yes_images)
    random.shuffle(no_images)

    # Ensure balanced splits
    total_train = 6153
    total_val = 1026
    total_test = 1026

    train_split = total_train // 2  # Half yes, half no
    val_split = total_val // 2
    test_split = total_test // 2

    # Move images
    def move_images(image_list, src_folder, dest_folder, count):
        for img in image_list[:count]:
            shutil.move(os.path.join(src_folder, img), os.path.join(dest_folder, img))
        return image_list[count:]  # Return remaining images

    # Distribute images
    yes_images = move_images(yes_images, source_yes, os.path.join(train_dir, "yes"), train_split)
    yes_images = move_images(yes_images, source_yes, os.path.join(val_dir, "yes"), val_split)
    yes_images = move_images(yes_images, source_yes, os.path.join(test_dir, "yes"), test_split)

    no_images = move_images(no_images, source_no, os.path.join(train_dir, "no"), train_split)
    no_images = move_images(no_images, source_no, os.path.join(val_dir, "no"), val_split)
    no_images = move_images(no_images, source_no, os.path.join(test_dir, "no"), test_split)

    print("Data split completed successfully!")


image_selector()
