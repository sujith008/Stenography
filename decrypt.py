# decryption.py

import cv2
import os
import tkinter as tk
from tkinter import filedialog

# Function to select an image file
def select_image():
    root = tk.Tk()
    root.withdraw()  # Hide the root window
    file_path = filedialog.askopenfilename(title="Select an Encrypted Image", filetypes=[("Image Files", "*.jpg *.png *.jpeg")])
    return file_path

# Open file dialog to select an encrypted image
image_path = select_image()
if not image_path:
    print("No image selected. Exiting...")
    exit()

# Load the encrypted image
img = cv2.imread(image_path)
if img is None:
    print("Error: Unable to load the image.")
    exit()

# Take user input for the decryption passcode
pas = input("Enter passcode for decryption: ")
password = input("Re-enter passcode: ")

# Create dictionary for ASCII decoding
c = {i: chr(i) for i in range(255)}

# Decrypt message
if password == pas:
    message = ""
    n, m, z = 0, 0, 0
    try:
        while True:
            message += c[img[n, m, z]]
            n = (n + 1) % img.shape[0]
            m = (m + 1) % img.shape[1]
            z = (z + 1) % 3
    except KeyError:
        pass
    
    print("Decrypted message:", message)
else:
    print("ERROR: Incorrect passcode!")
