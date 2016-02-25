import flask
import redis
import collections
import json
import numpy as np

app = flask.Flask(__name__)
conn = redis.Redis()

def buildHistogram():
    keys = conn.keys()
    values = conn.mget(keys)
    c = collections.Counter(values)
    z = sum(c.values())
    return {k:v/float(z) for k,v in c.items()}

@app.route("/")
def histogram():
    h = buildHistogram()
    return json.dumps(h)

@app.route("/entropy")
def entropy():
    h = buildHistogram()
    return -sum([p*np.log(p) for p in h.values()]) 

@app.route("/probability")
def probability():
    city = request.args.get('city', '')
    ref = request.args.get('referrer', '')
    d = conn.hget(city,ref)
    return d

    



if __name__ == "__main__":
    app.debug = True
    app.run()
