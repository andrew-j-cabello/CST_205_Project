# CST 205 Final Project: Image Hidden Code Encryptor/Decryptor

This program can be used to add and read hidden codes into images, with public and private keys used to ensure the message stays secure.

#GITHUB REPO LINK 
- https://github.com/andrew-j-cabello/CST_205_Project 

## Features

- Hides one image inside of another using least significant bit (LSB) sternography. It does this by replacing the final bit in every image with a bit from another image, storing information in an image without significantly changing the colors of the first image.
- The program also features a way to retrieve data from images already encoded with LSB sternography.
- Using the UnSplash API, the user can select a keyword for the image they want to hide and the image they want to hide the former image in, and automatically fetch said images from a repository.
- All done through a GUI, allowing for easy usage.

## Tech Stack

- Language: Python
- Framework: Standard Python Script
- Infrastructure:
  
 Unsplash API: Used to get images to hide data in.

 NumPy: Used to easily manipulate bits in order to hide the data.

 Pillow: Used to manipulate images in order to hide data in an image.

## Installation/Usage

Step 1: Download the files from the repository

Step 2: Make an account with UnSplash in order to access images, put API keys created in the code (Not needed for this presentaiton, we have one preloaded)

Step 3: Unzip files, and open the file containing them in your file manager of choice

Step 4: Open up a Command Line/Terminal, and run gui.py using Python

# Future work 

- Try and see if we could incorportate other forms of media to work with our encrypt / decrypt 
- Finish implementing the function which takes care of taking the output carrier image we get saved after running our program 
  as right now we don't have the ability to just run the decrypt with a encrypted picture