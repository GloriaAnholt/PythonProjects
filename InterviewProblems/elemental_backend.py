# Elemental Technologies: Back-end Web Dev Screening Question
# 02.25.2016
# @totallygloria

"""
Write a program that parses the inventory and answers the following questions:

1. What are the 5 most expensive items from each category?
2. Which cds have a total running time longer than 60 minutes?
3. Which authors have also released cds?
4. Which items have a title, track, or chapter that contains a year.

read the inventory from stdin, and it should print your answers to stdout

run through all of it exactly once, add new types to a dictionary as you find them,
and then just keep track of the top five items with some logic that compares current
item to some stored largest ones and bumps the list as necessary
"""


# json.loads - load a json-formatted file in as a python value
# json.dumps - dump python values into a json-formatted file

import sys
import json


inventory = json.loads(open('elemental_data.txt').read())

for d in inventory:
    print 'title:', d["title"]
    print 'cost:', d["price"]

    # task 1: check the type, if it's new, make a new entry in the exp dict
    # exp dict should be {'type':'type', 'top 5':['name':'#',
    #                                             'name':'#'
    #                                             'name','#']}

    # thing 2: made a cd_timing dict
    # if d["type"] == "cd":
    #           for track in d["tracks"]:
    #               total_time += d["tracks"]["seconds"]

    # thing 3: make an author-list which compares to cd authors and sets something to true?

    # thing 4: title, track or chapter with a year
    # can you search for a 4-digit number less than 2016? Of just a 4-digit number?
    # What about 2112? Or something before 1000?