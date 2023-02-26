import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from data_plot_formatter import getRatingsAsCountedAmounts, getRatingsAsList


def plotRatingsCount() -> None:
    ratings = getRatingsAsCountedAmounts('helpdistribution.csv')
    figure = plt.figure()
    ax = figure.add_axes([0.1,0.1,0.7,0.9])
    xaxis = [1,2,3,4,5]
    ax.bar(xaxis, ratings)
    plt.show()

#plotRatingsCount()







