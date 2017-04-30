#########################################################################
# Project: Vocal tweet recommender for the Bothrs startup based in Ghent
# Author: Lander Bodyn
# Date: 15/04/2017
#########################################################################

import csv
import numpy
import pandas as pd





# Read in data
df = pd.read_csv('Rating-Grid view.csv')

# Build data matrix
df2 = df.pivot(index='\ufeffUserID', columns='MessageId', values='Rating')

print(df)
print(df2)

# Build recommender system


def pca_recommender():


def feature_recommender():



