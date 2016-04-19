Title: Python Vs NodeJS
Date: 2016-04-17 12:15
Tags: Node,Python,Vs
Category: Programming
Slug: python-vs-nodejs
Author: Ian Laird
Summary: Task execution speed: Python or NodeJS?

![Python-vs-NodeJs](/images/python-vs-nodejs.png)

<br/>

Python is genrally my tool of choice for random development tasks. It's clean,
it has many usefull and maintained packages, and the environment is most always
available. This make Python a wonderful, get it done, tool IMHO.

NodeJS is a newer language to me. We use it quite heavly at work and it is
clearly gaining popularity in the development communities. I have a long list
of things i dislike about NodeJs but we will save that for another time.

What i wanted to share today is the result of some performance testing I did to
see the execution speed of NodeJs as it compaired to Python. To be clear, I am
_not_ talking about the event loop model. I am talking about the interpritaion
of an instruction to it being fufilled by the underlining system.

A link to the code is available at the bottom of this page.

# Testing Concept

Each of these tests were ran 10 times and the metric defined in each test were
averaged to produce a score. The scores are listed below the graph in each
case. The idea was to calculate the amount of work that could be done in a
given amount of time or the amount of time it would take to do a given amount
of work.

---

# Case 1 - Blocking IO

Blocking IO is a very common thing in software development. This occurse
whenever you access a disk or network resource. Examples are things such as
database operations, web requests, logging messages, sending emails and so on.

Blocking IO is a senario that should showcase NodeJs's ability for effective
and efficient use of resources. And as you will see in the results, it does.

## Senario

The task requires two fiarly slow operations.

1. A web request to DynamoDB to increment a field using an atomic update
   expresstion.
2. Write the result of that opperation into a file.

This operation will execute 50 times. The amount of time it takes to complete
all 50 transactions is converted to a rate and is recorded as one test.

__Due to a bug in my loop count (off by 1 error) only 9 iterations where ran
on this test__

## Results

The results are not supprising. NodeJs had a much higher throughput as it was
able to write results while waiting for other requests to complete. Python was
much more consistant but I think we can give that to the read consistatncy of
DynamoDB. 

<iframe width="100%" height="400" frameborder="0" scrolling="no"
src="https://plot.ly/~en0/1.embed?share_key=uhc9Ur6HklbIiIf5UJFxi5"></iframe>

__Python Average Rate: 22.6860528133__

__NodeJs Average Rate: 164.79096160949314__

---

# Case 2 - The Consumer

Consumers are basicly workers that take tasks from a queue or stack that are
then processed. Consumers are ushually built to be as statless as possible to
aford the opertunity for scale out the increase throuput of a system. It is a
eligant and efficient model.

This test has a small amount of Blocking IO and a small amount of bound CPU
time.  This is a common situation for most consumer based solutions.

## Senario

The test requires the application to pull a task from a queue and process it.

Processing a task consist of the following steps:

1. Decode the task message.
2. Count an integer up to the value specified in the task message.
3. Acknowledge the completion of the task to the queueing system.
4. Increment internal counters.

The application is given 10 seconds to process as many requests as possible. At
the end of 10 seconds the number of completed tasks (acknowldeged tasks) is
used to calculate the transfer rate. This is one test.

_NOTE: A prefetch limit was set to 1. This forced a task to be completed before
the next task would be dispatched. This should effectivly take away NodeJs
event loop advantage._

## Results

The results where closer by percentage but NodeJs still out performed Python by
a rather significant margin. I was supprised by this result. I assumed with the
prefrech limitation and the small amount of blocking IO, the throughput would
be much closer.  As you can see, my assumption was far from accurate.

<iframe width="100%" height="400" frameborder="0" scrolling="no"
src="https://plot.ly/~en0/3.embed"></iframe>

__Python Average Transfer Rate: 1499.1499893__

__NodeJs Average Transfer Rate: 2037.2523271178175__

---

# Case 3 - The Recursive Fibonacci

Fibonacci is a classic CPU bound benchmark test. It requires a lot processor
activity to calculate and very little (if any) blocking IO. I decided to use a
recursive approach simply because it is not efficient. It put both Python and
NodeJs in the difficult situation of brute forcing the calculation and thus
generating a significant amount of CPU utilization.

## Senario

The test requires the application to calculate the 10th, 20th, and 30th
Fibonacci numbers using a recursive algorythm.

The time it took to calculate these numbers was stored as the metric. This
defines one test. For the aditional datapoint, I also included a C
implementation in this test as a baseline.

## Results

The results where quite amazing to me. Not only did NodeJs out perform Python,
NodeJs crushed Python in a CPU bound process with zero blocking IO.  The margin
between NodeJs and Python is nearly as much as the margin between C and Python.

_Note: The graph is using a logarythmic scale for visability._

<iframe width="100%" height="400" frameborder="0" scrolling="no"
src="https://plot.ly/~en0/5.embed?share_key=yvaSgmkjsTQn8ESHmzEie4"></iframe>

__Python Averaged Elapsed Time: 2.78023791313 Seconds__

__NodeJs Averaged Elapsed Time: 0.012099999999999998 Seconds__

__C Average Elapsed Time: 0.0064275 Seconds__

---

# Conclution

NodeJs has already proven itself as a viable langauge for serious programing
jobs. The community doesn't need me for that. It has been gaining popularity
for some time now. But these tests opened my eyes to the posabilities available
using this language and I look forward to learning more about.

There are many more datapoints to investigate but given my recent experience,
NodeJs will be another good candidate for consideration in future projects.

On a side note, I am disapointed in Python's performance in at least 2 of these
cases. I feel that it should have preformed better. I know that I could speed
up the CPU bound tasks by using more memory efficient algorythms: Python is a
memory hog. 

Thanks for reading!

# Disclamer

I am not a seasoned NodeJs Developer. I am sure these implementations will make
many NodeJs developers cry. But I am a seasoned Python developer and these
Python implementations make me cry. We can frown at the code together, and feel
free to offer more accurate ways to calculate these metrics.

That said, I did not try to write good code here. Just effective enough code to
gather the datapoints.  If you feel the code is negativly impacting the test,
please let me know and i will update it.  Realisticly, both the Python and
NodeJs code are equaly terrable. Deal with it.

Also, keep in mind these stats really on calculate human waiting time and do
not include other extreamly important metrics such as memory utilization. 

[Test Souce Code](http://github.com/en0/python-vs-nodejs)
