import json
import sys
import redis
import time
import urlparse

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
        # then let's just ditch it
        continue

    try:
        referrer = d["r"]
    except KeyError:
        # if there is no referrer present in the message
        # then let's just ditch it
        continue

    if referrer == "direct":
        netloc = "direct"
    else:
        o = urlparse.urlparse(referrer)
        netloc = o.netloc

    conn.hincrby(city, netloc, 1)
    print json.dumps({"cy": city, "r": netloc})
    sys.stdout.flush()
