# Description

This project is based on the Fullcycle modules
- "Arquitetura baseada em microsserviços"
- "EDA - Event Driven Architecture"

# Development

Run tests
```
go test ./...
```

Running docker container:
```
docker compose up -d
```

Connecting to mysql:
```
docker exec -it fullcycle_wallet_core-mysql-1 bash
mysql -u root -proot wallet
```

Running app:
```
go run cmd/walletcore/main.go
```

Http requests:
Check the file: api/client.http