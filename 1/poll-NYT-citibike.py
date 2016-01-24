import requests
import json
import time

while True:
    # get the citibike response from their API
    r = requests.get("https://www.citibikenyc.com/stations/json")
    # extract my favourite citibike station
    for m in r.json()["stationBeanList"]:
        if m["stationName"] == "W 41 St & 8 Ave":
            print json.dumps(m, indent=1)
    time.sleep(10)
