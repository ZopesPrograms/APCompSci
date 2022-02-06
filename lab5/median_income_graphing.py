import graphing
import random
import pandas as pd

incomes = pd.read_csv('lab5/medIncome.csv')
backup = incomes.copy()

mean = 0
sampleMeans = []

if __name__ == '__main__':
    print(incomes)
    '''for a in range(0, 50):
        incomes = backup.copy()
        random.shuffle(incomes)

        mean = 0
        for b in range(0, 100):
            mean += incomes.pop()
        mean = mean / 100
        sampleMeans.append(mean)

        print('Mean ' + str(a) + ' to: ' + str(mean))'''
