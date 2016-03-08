import flask
import redis
import json

app = flask.Flask(__name__)
conn = redis.Redis(db=1)

@app.route("/")
def index():
    return flask.render_template('index.html')

@app.route("/graph")
def buildGraph():

    links = []

    stations = conn.keys("*")

    stationsWithEdges = []
    nodeIndex = {}

    # for each node we'll get the edges for that node, and add them
    # to the edge list
    for station in stations:
        for target,weight in conn.hgetall(station).items():
            weight = int(weight)
            if weight > 2:
                if station not in nodeIndex:
                    nodeIndex[station] = len(nodeIndex)
                    stationsWithEdges.append(station)
                if target not in nodeIndex:
                    nodeIndex[target] = len(nodeIndex)
                    stationsWithEdges.append(target)
                links.append({"source":nodeIndex[station], "target":nodeIndex[target], "weight":weight})
            
    nodes = [{"name":s, "group":0} for s in stationsWithEdges]
    graph = {"links":links, "nodes":nodes}
    print json.dumps(graph, indent=1)

    return json.dumps(graph)


if __name__ == "__main__":
    app.debug = True
    app.run()


