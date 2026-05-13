# CST 205 Final Project: Image Hidden Code Encryptor/Decryptor

This program can be used to add and read hidden codes into images, with public and private keys used to ensure the message stays secure.

## Features

- Hides one image inside of another using least significant bit (LSB) sternography. It does this by replacing the final bit in every image with a bit from another image, storing information in an image without significantly changing the colors of the first image.
- The program also features a way to retrieve data from images already encoded with LSB sternography.
- Using the UnSplash API, the user can select a keyword for the image they want to hide and the image they want to hide the former image in, and automatically fetch said images from a repository.
- All done through a GUI, allowing for easy usage.

## Tech Stack

- Language: Python
- Framework: Standard Python Script
- Infrastructure: Unsplash API, NumPy, Pillow, local image processing.

## Installation/Usage

Step 1: Download the files from the repository
Step 2: Unzip files, and open the file containing them in your file manager of choice
Step 3: Open up a Command Line/Terminal, and run gui.py using Python
