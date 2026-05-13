# CST 205 Final Project: Image Hidden Code Encryptor/Decryptor

This program can be used to add and read hidden codes into images, with public and private keys used to ensure the message stays secure.

## Features

- Hides one image inside of another using least significant bit (LSB) sternography. It does this by replacing the final bit in every image with a bit from another image, storing information in an image without significantly changing the colors of the first image.
- The program also features a way to retrieve data from images already encoded with LSB sternography.
- Using the UnSplash API, the user can select a keyword for the image they want to hide and the image they want to hide the former image in, and automatically fetch said images from a repository.
- Put info about GUI here.

## Tech Stack

- Language: Python
- Framework: Standard Python Script
- Infrastructure: Unsplash API, NumPy, Pillow, local image processing.

## Installation

WIP
