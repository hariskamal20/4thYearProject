import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import csv
import seaborn as sns


class Plots:
    def __init__(self):
        pass

    #-----------------------------------------------------------------    
    #Function for regression analysis
    def genrateplotforGeneralConsumption(self):
        #general data setrs regarding comsumption by area
        #With method of LinerRegession
        plt.rcParams['figure.figsize'] = (20.0, 10.0)
        # Reading Data
        data = pd.read_csv('dublin-city-residential-energy-in-each-small-area.csv')
        #print(data.shape)
        #data.head()
        X = data['Estimated Energy Use (kWh)'].values
        Y = data['Total Floor Area'].values
        # Mean X and Y
        mean_x = np.mean(X)
        mean_y = np.mean(Y)
        # Total number of values
        m = len(X)
        # Using the formula to calculate b1 and b2
        numer = 0
        denom = 0
        for i in range(m):
            numer += (X[i] - mean_x) * (Y[i] - mean_y)
            denom += (X[i] - mean_x) ** 2
            b1 = numer / denom
            b0 = mean_y - (b1 * mean_x)

        # Print coefficients
        #print(b1, b0)
        max_x = np.max(X) + 100
        min_x = np.min(X) - 100

        # Calculating line values x and y
        x = np.linspace(min_x, max_x, 1000)
        y = b0 + b1 * x
        # Ploting Line
        plt.plot(x, y, color='#58b970', label='Regression Line')
        # Ploting Scatter Points
        plt.scatter(X, Y, c='#ef5423', label='Scatter Plot')
        plt.xlabel('Annual Energy Use')
        plt.ylabel('Total Floor Area')
    
        plt.savefig('static/genrateplotforGeneralConsumption.png')

