#!/usr/bin/env bash

# make sure redis is running!

# run this to insert data into redis
python poisson.py | python diff.py | python insert.py

# run this to poll redis and calculate the moving average from time to time 
python avg.py
