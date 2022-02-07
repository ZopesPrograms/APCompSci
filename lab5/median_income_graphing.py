import graphing
import random
import pandas as pd

incomes = pd.read_csv('lab5/medIncome.csv')

mean = 0
sampleMeans = []

if __name__ == '__main__':
    for a in range(0, 50):

        for b in range(0, 100):
            income = incomes.sample().mean(0).to_dict()
            mean += income['x'] * income['Unnamed: 0']
        mean = mean / 100
        sampleMeans.append(mean)

        print('Mean ' + str(a) + ' to: ' + str(mean))
