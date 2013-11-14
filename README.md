sendhub-programming-challenge
=============================
Hosted on heroku:  
http://sendhubapi.herokuapp.com/

<pre>curl -X POST -H "Content-Type: application/json" -d '{"message": "SendHub Rocks", "recipients": ["412-427-8881", "412-427-8882", "412-427-8883", ""412-427-8884", "412-427-8885", "412-427-8886"]}' http://sendhubapi.herokuapp.com/api/sendhub/v1.0/routes</pre>

For now, the valid format of usa phone number is 412-427-8881

<hr>
Future improvement:
* Write more complicated regular expression to support more phone number format. For example, (412) 427-8881.    
