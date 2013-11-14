#!/bin/bash
# test case 1
curl -X POST -H "Content-Type: application/json" -d '{"message": "SendHub Rocks", "recipients": ["412-427-8881"]}' http://sendhubapi.herokuapp.com/api/sendhub/v1.0/routes

# test case 2
curl -X POST -H "Content-Type: application/json" -d '{"message": "SendHub Rocks", "recipients": ["412-427-8881", "412-427-8882", "412-427-8883", "412-427-8884", "412-427-8885", "412-427-8886"]}' http://sendhubapi.herokuapp.com/api/sendhub/v1.0/routes

# test case 3
curl -X POST -H "Content-Type: application/json" -d '{"message": "SendHub Rocks", "recipients": ["412-427-8881", "412-427-8882", "412-427-8883", "412-427-8884", "412-427-8885", "412-427-8886", "412-427-887"]}' http://sendhubapi.herokuapp.com/api/sendhub/v1.0/routes
