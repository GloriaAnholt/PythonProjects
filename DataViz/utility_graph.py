"""
Data Visualization Project

1. Parse data from a CSV file, render it in JSON-like form,
2. visualize in graphs using matplotlib, and 3. plot using GeoJSON.

"""

from collections import Counter
import csv
import matplotlib.pyplot as plt
import numpy as np
import csv_parser as p


MY_FILE = "iouzipcodes2011.csv"


def visualize_companies(parsed_data):

    zips_per_company = Counter(item["utility_name"] for item in parsed_data)

    price_per_co = []
    name_cache = set()
    for item in parsed_data:
        if item['utility_name'] in name_cache:
            pass
        else:
            name_cache.add(item['utility_name'])
            price_per_co.append(dict(utility_name=item['utility_name'], res_rate=item['res_rate']))

    print price_per_co


    company_tuple = tuple(zips_per_company)
    '''
    plt.plot(company_totals)       # Assign the data to a plot
    plt.xticks(range(len(company_tuple)), company_tuple)  # Assign labels to the plot from day_list
    plt.savefig("companies.png")  # Save the line graph
    plt.clf()                # Close figure
    '''

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
    visualize_companies(data_file)
    #visualize_type(data_file)


if __name__ == "__main__":
    main()
