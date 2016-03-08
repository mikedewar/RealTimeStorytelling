#!/usr/bin/env bash

python poll-NYT-citibike.py | python buildGraph.py &
python graphServer.py &
python forget.py
