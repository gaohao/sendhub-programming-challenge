sendhub-programming-challenge
=============================
Hosted on heroku:  
http://sendhubapi.herokuapp.com/

* greedy approach to calaculate the routes
<pre>curl -X POST -H "Content-Type: application/json" -d '{"message": "SendHub Rocks", "recipients": ["412-427-8881", "412-427-8882", "412-427-8883", "412-427-8884", "412-427-8885", "412-427-8886"]}' http://sendhubapi.herokuapp.com/v1.0/greedy_routes</pre>

* dynamic programming approach to calaculate the routes
<pre>curl -X POST -H "Content-Type: application/json" -d '{"message": "SendHub Rocks", "recipients": ["412-427-8881", "412-427-8882", "412-427-8883", "412-427-8884", "412-427-8885", "412-427-8886"]}' http://sendhubapi.herokuapp.com/v1.0/dynamic_routes</pre>

This problem is actually a claasic change-making problem. In our use case, a set of {1, 5, 10, 25}, the problem is easily solved by a greedy algorithm. The time complexity is 4 * n, n is the number of recipient.

Further thoughts:
From the wikipedia, "If the number of coin denominations is three or more, no explicit formula is known; but, for any fixed number of coin denominations, there is an algorithm computing the Frobenius number in polynomial time (in the logarithms of the coin denominations forming an input). No known algorithm is polynomial time in the number of coin denominations, and the general problem, where the number of coin denominations may be as large as desired, is NP-hard"

So if we know the total number of the categories, we can solve the problem in polynomial time by using dynamic programming.

Reference:  
http://en.wikipedia.org/wiki/Change-making_problem  
http://en.wikipedia.org/wiki/Coin_problem   

<hr>
Future improvement:
* Write more complicated regular expression to support more phone number format. For example, (412) 427-8881. For now, the valid format of usa phone number is 412-427-8881   
