import matplotlib
matplotlib.use("TkAgg")
import numpy as np
import matplotlib.pyplot as plt


class Graph:
    def __init__(self):
        self.num_cities = 4

    def plotData(self, title, positives, negatives, neutrals):
         # create plot
        fig, ax = plt.subplots()

        index = np.arange(self.num_cities)
        bar_width = 0.25
        opacity = 0.8

        rects1 = plt.bar(index, positives, bar_width,
        alpha=opacity,
        color='g',
        label='Positive')

        rects2 = plt.bar(index + bar_width, negatives, bar_width,
        alpha=opacity,
        color='red',
        label='Negative')

        rects3 = plt.bar(index + 2 * bar_width, neutrals, bar_width,
        alpha=opacity,
        color='y',
        label='Neutral')

        plt.xlabel('Cities')
        plt.ylabel('Sentiment')
        plt.title('Sentiment by city for phrase {}'.format(title))
        plt.xticks(index + bar_width, ( 'Seattle', 'San Francisco', 'Chicago', 'NYC'))
        plt.legend()

        plt.tight_layout()
        plt.show()
