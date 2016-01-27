# lecture 1 - consuming streams

The aim of this session is to learn how to consume a stream of data in a very simple way. We'll consume an event stream from bitly, and generate a sampled stream from citibike. Specifically we will:

* learn how to consume a long-lived HTTP stream
* learn how to poll an API and watch for changes
* learn how to connect command line tools using pipes
* be introduced to the `jq` and `websocketd` tools
* learn how to consume from a websocket inside a browser using javascript

roughly, our schedule looks like

* curl the bitly stream
* discuss how we are receiveing data
* quickly review pipes, and meet `jq`
* make a websocket server using `websocketd`
* log the stream in the browser's console log

**BREAK**

* curl the citibike API
* do the same with python
* detect changes to citibike stations, serve via websocket
* build a page, served with a python simple server, that uses d3 to modify DOM elements in the browser

We'll finish by talking about the exercise.
