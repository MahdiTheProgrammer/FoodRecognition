import torch
from torch import nn 
import os
import glob

# Specify the folder path where the images are located
folder_path = "Dataset/"

# Create a list to store the image paths
image_list = []

# Use glob to search for image files within the folder
image_files = glob.glob(os.path.join(folder_path, "*.jpg"))  # Adjust the file extension as needed

# Iterate over the image files and add their paths to the list
for image_file in image_files:
    image_list.append(image_file)