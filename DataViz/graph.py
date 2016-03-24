"""
Data Visualization Project

Parse data from an ugly CSV or Excel file, and render it in
JSON-like form, visualize in graphs, and plot on Google Maps.

visualize JSON-like data using popular Python math libraries.

Copyright (c) 2013 E. Lynn Root
Distributed under the zlib png license. See LICENSE for details.

Changes copyright (c) 2016 Gloria Guy
"""

from collections import Counter
import csv
import matplotlib.pyplot as plt
import numpy as np
import parse as p


MY_FILE = "../data/sample_sfpd_incident_all.csv"


def visualize_days(parsed_data):
    """Visualize data by day of week"""

    # Returns a dict that sums the total values for each key.
    # keys = DaysOfWeek, values = count of incidents.
    day_totals = Counter(item["DayOfWeek"] for item in parsed_data)

    # Separate out the days to order it correctly when plotting.
    day_list = [
                  day_totals["Monday"],
                  day_totals["Tuesday"],
                  day_totals["Wednesday"],
                  day_totals["Thursday"],
                  day_totals["Friday"],
                  day_totals["Saturday"],
                  day_totals["Sunday"]
                ]
    # plt.xticks() only accepts tuples for labeling the x-axis
    day_tuple = tuple(["Mon", "Tues", "Wed", "Thurs", "Fri", "Sat", "Sun"])

    plt.plot(day_list)       # Assign the data to a plot
    plt.xticks(range(len(day_tuple)), day_tuple)  # Assign labels to the plot from day_list
    plt.savefig("Days.png")  # Save the line graph
    plt.clf()                # Close figure


def visualize_type(parsed_data):
    """Visualize data by category in a bar graph"""
    # Sums the total incidents per Category, graphs in a bar graph
    counter = Counter(item["Category"] for item in parsed_data)

    xlabels = tuple(counter.keys())  # Set x-axis labels (based on the counter's keys)
    xlocations = np.arange(len(xlabels)) + 0.5  # Use numpy to set where labels hit x-axis
    width = 0.5                             # Width of each bar

    # Assign data to a bar plot
    plt.bar(xlocations, counter.values(), width=width)

    # Assign labels and tick location to x-axis
    plt.xticks(xlocations + width / 2, xlabels, rotation=90)

    plt.subplots_adjust(bottom=0.4)         # Add space at bottom so labels aren't cut off
    plt.rcParams['figure.figsize'] = 13, 10  # Make the overall graph/figure larger
    plt.savefig("Type.png")                 # save the graph
    plt.clf()                               # close the figure


def main():
    data_file = p.parse(MY_FILE, ",")
    visualize_days(data_file)
    visualize_type(data_file)


if __name__ == "__main__":
    main()
