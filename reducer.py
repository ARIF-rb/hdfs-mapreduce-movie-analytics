#!/usr/bin/env python3

import sys
from decimal import Decimal

# Student ID: 3003263


#  *** Note: This should be set to 10 in your submitted code *** 
# 
# You will want to set it to 10 when running against the large ratings.txt data file.
# You will want to set it to 1 or 2 when running against the smaller r5.txt and r100.txt files
# otherwise films with small numbers of votes will be prevented from producing results
min_votes = 10
current_year = None
highest_avg_rating = 0.0
movies_with_highest_avg = []
print('min_votes = %s' % min_votes, file=sys.stderr)

# Note: The code below does not solve the problem you have been
# given (nor does it use min_votes) but it should help you see
# the keys and values the reducer is receiving, and their ordering.
# You will need to make significant changes to this code to
# implement a solution that produces the correct output.


# You may want to write:
#     * code that filters based on min_votes,
#     * code that averages,
#     * code that finds the highest(s).
#   ...these are just suggestions/hints.

# Process the input line by line
for line in sys.stdin:

    # Parse the input line
    # key, value = line.split('\t')
    year, title, sum_ratings, votes = line.strip().split('\t')
    sum_ratings = Decimal(sum_ratings)
    votes = int(votes)
    if votes >= min_votes:

        avg_rating = sum_ratings / votes

        if current_year == year:
            if avg_rating == highest_avg_rating:
                movies_with_highest_avg.append((f"{year}\t{title}", round(avg_rating, 1)))
            elif avg_rating > highest_avg_rating:
                highest_avg_rating = avg_rating
                movies_with_highest_avg = [(f"{year}\t{title}", round(avg_rating, 1))]

        else:
            if current_year:
                for year_title, title_avg_rating in movies_with_highest_avg:
                    print('%s\t%s' % (year_title, title_avg_rating))
            current_year = year

            highest_avg_rating = avg_rating
            movies_with_highest_avg = [(f"{year}\t{title}", round(avg_rating, 1))]

# Output for the last year processed movie
if current_year:
    for year_title, title_avg_rating in movies_with_highest_avg:
        print('%s\t%s' % (year_title, title_avg_rating))
