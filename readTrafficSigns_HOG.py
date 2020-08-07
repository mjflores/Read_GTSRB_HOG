# The German Traffic Sign Recognition Benchmark
#
# sample code for reading the hog features of traffic sign images and the
# corresponding labels
#
# example:
#            
# trainFeatures, trainLabels = readTrafficSignsFeatures('GTSRB/Training')
# print len(trainLabels), len(trainImages)
# plt.hist(trainFeatures[42])
# plt.show()
#
# have fun, Marco

'''
   @autor: mjflores
   @date: 05/08/2020
'''

import matplotlib.pyplot as plt
import csv
import pandas as pd
import numpy as np
from os import listdir

def readHOG_txt(dr):
    file1 = open(dr,"r") 
    hog = []
    for line in file1: 
        hog.append(float(line))
    file1.close()         
    return hog

#=====================================

# function for reading the hog features of images
# arguments: path to the traffic sign data, for example './GTSRB/Training'
# returns: list of images, list of corresponding labels 
def readTrafficSignsFeatures_Train(rootpath):
    '''Reads HOG features from traffic sign data for German Traffic Sign Recognition Benchmark.

    Arguments: path to the traffic sign data, for example './GTSRB/Training'
    Returns:   list of images, list of corresponding labels'''
    
#    print("rootpath=",rootpath)
    features = [] # images
    labels = [] # corresponding labels
    # loop over all 42 classes
    for c in range(0,43):
        prefix = rootpath + format(c, '05d') + '/'
        for nomb in listdir(prefix):
            direc = '%s%s' % (prefix,nomb)
            hogk = readHOG_txt(direc)
            features.append(hogk)
            labels.append(c)            
    return features, labels
    
def readTrafficSignsFeatures_Test(rootpath):
    '''Reads HOG features from traffic sign data for German Traffic Sign Recognition Benchmark.

    Arguments: path to the traffic sign data, for example './GTSRB/Training'
    Returns:   list of images, list of corresponding labels'''
    
#    print("rootpath=",rootpath)
    features = [] # images
    labels = [] # corresponding labels
    # loop over all 42 classes
    for c in range(0,43):
        prefix = rootpath  
        for nomb in listdir(prefix):
            direc = '%s%s' % (prefix,nomb)
            hogk = readHOG_txt(direc)
            features.append(hogk)
            labels.append(c)            
    return features, labels
    
    
#=============================================================

drccnTrain = "../Traffic_sign/GTSRB_Final_Training_HOG/GTSRB/Final_Training/HOG/HOG_01/"

drccnTest = "../Traffic_sign/GTSRB_Final_Test_HOG/GTSRB/Final_Test/HOG/HOG_01/"


trainHOGs, trainLabels = readTrafficSignsFeatures_Train(drccnTrain)
testHOGs, testLabels = readTrafficSignsFeatures_Test(drccnTest)


#print(len(trainLabels), len(trainHOGs)) 
#plt.hist(trainHOGs[100])
#plt.title("Sign "+str(trainLabels[100]))
#plt.show()

#print(len(testLabels), len(testHOGs)) 
#plt.hist(testHOGs[100])
#plt.title("Sign "+str(testLabels[100]))
#plt.show()



