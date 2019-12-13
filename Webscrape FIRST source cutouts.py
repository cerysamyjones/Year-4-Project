# -*- coding: utf-8 -*-
"""
Created on Fri Nov  1 17:01:55 2019

@author: Cerys
"""
from selenium import webdriver
import pandas as pd
import time
from selenium.common.exceptions import NoSuchElementException

#Uses chrome driver - needs to be downloaded before running code
#The version of chrome driver used must be the same as the chrome browser
#Chrome driver can be used remotely once downloaded
driver = webdriver.Chrome()
#Open chrome and maximise window
driver.maximize_window()

#Get webpage that cutouts can be downloaded from
driver.get("https://third.ucllnl.org/cgi-bin/firstcutout")

#Assign required image size (in arcmin) by finding image size element and changing its value
size_arcmin = 2.5
imagesize = driver.find_element_by_name('ImageSize')
driver.execute_script("arguments[0].value=arguments[1]",imagesize,'{}'.format(size_arcmin))

#Read in RA and dec data downloaded from VisieR 
data = pd.read_csv('Radio Galaxy Zoo AGN with Jets.txt',sep='  ',
                   engine='python',dtype=None,header=None)
ra = data.iloc[:,1] #convert to hours
dec = data.iloc[:,2] #given in degrees 

#Loop to copy each RA and dec into the cutout search engine and download each image
for i in range(len(ra)):
    try:
        #Finds search box and changes value to a string with RA and dec 
        radec = driver.find_element_by_name('RA')
        driver.execute_script("arguments[0].value=arguments[1]",radec,"{}\t+{}".format(ra[i],dec[i]))
        #Clicks on button to select download type to be a FITS image
        fits_file = driver.find_elements_by_name('ImageType')[2]
        fits_file.click()
        #Clicks submit to download image
        submit = driver.find_element_by_name('.submit')
        submit.click()
    except NoSuchElementException:
        #Exception incase the input RA and dec are out of range of the database
        #Resets the webpage and continues loop through remaining values
        print ('Could not find element {}'.format(i))
        driver.get("https://third.ucllnl.org/cgi-bin/firstcutout")
        time.sleep(3)
        imagesize = driver.find_element_by_name('ImageSize') #in arcmins
        driver.execute_script("arguments[0].value=arguments[1]",imagesize,'2.5')
        continue
