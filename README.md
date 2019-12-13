# Year-4-Project

"Detecting And Classifying Radio Galaxies Using Convolution Neural Networks With Synthetic Training Sets"

## Description of Repository Contents: 

1. FITS file / image manipulation  
-> Examples of the basic functionality of reading and manipulating FITS files / images. The key examples for this project being; sigma clipping the images to remove the background, and rotating the images for training set augmentation.

2. Webscrape FIRST source cutouts  
-> Downloads 2.5x2.5 arcsec FITS images of sources from the FIRST website cutout search engine by web scraping using chrome driver.
-> Very useful for downloading many images in one go, runtime approx 10 mins per 1000 images.

3. Building training set  
-> Loading FITS files from a directory into a 3D array for use as a training / test data set for a neural network. Includes functionality for; identifying missing data from the expected list of sources, identifying bad data (including nan pixel values), sigma clipping and normalising the images, augmenting a data set using rotations and flipped rotations of the images, and combining multiple data sets into one large shuffled data set with a corresponding list of image labels for which original data set the image came from.

4. Simple neural network  
-> Basic neural network (based on design shared on Tensorflow website) designed to identify point sources from AGN with jets. 
-> Very simple task and as such does so with approx 100% accuracy.

5. Complex (convolutional) neural network  
-> More complex neural network designed to group AGN with jets by their bending angle (angle between the jets)
-> Uses convolutional layers, pooling layers and densely connected layers to achieve an accuracy of 97% for this task. 

6. Filtering FIRST sources  
-> Program designed to use a variety of methods to filter all identified first sources for those which are most likely to be AGN with jets. These sources can then be downloaded using webscraping.
-> Filtering is done by evaluating the distance between sources, their symmetry, spread, brightness, however none of these methods are 100% accurate and as a result any potential AGN with jets identified using this program must be passed through a neural network to check their classification. 

7. DCGAN  
-> (Deep Convolutional Generative Adversarial Network)
From a training set of agn images, use a DCGAN to generate a training set of realistic, fake agn images. Uses model checkpoints for restoring previous model variables, for long training over many epochs. Generates a GIF to visualise the training process of the GAN from random noise to realistic images. 
