import graphing
import random

import numpy as np
import pandas as pd

incomes = pd.read_csv('lab5/medIncome.csv')

mean = 0
sampleMeans = []

def central_limit_histogram(incomes, samples, trials):
    assert type(samples) == int, (str(samples) + ' must be a positive integer!')
    assert type(trials) == int, (str(trials) + ' must be a positive integer!')

    assert samples > 0, (str(samples) + ' must be a positive integer!')
    assert trials > 0, (str(samples) + ' must be a positive integer!')

    for a in range(0, samples):

        for b in range(0, trials):
            income = incomes.sample().mean(0).to_dict()
            mean += income['x']
        mean = mean / 100
        sampleMeans.append(mean)

        print('Mean ' + str(a) + ' to: ' + str(mean))

if __name__ == '__main__':
    for a in range(0, 50):

        for b in range(0, 100):
            income = incomes.sample().mean(0).to_dict()
            mean += income['x']
        mean = mean / 100
        sampleMeans.append(mean)

        print('Mean ' + str(a) + ' to: ' + str(mean))
    graphing.makeHist(sampleMeans, np.arange(0,100000,2000), "test.png")