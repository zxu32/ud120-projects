#!/usr/bin/python

""" 
    This is the code to accompany the Lesson 2 (SVM) mini-project.

    Use a SVM to identify emails from the Enron corpus by their authors:    
    Sara has label 0
    Chris has label 1
"""
from tools.email_preprocess import preprocess
from sklearn import svm
import sys
from time import time
sys.path.append("../tools/")

### features_train and features_test are the features for the training
### and testing datasets, respectively
### labels_train and labels_test are the corresponding item labels
features_train, features_test, labels_train, labels_test = preprocess()

# slicing some of the data off the sets, one of the quiz questions
# features_train = features_train[:len(features_train)//100]
# labels_train = labels_train[:len(labels_train)//100]

clf = svm.SVC(kernel='rbf', C=10000)
clf.fit(features_train, labels_train)
pred = clf.predict(features_test)

print((pred == 1).sum())

accuracy = (labels_test == pred).sum()/float(len(labels_test))
print(accuracy)
#########################################################
