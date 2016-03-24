"""
Data Visualization Project

Parse JSON-like data, visualize in graphs, and plot as a map.

Copyright (c) 2013 E. Lynn Root
Distributed under the zlib png license. See LICENSE for details.

Changes copyright (c) 2016 Gloria Guy
"""

import geojson
import parse as p


def create_map(data_file):
    """Creates a GeoJSON file.
    Returns a GeoJSON file that can be rendered in a GitHub Gist at gist.github.com.
    GitHub will automatically render the GeoJSON file as a map.
    """

    geo_map = {"type": "FeatureCollection"}  # Define type of GeoJSON we're creating
    item_list = []                           # collects each point to graph

    # Iterate over our data using enumerate() to get the line, and the index
    for index, line in enumerate(data_file):
        if line['X'] == "0" or line['Y'] == "0": # Zero coordinates throw off the map
            continue

        data = {}  # Use a new dictionary for each iteration.

        # Assign line items to appropriate GeoJSON fields.
        data['type'] = 'Feature'        # goeJSON FeatureCollections must contain Features
        data['id'] = index              # Features must have properties & geometries
        data['properties'] = {'title': line['Category'],
                              'description': line['Descript'],
                              'date': line['Date']}
        data['geometry'] = {'type': 'Point',
                            'coordinates': (line['X'], line['Y'])}

        # Add data dictionary to our item_list
        item_list.append(data)

    # For each point in our item_list, we add the point to our dictionary.
    # setdefault creates a key called 'features' w/ the value of an empty list.
    # Each iteration appends the current X,Y point to the geo_map list.
    for point in item_list:
        geo_map.setdefault('features', []).append(point)

    # With data parsed into GeoJSON, write to a file to upload to gist.github.com
    with open('file_sf.geojson', 'w') as f:
        f.write(geojson.dumps(geo_map))


def main():
    data = p.parse(p.MY_FILE, ",")

    return create_map(data)


if __name__ == '__main__':
    main()
