import json
import sys
import redis
import time

conn0 = redis.Redis(db=0)
conn1 = redis.Redis(db=1)

stations = {}

while True:
    line = sys.stdin.readline()
    try:
        d = json.loads(line)
    except ValueError:
        continue

    x = d["stationName"]
    y = d["availableBikes"]
    
    if x not in stations:
        stations[x] = y
        continue

    old = stations[x]
    stations[x] = y
    
    if old != y:
        conn0.setex(x,y,120)
        print json.dumps({"name": x, "diff": y-old})
        sys.stdout.flush()

        keys = conn0.keys("*")
        
        for k in keys:
            n = conn0.get(k)
            if n:
                conn1.hincrby(x, k, 1) 
                #conn1.hincrby(k, x, 1) 

    
