# Year-4-Project

"Detecting And Classifying Radio Galaxies Using Convolution Neural Networks With Synthetic Training sets"

## Description of Repository Contents: 

1. FITS file / image manipulation
-> Examples of the basic functionality of reading and manipulating FITS files / images. The key examples for this project being; sigma clipping the images to remove the background, and rotating the images for training set augmentation.

2. Webscrape FIRST source cutouts
-> Get FITS cutout images

3. Building training set
-> Loading FITS files from a directory into a 3D array for use as a training / test data set for a neural network. Includes functionality for; identifying missing data from the expected list of sources, identifying bad data (including nan pixel values), sigma clipping and normalising the images, augmenting a data set using rotations and flipped rotations of the images, and combining multiple data sets into one large shuffled data set with a corresponding list of image labels for which original data set the image came from.

4. Simple neural network
->

5. Complex (convolutional) neural network
->

6. Filtering FIRST sources
->

7. DCGAN
-> (Deep Convolutional Generative Adversarial Network)
From a training set of agn images, use a DCGAN to generate a training set of realistic, fake agn images. Uses model checkpoints for restoring previous model variables, for long training over many epochs. Generates a GIF to visualise the training process of the GAN from random noise to realistic images. 
