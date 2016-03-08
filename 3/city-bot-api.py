import flask
from flask import request
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
    # get the distribution for the city
    print city
    d = conn.hgetall(city)
    # get the count for the referrer
    try:
      c = d[ref]
    except KeyError:
      return json.dumps({
        "city": city, 
        "prob": 0,
        "referrer": ref
      })
    # get the normalising constant
    z = sum([float(v) for v in d.values()])
    return json.dumps({
      "city": city, 
      "prob": float(c)/z,
      "referrer": ref
      })

    



if __name__ == "__main__":
    app.debug = True
    app.run()
