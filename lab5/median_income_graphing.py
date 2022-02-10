import graphing
import random

import os

import numpy as np
import pandas as pd

# Load csv of LA incomes into 'incomes' DataFrame variable
incomes = pd.read_csv('lab5/medIncome.csv')

def central_limit_histogram(incomes, samples, trials, limit1, limit2, bin, filen, directory):
    ''' Creates histogram of mean incomes calculated by random collections of
        incomes inputted, and saves it to a file. Makes normal curve in doing
        so by the central limit theorem.

    Parameters
    --
    incomes: DataFrame
        CSV Dataframe containing incomes distribution
    samples: int > 0
        Number of means to take from random samplings of incomes
    trials: int > 0
        Individual sample incomes to go into mean
    limit1: float
        Lower bound of income range displayed in graph
    limit2: float
        Upper bound of income range displayed in graph
    bin: float
        Width of histogram bin over x-axis
    filen: str
        What name our histogram graph file should be saved as
    directory: str
        The name of the folder in which to save our mean sampling histogram

    Returns 
    --
    None, but creates histogram of income normal curve by central limit theorem.
    '''

    # Throw exception if our samples, trials variables are not positive integers

    assert type(samples) == int, (str(samples) + ' must be a positive integer!')
    assert type(trials) == int, (str(trials) + ' must be a positive integer!')

    assert samples > 0, (str(samples) + ' must be a positive integer!')
    assert trials > 0, (str(samples) + ' must be a positive integer!')

    # Mean variable + list of means
    mean = 0
    sampleMeans = []

    # Cycle through 'samples' number of means
    for a in range(0, samples):

        # Take means from 'trials' number of random income samples
        for b in range(0, trials):

            # Take random income, add it to mean sum var
            income = incomes.sample().mean(0).to_dict()
            mean += income['x']

        ''' Make mean sum var into mean via division by trials count --
            then append it to mean list. '''
        mean = mean / trials
        sampleMeans.append(mean)
        # Reset mean, print output for debug
        mean = 0
        print('Mean ' + str(a) + ' to: ' + str(mean))

    # Creates folder to store income histogram if it does not already exist
    if not os.path.exists('Graphs/'+directory):
        os.makedirs('Graphs/'+directory)

    ''' Saves histogram of collected random sample means in folder 'directory' 
        under filename 'filen.'''
    graphing.makeHist(sampleMeans, np.arange(limit1,limit2,bin), (str(directory)+'/'+filen))

# MAIN CODE BLOCK
if __name__ == '__main__':

    ''' Graph LA income random mean sampling histograms with parameters as 
        perscribed by the lab 5 instructions. '''

    central_limit_histogram(incomes, 50, 100, 45000, 60000, 200, "normal50.png", "la_incomes_normals")
    central_limit_histogram(incomes, 100, 100, 45000, 60000, 200, "normal100.png", "la_incomes_normals")

    central_limit_histogram(incomes, 500, 100, 45000, 60000, 200, "normal500.png", "la_incomes_normals")
    central_limit_histogram(incomes, 1000, 100, 45000, 60000, 200, "normal1000.png", "la_incomes_normals")
    
    central_limit_histogram(incomes, 5000, 100, 45000, 60000, 200, "normal5000.png", "la_incomes_normals")
    central_limit_histogram(incomes, 10000, 100, 45000, 60000, 200, "normal10000.png", "la_incomes_normals")