### Lab 5 graphing module ###



## SETUP ##

import numpy as np # this allows us to draw from a normal distribution
import matplotlib.pyplot as plt # this allows us to create graphs
import os # this allows us to create new folders to hold our graphs

# Create a folder to hold all of your graphs
if not os.path.exists('lab5/Graphs'):
    os.makedirs('lab5/Graphs')

## Creating boxplots and histograms ##

# get samples
mean = 0
std = 1
samples = 1000

mySamples = np.random.normal(mean, std, samples)
mySamples2 = np.random.normal(mean, std, samples)

# visualize samples
# histograms
plt.hist(mySamples, bins=np.arange(-4,4,0.25), density=False)
fileName = "lab5/Graphs/Change_Me.png"
plt.savefig(fileName)
plt.close()

# boxplots
plt.boxplot([mySamples, mySamples2], notch=True)
fileName = "lab5/Graphs/Change_Me2.png"
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
    None, but saves a histogram in Graphs folder
    '''

    # Creates histogram out of samples, saves it in Graphs folder under fileName.
    plt.hist(mySamples, bins=binSize, density=True)
    plt.savefig("lab5/Graphs/" + fileName)
    plt.close()


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
    None, but saves a boxplot in Graphs folder
    '''

    # Creates boxplot out of samples, saves it in Graphs folder under fileName.
    plt.boxplot(mySamplesL, notch=True)
    plt.savefig("lab5/Graphs/" + fileName)
    plt.close()


def repeatRandomSamples(trials=10, mean=0, sd=1, sampleSize=1000, binSize = np.arange(-5,5,0.1), folderName=""):
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
    foldername: str
        The name of the folder in which to save our random sampling

    Returns 
    --
    None, but creates histograms and a boxplot
    '''

    ''' Creates folder by "folderName" in Graphs folder to hold 
        sample results graphs. '''

    if not os.path.exists('lab5/Graphs/'+folderName):
        os.makedirs('lab5/Graphs/'+folderName)

    # Randomized samples list defined here
    samples = []

    # Run 'trials' number of normal curve samplings
    for i in range(0,trials):

        ''' Generates normal curve probability centering around mean with
            standard deviation 'sd' and 'sampleSize' sample size. '''
        
        temp = np.random.normal(mean, sd, sampleSize)

        ''' Append normal list to sample list, and make histogram of 
        normal curve list. '''

        samples.append(temp)
        makeHist(temp, binSize, (folderName + "/normal" + str(i) + ".png"))

    # Make boxplot from list of normal curve samples
    makeBoxplot(samples, (folderName + "/cumulative_normals.png"))

# MAIN CODE BLOCK
if __name__ == '__main__':

    # Make random samplings as directed in lab 5 directions.
    repeatRandomSamples(folderName="original")

    repeatRandomSamples(mean=0, sd=1, sampleSize=15, folderName="2-1")
    repeatRandomSamples(mean=0.5, sd=1, sampleSize=15, folderName="2-2")
    repeatRandomSamples(mean=2, sd=1, sampleSize=15, folderName="2-3")

    repeatRandomSamples(mean=0, sd=1, sampleSize=1000, folderName="2-4")
    repeatRandomSamples(mean=0.5, sd=1, sampleSize=1000, folderName="2-5")
    repeatRandomSamples(mean=2, sd=1, sampleSize=1000, folderName="2-6")