package main

import (
	"database/sql"
	"fmt"

	_ "github.com/go-sql-driver/mysql"
	"github.com/killertiger/fullcycle_wallet_core/internal/database"
	"github.com/killertiger/fullcycle_wallet_core/internal/event"
	"github.com/killertiger/fullcycle_wallet_core/internal/usecase/create_account"
	"github.com/killertiger/fullcycle_wallet_core/internal/usecase/create_client"
	"github.com/killertiger/fullcycle_wallet_core/internal/usecase/create_transaction"
	"github.com/killertiger/fullcycle_wallet_core/pkg/events"
)

func main() {
	// db, err := sql.Open("mysql", fmt.Sprintf("%s:%s@tcp(%s:%s)/%s?charset=utf8&parseTime=true&loc=Local", "root", "root", "localhost", "3306", "wallet"))
	db, err := sql.Open("mysql", fmt.Sprintf("%s:%s@tcp(%s:%s)/%s?&parseTime=true&loc=Local", "root", "root", "localhost", "3306", "wallet"))
	if err != nil {
		panic(err)
	}
	defer db.Close()

	eventDispatcher := events.NewEventDispatcher()
	transactionCreatedEvent := event.NewTransactionCreated()
	// eventDispatcher.Register("TransactionCreated", handler)

	clientDb := database.NewClientDB(db)
	accountDb := database.NewAccountDB(db)
	transactionDb := database.NewTransactionDB(db)

	createClientUseCase := create_client.NewCreateClientUseCase(clientDb)
	createAccountUseCase := create_account.NewCreateAccountUseCase(accountDb, clientDb)
	createTransactionUseCase := create_transaction.NewCreateTransactionUseCase(transactionDb, accountDb, eventDispatcher, transactionCreatedEvent)
}
