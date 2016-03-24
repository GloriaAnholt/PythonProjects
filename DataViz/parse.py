"""
Data Visualization Project

Parse CSV file as JSON.

Copyright (c) 2013 E. Lynn Root
Distributed under the zlib png license. See LICENSE for details.

Changes copyright (c) 2016 Gloria Guy
"""

import csv


# Put the full path to your CSV/Excel file here
MY_FILE = "../data/sample_sfpd_incident_all.csv"


def parse(raw_file, delim):
    """Parses a raw CSV file to a JSON-like object"""

    opened_file = open(raw_file)
    csv_data = csv.reader(opened_file, delimiter=delim)
    parsed_data = []

    fields = csv_data.next()  # Use first line for headers

    for row in csv_data:
        parsed_data.append(dict(zip(fields, row)))  # Zip together header + value

    opened_file.close()

    return parsed_data


def main():
    new_data = parse(MY_FILE, ",")

    print new_data


if __name__ == "__main__":
    main()
