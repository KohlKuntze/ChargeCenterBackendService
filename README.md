# ChargeCenterBackendService

# Sample Request to Test:

## Local:
```
curl -X POST -H "Content-type: application/json" -d "{\"firstName\" : \"John\", \"lastName\" : \"Smith\"}" "localhost:5000/post_json"
```

## Server:
```
curl -X POST -H "Content-type: application/json" -d "{\"firstName\" : \"John\", \"lastName\" : \"Smith\"}" "http://charge-center-backend-service.eba-c2vgh8y3.us-east-1.elasticbeanstalk.com/post_json"
```