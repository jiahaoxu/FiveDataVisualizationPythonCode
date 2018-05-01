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
    ax.plot(x_data, y_data, lw=2, color=color, alpha=0.75)

    if yscale_log:
        ax.set_yscale('log')

    # labels and title
    ax.set_title(title)
    ax.set_xlabel(x_label)
    ax.set_ylabel(y_label)

    plt.show()


def histogram(data, bins, cumulative=False, x_label='', y_label='', title='', color='r', yscale_log=False):
    plt.rcParams["patch.force_edgecolor"] = True
    _, ax = plt.subplots()
    ax.hist(data, bins=bins, cumulative=cumulative, color=color)
    # labels and title
    ax.set_title(title)
    ax.set_xlabel(x_label)
    ax.set_ylabel(y_label)

    plt.show()


def overlaid_histogram(data1, data2, bins=0, data1_name='', data1_color='r', data2_name='', data2_color='g', x_label='', y_label='', title='', yscale_log=False):
    # overlaid two histograms to compare them

    # set the bounds for the bins so that the two distributions are fairly compared
    max_nbins = 20
    data_range = [min(min(data1), min(data2)), max(max(data1), max(data2))]
    bin_width = (data_range[1] - data_range[0]) / max_nbins

    if bins == 0:
        # set up the bin list
        bins = np.arange(data_range[0], data_range[1] + bin_width, bin_width)
    
    _, ax = plt.subplots()
    ax.hist(data1, bins, color=data1_color, alpha=1, label=data1_name)
    ax.hist(data2, bins, color=data2_color, alpha=0.75, label=data2_name)
    # labels and title
    ax.set_title(title)
    ax.set_xlabel(x_label)
    ax.set_ylabel(y_label)
    ax.legend()

    plt.show()


def barplot(x_data, y_data, error_data, x_label='', y_label='', title=''):
    _, ax = plt.subplots()
    # draw bars, position them in the center of the tick mark on the x-axis
    x = range(len(x_data))
    ax.bar(x, y_data, color='r', align='center')
    # draw error bars (could be standard deviation)

    ax.errorbar(x, y_data, yerr=error_data, color='black', ls='none', lw=2, capthick=2)
    plt.xticks(x, x_data)

    ax.set_title(title)
    ax.set_xlabel(x_label)
    ax.set_ylabel(y_label)

    plt.show()


def group_barplot(x_data, y_data_list, colors, error_data=[], y_data_names=[], x_label='', y_label='', title=''):
    _, ax = plt.subplots()
    # total width for all bars at one x location
    totol_width = 0.8
    # width of each individual bar
    ind_width = totol_width / len(y_data_list)
    # center each group of bars about the x tick mark
    alteration = np.arange(-totol_width/2 + ind_width/2, totol_width/2, ind_width)

    print alteration

    x = range(len(x_data))
    # draw bars, one category at a time
    for i in range(len(y_data_list)):
        # move the bar to the right on the x-axis so that it won't
        # overlap with previous drawn ones
        ax.bar(x + alteration[i], y_data_list[i], color=colors[i], label=y_data_names[i], width=ind_width)
        if len(error_data) != 0:
            ax.errorbar(x + alteration[i], y_data_list[i], yerr=error_data[i], color='black', ls='none', lw=2, capthick=2)
    
    plt.xticks(x, x_data)
    ax.set_title(title)
    ax.set_xlabel(x_label)
    ax.set_ylabel(y_label)
    ax.legend()

    plt.show()