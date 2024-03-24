# Description

This project is based on the Fullcycle modules
- "Arquitetura baseada em microsserviços"
- "EDA - Event Driven Architecture"


# Application

Running docker container:
```
docker compose up -d
```


Golang application:
http://localhost:3000/

Python application:
http://localhost:3003/


Kafka:
http://localhost:9021/

Connecting to mysql:
```
docker exec -it fullcycle_wallet_core-mysql-1 bash
mysql -u root -proot wallet
```

Running tests:
```
docker exec -it goapp bash
o test ./...
```

Http requests:
Check the file: api/client.http