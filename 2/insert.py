import json
import sys
import redis

conn = redis.Redis()

while 1:
    line = sys.stdin.readline()
    d = json.loads(line)
    delta = d["delta"]
    time = d["time"]
    conn.setex(time, delta, 120)
    print json.dumps({"time":time, "delta":delta})
