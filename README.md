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
curl -X GET \
    -G 'localhost:5000/information/get_charge_allocation' \
    -d 'charger_name=CHARGER_1' \
    -d 'port_info={%22port_one%22:0.9,%22port_two%22:0.1}'
```

#### Server:
```
curl -X POST -H "Content-type: application/json" -d "{\"charger_name\":\"CHARGER_1\",\"port_info\":{\"port_1\":0.3,\"port_2\":0.7}}" "http://charge-center-backend-service.eba-c2vgh8y3.us-east-1.elasticbeanstalk.com/information/get_charge_allocation"
```