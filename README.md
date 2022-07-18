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

# Pushing a change:


# Setup Dynamo:

##### 1) Create Local Dynamo Server:
* *Note: this needs to be run in the directory which has this file*
```
java -Djava.library.path=./DynamoDBLocal_lib -jar DynamoDBLocal.jar -sharedDb
```

#### 2) Make sure you're logged into AWS:
```
aws configure
```

#### 3) Create the table:
```
aws dynamodb create-table \
    --table-name ChargerAllocation \
    --attribute-definitions \
        AttributeName=ChargerId,AttributeType=S \
    --key-schema AttributeName=ChargerId,KeyType=HASH \
    --provisioned-throughput ReadCapacityUnits=1,WriteCapacityUnits=1 \
    --table-class STANDARD \
    --endpoint-url http://localhost:8000 \
    --debug
```

#### 4) Add items to the table like so:
```
 aws dynamodb put-item \
    --table-name ChargerAllocation \
    --item '{
        "ChargerId": {"S": "Charger-1"},
        "PlugIds": {"SS": ["Plug-1", "Plug-2" ,"Plug-3"]},
        "PlugAllocation": {"M": {
        	"Plug-1": {"N": "0.4"},
        	"Plug-2": {"N": "0.35"},
        	"Plug-3": {"N": "0.25"}
        }}
      }' \
    --endpoint-url http://localhost:8000 \
    --return-consumed-capacity TOTAL
```

#### How to list your dynamo tables:
```
aws dynamodb list-tables --endpoint-url http://localhost:8000
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