#!/usr/bin/env python3

import sys

# Student ID: 3003263

# Read included years
with open('years.txt', 'r') as f:
    included_years = f.read().split()
    # Print debug/info message to stderr

# Process the input line by line
for line in sys.stdin:

    # Parse the input line
    uid, title, genres, year, rating = line.strip().split('\t')
    # Output the title and a count of 1.
    # Note: This IS NOT the CORRECT approach but should give you a useful starting point
    # print('%s\t%s' % (title, 1))
    # print(genres)
    if (not included_years) or (included_years and year in included_years):
        for genre in genres.split('|'):
            print("%s\t%s\t%s" % (year, title, rating))


