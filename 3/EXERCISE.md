# Exercise 2 - 2/24/16

The aim of this exercise is to flesh out your beat robot. 

# Definition

1. Build a system to track a distrbution or set of distributions that capture something you find interesting about a stream of data. (40%)
2. Build an API that can return:
 * * the rate of the stream
 * * the distributions you assembled in the first part of this exercise
 * * the entropy of the distributions
 * * the probability of a new message given the stored distributions (40%)
3. Extend the alerting system you built in Exercise 2 to alert on changes in entropy or unlikey new messages. (10%)
4. Build a webpage that displays the current distribution(s) stored in your system by querying the API you build in the second part of this exercise. (10%)

# Grading

For parts 1 and 2 we will grade by reading, and potentially running, the code you submit. As before, we are looking for clear descriptions of why you made the coding decisions you did from the comments. 

For part 3 we are looking for comments (which can be in the code or a README) that indicate how you chose the conditions under when you alert. 

For part 4 we are looking for an interface that allows you to keep track of the state of your beat robot, to make sure it is behaving as expected. It is up to you to decide how to show this in a webpage. 
