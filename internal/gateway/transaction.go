package gateway

import "github.com/killertiger/fullcycle_wallet_core/internal/entity"

type TransactionGateway interface {
	Create(transaction *entity.Transaction) error
}
