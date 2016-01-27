import requests
import json
import time

oldAvailableBikes = 0
while True:
    # get the citibike response from their API
    r = requests.get("https://www.citibikenyc.com/stations/json")
    # extract my favourite citibike station
    for m in r.json()["stationBeanList"]:
        if m["stationName"] == "W 41 St & 8 Ave":
            availableBikes = m["availableBikes"]
            print availableBikes
            print m
            if availableBikes > oldAvailableBikes:
                print "{'new bikes returned':%s}"%availableBikes-oldAvailableBikes
            if availableBikes < oldAvailableBikes:
                print "{'bikes taken':%s}"%oldAvailableBikes-availableBikes
            break
    oldAvailableBikes = availableBikes
    time.sleep(10)
