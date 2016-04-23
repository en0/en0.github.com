Title: Python Vs Node.js
Date: 2016-04-17 12:15
Tags: Node,Python,Vs
Category: Programming
Slug: python-vs-nodejs
Author: Ian Laird
Summary: A comparison between the execution speed of Python and Node.js

![Python-vs-NodeJs](/images/python-vs-nodejs.png)

<br/>

Python is my tool of choice for random development tasks. It's clean, it has
many useful and maintained packages, and the environment is most always
available. This makes Python a wonderful, get it done tool.

Node.js is a new language to me. We have begun to use it quite heavily at work
and it is clearly gaining popularity in the development communities. I have a
long list of things I dislike about Node.js but we will save that for another
time.

What I want to share with you today is the result of some performance testing
that I did to see the execution speed of Node.js as it compared to Python. To be
clear, I am __not__ talking about the event loop model. I am talking about the
interpretation of a _task_ to its fulfillment by the underlining system.

_A link to the code is available at the bottom of this page._

# Testing Concept

Each of these tests were run 10 times. The metrics defined in each test were
averaged to produce a score. The scores are listed below the graph in each
case. The idea was to calculate the amount of work that could be done in a
given amount of time, or the amount of time it might take to do a given amount
of work, and compare to the opposing language.

---

# Case 1 - Blocking IO

Blocking IO is a very common thing in software development. This occurs
whenever a program accesses a disk or network resource. Some examples might be
database operations, web requests, logging messages, and sending emails.

Blocking IO is a scenario that should showcase Node.js's ability for effective
and efficient use of resources. And as you will see in the results, it does.

## Scenario

The task requires two fairly slow operations:

1. A web request to DynamoDB to increment a field. (Atomic Update Expression)
2. Write the result of that operation into a file.

This operation will execute 50 times. The amount of time it takes to complete
all 50 transactions is converted to a rate. This is considered one test.

__Due to a bug in the loop counter, only 9 iterations where run on the Node.js
implementation. The final run of the Python version of this task was removed to
align the graph results.__

## Results

The results are not surprising. Node.js had a much higher throughput as it was
able to write results while waiting for other requests to complete. Python was
much more consistent but I think we can attribute that to the read consistency of
DynamoDB.

<iframe width="100%" height="400" frameborder="0" scrolling="no"
src="https://plot.ly/~en0/1.embed?share_key=uhc9Ur6HklbIiIf5UJFxi5"></iframe>

__Python Average Rate: 22.6860528133__

__Node.js Average Rate: 164.79096160949314__

---

# Case 2 - The Consumer

Consumers are basically workers that take tasks from a queue or stack to be
processed. Consumers are usually built to be as stateless as possible to
afford the opportunity for scale out to increase throughput of a system. It is
an elegant and efficient model.

This test has a small amount of Blocking IO and a small amount of bound CPU
time.  This is a common situation for most consumer based solutions.

## Scenario

The test requires the application to pull a task from a queue and process it.

Processing a task consists of the following steps:

1. Decode the task message.
2. Count an integer up to the value specified in the task message.
3. Acknowledge the completion of the task to the queueing system.
4. Increment internal counters.

The application is given 10 seconds to process as many requests as possible. At
the end of 10 seconds the number of completed tasks (acknowledged tasks) is
used to calculate the transfer rate. This is one test.

_NOTE: A prefetch limit was set to 1. This forced a task to be completed before
the next task would be dispatched. This should affectively take away the
Node.js event loop advantage._

## Results

The results were closer by percentage, but Node.js still out performed Python by
a rather significant margin. I was surprised by this result. I assumed with the
prefetch limitation and the small amount of blocking IO, the throughput would
be much closer.  As you can see, my assumption was far from accurate.

<iframe width="100%" height="400" frameborder="0" scrolling="no"
src="https://plot.ly/~en0/3.embed"></iframe>

__Python Average Transfer Rate: 1499.1499893__

__Node.js Average Transfer Rate: 2037.2523271178175__

---

# Case 3 - The Recursive Fibonacci

Fibonacci is a classic CPU bound benchmark test. It requires a lot processor
activity to calculate and very little (if any) blocking IO. I decided to use a
recursive approach simply because it is not efficient. It put both Python and
Node.js in the difficult situation of brute forcing the calculation and thus
generating a significant amount of CPU utilization.

## Scenario

The test requires the application to calculate the 10th, 20th, and 30th
Fibonacci numbers using a recursive algorithm.

The time it took to calculate these numbers was stored as the metric. This
defines one test. For the additional datapoint, I also included a C
implementation in this test as a baseline.

## Results

The results where quite amazing to me. Not only did Node.js out perform Python,
Node.js crushed Python in a CPU bound process with zero blocking IO.  The margin
between Node.js and Python is nearly as much as the margin between C and Python.

__Edit: I ran this test again using [PyPy](http://pypy.org/download.html) and added the
results into the graph.__

_Note: The graph is using a logarithmic scale for visibility._

<iframe width="100%" height="400" frameborder="0" scrolling="no"
src="https://plot.ly/~en0/7.embed"></iframe>

__Python Averaged Elapsed Time: 0.278023791313 Seconds__

__Node.js Averaged Elapsed Time: 0.012099999999999998 Seconds__

__C Average Elapsed Time: 0.0064275 Seconds__

__PyPy Average Elapsed Time: 0.02586944103239 Seconds__

---

# Conclusion

In review of these test results, my conclusion is that Node.js is a fast and
performant language.  It gets the most out of available resources by reducing
idle time thanks to the event loop model. In synchronous tasks, it is able to
impressively out perform other interpreted languages. In the case of the
Fibonacci test, Node.js was closer to C's execution time then it was to
Python's. Given the layers of abstraction involved in an interpreted language,
this is impressive indeed.

Node.js has already proven itself as a viable language for serious programing
jobs. The community doesn't need me for that. It has been gaining popularity
for some time now. But these tests opened my eyes to the possibilities available
using this language and I look forward to learning more about.

There are many more data points to investigate but given my recent experience,
Node.js will be another good candidate for consideration in future projects.

On a side note, I am disappointed by Python's performance in at least two of
these cases. I feel that it should have done better. I know I could speed up the
CPU bound tasks by using more memory efficient algorithms: Python is a memory
hog.

# Disclaimer

I am not a seasoned Node.js developer. I am sure these implementations will
make many Node.js developers cry. But I am a seasoned Python developer and
these Python implementations make me cry. We can frown at the code together.
Feel free to offer additional ways to calculate these metrics.

That said, I did not try to write good code here. Just effective enough code to
gather the data points.  If you feel the code is negatively impacting the test,
please let me know. I will update it.  Realistically, both the Python and the
Node.js code are equally terrible. Deal with it.

Also, keep in mind these stats really only calculate _human waiting_ time and do
not include other extremely important metrics such as memory utilization.

---

Source coude available on [GitHub](https://github.com/en0/python-vs-nodejs)
