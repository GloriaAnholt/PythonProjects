# Data Visualization Project: Data.gov power prices by zipcode
# 3/16/2016
# @totallygloria

"""
Parses a Data.gov CSV file on power utility prices by zipcode as a JSON file.
"""

import csv


# Full path to CSV/Excel file here
MY_FILE = "iouzipcodes2011.csv"


def parse(raw_file, delim):
    """Parses a raw CSV file to a JSON-like object"""

    opened_file = open(raw_file)
    csv_data = csv.reader(opened_file, delimiter=delim)
    parsed_data = []

    headers = csv_data.next()  # Use first line for headers

    for row in csv_data:
        parsed_data.append(dict(zip(headers, row)))  # Zip together header + value

    opened_file.close()

    return parsed_data


def main():
    new_data = parse(MY_FILE, ",")

    print new_data


if __name__ == "__main__":
    main()
