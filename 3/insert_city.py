import json
import sys
import redis
import time

conn = redis.Redis()

while 1:
    line = sys.stdin.readline()
    try:
        d = json.loads(line)
    except ValueError:
        # sometimes we get an empty line, so just skip it
        continue

    try:
        city = d["cy"]
    except KeyError:
        # if there is no city present in the message
        # then store a "null" city
        city = "null"

    t = str(time.time())
    conn.setex(t, city, 120)
    print json.dumps({"t":t, "cy":city})
    sys.stdout.flush()
