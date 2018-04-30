import matplotlib.pyplot as plt
import numpy as np

def scatterplot(x_data, y_data, x_label='', y_label='', title='', color='r', yscale_log=False):
    # create the plot object
    _, ax = plt.subplots()

    # plot the data, set the size, color and transparancy (alpha)
    ax.scatter(x_data, y_data, s=10, color=color, alpha=0.75)

    if yscale_log:
        ax.set_yscale('log')

    # labels and title
    ax.set_title(title)
    ax.set_xlabel(x_label)
    ax.set_ylabel(y_label)

    plt.show()

def lineplot(x_data, y_data, x_label='', y_label='', title='', color='r', yscale_log=False):
    # create the plot object
    _, ax = plt.subplots()

    # plot the data, set the size, color and transparancy (alpha)
    ax.plot(x_data, y_data, s=10, color=color, alpha=0.75)

    if yscale_log:
        ax.set_yscale('log')

    # labels and title
    ax.set_title(title)
    ax.set_xlabel(x_label)
    ax.set_ylabel(y_label)

    plt.show()