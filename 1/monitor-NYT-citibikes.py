#!/usr/bin/env python
import requests
import json
import time
from sys import stdout

# this script polls the citibike API, looking for changes in the number of 
# citibikes at each station

availableBikes = {}

while True:
    # get the citibike response from their API
    r = requests.get("https://www.citibikenyc.com/stations/json")
    for m in r.json()["stationBeanList"]:
        # for each station, initialise the store if necessary
        if m["stationName"] not in availableBikes:
            availableBikes[m["stationName"]] = m["availableBikes"]
            continue

        delta = m["availableBikes"] - availableBikes[m["stationName"]]

        # if the number of bikes have changed, emit a message
        if delta != 0:
            print '{"station":"%s","bikeDelta":"%s"}'%(m["stationName"], delta)
            stdout.flush()

        # update the store with the new number of available bikes for that station
        availableBikes[m["stationName"]] = m["availableBikes"]
    time.sleep(2)
