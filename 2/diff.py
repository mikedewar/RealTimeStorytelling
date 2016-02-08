import json
import sys

last = 0
while 1:
    line = sys.stdin.readline()
    d = json.loads(line)
    if last == 0 :
        last = d["t"]
        continue
    delta = d["t"] - last
    print json.dumps({"delta":delta, "t":d["t"]})
    sys.stdout.flush()
    last = d["t"]



