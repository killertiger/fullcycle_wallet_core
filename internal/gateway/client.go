package gateway

import "github.com/killertiger/fullcycle_wallet_core/internal/entity"

type ClientGateway interface {
	Get(id string) (*entity.Client, error)
	Save(client *entity.Client) error
}
