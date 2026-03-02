#!/usr/bin/env python3

import sys


# Student ID: 3003263
current_movie = None
current_movie_user_votes = 0
current_movie_ratings_sum = 0.0


# Process the input line by line
for line in sys.stdin:

    year, title, rating = line.strip().split('\t')
    # key = f"{title}\t{year}"
    movie = "%s\t%s" % (year.strip("\t"), title.strip("\t"))
    rating = float(rating)
    if movie == current_movie:

        current_movie_user_votes += 1
        current_movie_ratings_sum += rating
    else:
        if current_movie:
            print("%s\t%s\t%s" % (current_movie, current_movie_ratings_sum, current_movie_user_votes))

        current_movie = movie
        current_movie_user_votes = 1
        current_movie_ratings_sum = rating

if current_movie:
    print("%s\t%s\t%s" % (current_movie, current_movie_ratings_sum, current_movie_user_votes))




