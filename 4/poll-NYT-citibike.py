#!/usr/local/bin/python
import requests
import json
import time

while True:
    # get the citibike response from their API
    r = requests.get("https://www.citibikenyc.com/stations/json")
    # extract my favourite citibike station
    for m in r.json()["stationBeanList"]:
        print json.dumps(m)
    time.sleep(2)
