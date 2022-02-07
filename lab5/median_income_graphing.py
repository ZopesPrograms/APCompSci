import graphing
import random

import os

import numpy as np
import pandas as pd

incomes = pd.read_csv('lab5/medIncome.csv')

def central_limit_histogram(incomes, samples, trials, filen, directory):
    assert type(samples) == int, (str(samples) + ' must be a positive integer!')
    assert type(trials) == int, (str(trials) + ' must be a positive integer!')

    assert samples > 0, (str(samples) + ' must be a positive integer!')
    assert trials > 0, (str(samples) + ' must be a positive integer!')

    mean = 0
    sampleMeans = []

    for a in range(0, samples):
        for b in range(0, trials):

            income = incomes.sample().mean(0).to_dict()
            mean += income['x']

        mean = mean / 100
        sampleMeans.append(mean)

        print('Mean ' + str(a) + ' to: ' + str(mean))

    if not os.path.exists('Graphs/'+directory):
        os.makedirs('Graphs/'+directory)

    graphing.makeHist(sampleMeans, np.arange(0,100000,200), (str(directory)+'/'+filen))

if __name__ == '__main__':
    central_limit_histogram(incomes, 50, 100, "normal50.png", "la_incomes_normals")
    central_limit_histogram(incomes, 100, 100, "normal100.png", "la_incomes_normals")

    central_limit_histogram(incomes, 500, 100, "normal500.png", "la_incomes_normals")
    central_limit_histogram(incomes, 1000, 100, "normal1000.png", "la_incomes_normals")
    
    central_limit_histogram(incomes, 5000, 100, "normal5000.png", "la_incomes_normals")
    central_limit_histogram(incomes, 10000, 100, "normal10000.png", "la_incomes_normals")