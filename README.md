# Introduction
Welcome to the CEC 2025 Programming Competition! Everything you need is in this GitHub, and we recommend the following steps to get started:

1. Read the rest of this README.md
2. Read the tutorial linked in githubHowToUseGithubDesktop.txt
3. Read the tutorial linked in githubHowToFork.txt
4. Fork this repo
5. Clone your forked repo locally on your machine
6. Start coding!

   
# Getting Help
Please follow the following steps if you need help:

1. Check the included documentation for logistics and scoring questions
2. Check the Programming Competition Case for competition questions
3. Check the discord for previously answered questions
4. If you have done all of that, ask the Directors for help. If we can answer your question, it will be posted on the discord in English and French.
   
# Important Notes
In your README.md please specify:

- How to run your code
- What language and version your code uses (ie. Python 3.11)
- A list of required packages (i.e. Pandas, NumPy), with version if needed (ie. pytorch==2.1.116). A requirements.txt would also suffice.
- If needed, what OS your code should be run on. Any specifications of this sort not included in your README cannot be assumed to be on the 
Directors’ machine(s).

# Info Files
The following files provide all the information regarding the competition. 
This includes:
- The Case Document
- Presentation
- Example Output
- Testing information
- GitHub Info

# Accessing Dataset

We have given you all access to the images through the OneDrive link here: 

https://dalu-my.sharepoint.com/:u:/g/personal/or942416_dal_ca/EdKN7DMS8tNHm-dPmV56JCEB46o-vSoG4WMfbcdNRZCX8Q?e=PboqSt 


You'll notice that the dataset is to be saved as a 7z file. You will need to install either 7-zip or keka to extract the dataset.

## 7-zip can be downloaded for Windows using link below:
https://www.7-zip.org

## kekas can be downloaded for MacOS using link below:
https://www.keka.io/en/

When extracting the file make sure to use 7-zip or keka.

The password for the 7z file is:
```
gT5&dK9zR2wQ!aP0eY3B#6vL1zXhF8j
```

We suggest saving the folder via a zip file and then unzipping it locally to your computer. Download the no zip file followed by the yes zip file, to avoid errors. On average this method takes about 20min (assuming ~400KB/s). You can try syncing the OneDrive folder, however we find it takes longer to download the files that way.

# Testing
Your code will be tested by comparing the results of your algorythm to the correct results. A folder labelled 'CEC_test' will have a set amount of test images (that only the directors have access to) corresponding to 'yes' or 'no'. The file format for these images will be png, with the names of each image being 'test_xxx.png'. Note x in this case represents the number of files tested, similiar to the yes and no directories. Make sure you have a testing script referncing this folder located at (/CEC_2025/CEC_test), Directors will change the file path according to their machines on the day.

Results will be compared with the correct results in Excel. It is neccesary that competitors output there results to a csv, xlsx, or google sheet file (or similiar). While other UI's are encouraged for asthetic purposes, a .csv file or anything simliar for outputting raw results is neccesary for testing purposes! You can see the sample outupt in the info folder for more details relating to this!

As long as your code outputs the test_image being tested (1st collumn) and the resule which is either 'yes' or 'no' (2nd collumn), your code will be ready for testing.

# Potentiall Useful Info:

## Retrieve Dataset
Below is an example code which accesseses this folder and then runs through using the root directory. 

Note: This code was written for MacOS interfacing

```ruby
import os
from os import path

dataset_dir = "/file/path/to/CEC_2025" # Change this to where the folder is saved

# Initialize lists to hold data
image_paths = []
targets = []

total_images = 0

# Map for target labels
label_map = {'no': 0, 'yes': 1, 'CEC_test': 2}  # Added 'CEC_test' label

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
```
This should ouput something like this:
```
Number of images in 'no' directory: 8727
Number of images in 'CEC_test' directory: 1
Number of images in 'yes' directory: 9310
Total number of images: 18038
```
## Checking File Paths
You may also want to check the file paths of your images:
```ruby
import pandas as pd
import numpy as np

df = pd.DataFrame({
    'image_path': image_paths,
    'target': targets
}, index=np.arange(0, total_images))

print(df.head())
```
Which should output something like this:
```
                                          image_path  target
0  /Users/orionwiersma/Documents/CEC_2025/no/no_...       0
1  /Users/orionwiersma/Documents/CEC_2025/no/no_...       0
2  /Users/orionwiersma/Documents/CEC_2025/no/no_...       0
3  /Users/orionwiersma/Documents/CEC_2025/no/no_...       0
4  /Users/orionwiersma/Documents/CEC_2025/no/no_...       0
```
