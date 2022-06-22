# ChargeCenterBackendService


# Running locally:

##### 1) Create Virtual Environment:
```
virtualenv virt
``` 

##### 2) Make Sure Flask is Installed:
```
pip install flask==2.0.3
``` 

##### 3) Create requirements.txt:
```
pip freeze > requirements.txt
``` 

##### 4) Enter Previously Created Virtual Environment:
```
source virt/bin/activate
```

##### 5) Run Server:
```
python application.py
```


# Sample Request for Test:

#### Local:
```
curl -X POST -H "Content-type: application/json" -d "{\"firstName\" : \"John\", \"lastName\" : \"Smith\"}" "localhost:5000/post_json"
```

#### Server:
```
curl -X POST -H "Content-type: application/json" -d "{\"firstName\" : \"John\", \"lastName\" : \"Smith\"}" "http://charge-center-backend-service.eba-c2vgh8y3.us-east-1.elasticbeanstalk.com/post_json"
```