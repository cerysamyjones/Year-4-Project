from __future__ import absolute_import, division, print_function, unicode_literals
import tensorflow as tf
import numpy as np
import os
from astropy.io import fits 
from astropy import stats
from scipy.ndimage import rotate

#Number of x pixels and y pixels in each image (must be the same for all images)
xpix = 83
ypix = 83
#Creating a list of the file names within the fits image folder to open later
#Just copy and paste the path here and it will sort out the separators
agn_path = r'C:\Users\Cerys\Documents\Physics\Y4 Project\Data Preparation\Radio Zoo Images'
ps_path = r'C:\Users\Cerys\Documents\Physics\Y4 Project\Data Preparation\Stars'

def get_clipped_images(filepath,xpix,ypix,sigma):
    newpath = filepath.replace(os.sep, '/')
    dirs = os.listdir(newpath)
    n = len(dirs)
    data = np.empty(shape=(n,xpix,ypix),dtype=np.float64)
    for i in range(n):
        fullpath = '{}/{}'.format(newpath,dirs[i])
        d = fits.getdata(fullpath, ext=0)
        d[np.isnan(d)] = 0
        _,median,std = stats.sigma_clipped_stats(d, sigma=sigma)
        d[d<median+sigma*std] = median+sigma*std
        data[i,:,:] = d
    return data

def augment_data(data,size,xpix,ypix):
    rotations = size//len(data) # rotations per image
    angles = np.linspace(0, 360, rotations)
    act_size = rotations*len(data)
    training_set = np.empty((act_size, xpix, ypix))
    for i in range(len(data)):
        for j in range(len(angles)):
            if j % 2 == 0: training_set[i*len(angles)+j,:,:] = rotate(np.fliplr(data[i,:,:]), angles[j], reshape=False)
            else: training_set[i*len(angles)+j,:,:] = rotate(data[i,:,:], angles[j], reshape=False)
    return training_set

def train_test(data,percentage):
    d = np.concatenate(data,axis=0)
    n_images = len(d)
    labels = np.empty(n_images)
    i = 0
    for n in range(len(data)):
        labels[i:i+len(data[n])] = n
        i = len(data[n])
    rand_ind = np.random.permutation(range(n_images))
    d, labels = d[rand_ind], labels[rand_ind]
    n_train = np.int(np.round(n_images*percentage))
    train = (d[:n_train], labels[:n_train])
    test = (d[n_train:], labels[n_train:])
    return train, test
     
agn_data = get_clipped_images(agn_path,83,83,sigma=3)
ps_data = get_clipped_images(ps_path,83,83,sigma=1)
agn_augment = augment_data(agn_data, 10000,83,83)
ps_augment = augment_data(ps_data, 10000,83,83)

data = (agn_augment,ps_augment)
train, test = train_test(data,0.8)

#Neural network
model = tf.keras.models.Sequential([
  tf.keras.layers.Flatten(input_shape=(xpix, ypix)),
  tf.keras.layers.Dense(512, activation=tf.nn.relu),
  tf.keras.layers.Dropout(0.3),
  tf.keras.layers.Dense(10, activation=tf.nn.softmax)])
    
#Compile the network
model.compile(optimizer='adam',
              loss='sparse_categorical_crossentropy',
              metrics=['accuracy'])

#Perform fit
model.fit(*train, epochs=10)
test_loss, test_acc = model.evaluate(*test, verbose=2)
print('\nTest accuracy:', test_acc)
