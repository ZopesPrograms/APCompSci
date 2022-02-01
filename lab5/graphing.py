### Lab 5 graphing module ###



## SETUP ##

import numpy as np # this allows us to draw from a normal distribution
import matplotlib.pyplot as plt # this allows us to create graphs
import os # this allows us to create new folders to hold our graphs

# Create a folder to hold all of your graphs
if not os.path.exists('Graphs'):
    os.makedirs('Graphs')



## Creating boxplots and histograms ##

# get samples
mean = 0
std = 1
samples = 1000

mySamples = np.random.normal(mean, std, samples)
mySamples2 = np.random.normal(mean, std, samples)

# visualize samples
# histograms
plt.hist(mySamples, bins=np.arange(-4,4,0.25), density=True)
fileName = "Graphs/Change_Me.png"
plt.savefig(fileName)
plt.close()

# boxplots
plt.boxplot([mySamples, mySamples2], notch=True)
fileName = "Graphs/Change_Me2.png"
plt.savefig(fileName)
plt.close()



## Making lots of boxplots and histograms. ##

def makeHist(mySamples, binSize = np.arange(-5,5,0.1), fileName='histogram.png'):
    '''Creates a histogram and saves file as fileName.

    Parameters
    --
    mySamples: list of floats
        The data to graph.
    binSize: range 
        Defaults to bins of width 0.1 ranging from -5 to +5
    fileName: str
        The name you will give the saved histogram .png file

    Returns 
    --
    None, but saves a histogram
    '''
    pass


def makeBoxplot(mySamplesL, fileName='boxplot.png'):
    '''Creates a boxplot and saves file as fileName.
    Parameters
    --
    mySamples: list of lists of floats
        The datasets to graph.
    fileName: str
        The name you will give the saved boxplot .png file

    Returns 
    --
    None, but saves a boxplot
    '''
    pass


def repeatRandomSamples(trials=10, mean=0, sd=1, sampleSize=1000, binSize = np.arange(-5,5,0.1)):
    '''Creates histograms of samples drawn from a normal distribution and a boxplot comparing all trials.
    Uses the helper functions makeBoxplot and makeHist

    Parameters
    --
    trials: int
        Number of times to repeat random sampling
    mean: float
        Mean of normal distribution to randomly draw from
    sd: float
        Standard deviation of normal distribution to randomly draw from
    sampleSize: float
        The sample size of each individual trial
    binSize: range 
        Defaults to bins of width 0.1 ranging from -5 to +5

    Returns 
    --
    None, but creates histograms and a boxplot
    '''
    pass


if __name__ == '__main__':
    pass # TODO: remove this once you add script code here!