# Exercise 1 - 1/27/2016
## due on 2/10/2016

The aim of this exercise is to encourage you to explore and consume data you can find in the world, with a focus on streaming data. This exercise will make sure you can build a minimal pipeline from a data source to a webpage where that data can be seen by a reader. Subsequent exercises will flesh out this pipeline. 

## Definition

The exercise is split into three parts:

1. Find, or create, a stream of data. This can be anything you find compelling, and can be an event stream or a polled API. Write a README.md describing what an individual message in the stream represents in the real world, and therefore what volume of messages you expect in the stream. (40%)
2. Consume the messages in the stream using technology of your choice. (40%) Your solution should expect to stay on forever. It should:
  * consume the stream from its source
  * perform any basic cleaning, transformations, or filters (optional)
  * writes the output of the consumer to `stdout` so we can see it in a terminal
3. Create a websocket server that emits the messages and webpage that consumes them. The webpage can be as simple or as complex as you'd like; we simply want to make sure everyone can get data onto a webpage. Plese use the Chrome web browser. (20%)

## Grading

1. Part 1 of the exercise will be graded on the clarity of the description of the stream. We will be looking for evidence a clear understanding of how each message relates to an event in the world, and 
2. Part 2 will be graded primarily using the code comments in the consumer. We are looking for a clear description of how the code works. We will also attempt to run the code briefly to make sure it writes messages to `stdout`. 
3. Part 3 will be graded on the quality of presentation of the generated page. 

## Inspiration

In case you are lacking in inspiration for data sources, try exploring:
* GDELT [http://www.gdeltproject.org/](http://www.gdeltproject.org/)
* City data sets e.g.[http://datamine.mta.info/](http://datamine.mta.info/)
* Environmental data [http://developer.epa.gov/category/data/](http://developer.epa.gov/category/data/)
* Online chat rooms [https://api.slack.com/rtm](https://api.slack.com/rtm)

Also check out Jeremy Singer-Vine's email list http://tinyletter.com/data-is-plural.

## Resouces

* The folder containing this file also contains:
  * examples from class consuming public data
  * barebones `index.html` that has the code for consuming a websocket and manipulating elements in a webpage in response to messages from that websocket
