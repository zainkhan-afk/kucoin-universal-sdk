// Code generated by Kucoin Universal SDK Generator; DO NOT EDIT.

package deposit

import (
	"context"
	"github.com/Kucoin/kucoin-universal-sdk/sdk/golang/internal/interfaces"
)

type DepositAPI interface {

	// AddDepositAddressV3 Add Deposit Address(V3)
	// Description: Request via this endpoint to create a deposit address for a currency you intend to deposit.
	// Documentation: https://www.kucoin.com/docs-new/api-3470142
	// +---------------------+------------+
	// | Extra API Info      | Value      |
	// +---------------------+------------+
	// | API-DOMAIN          | SPOT       |
	// | API-CHANNEL         | PRIVATE    |
	// | API-PERMISSION      | GENERAL    |
	// | API-RATE-LIMIT-POOL | MANAGEMENT |
	// | API-RATE-LIMIT      | 20         |
	// +---------------------+------------+
	AddDepositAddressV3(req *AddDepositAddressV3Req, ctx context.Context) (*AddDepositAddressV3Resp, error)

	// GetDepositAddressV3 Get Deposit Address(V3)
	// Description: Get all deposit addresses for the currency you intend to deposit. If the returned data is empty, you may need to Add Deposit Address first.
	// Documentation: https://www.kucoin.com/docs-new/api-3470140
	// +---------------------+------------+
	// | Extra API Info      | Value      |
	// +---------------------+------------+
	// | API-DOMAIN          | SPOT       |
	// | API-CHANNEL         | PRIVATE    |
	// | API-PERMISSION      | GENERAL    |
	// | API-RATE-LIMIT-POOL | MANAGEMENT |
	// | API-RATE-LIMIT      | 5          |
	// +---------------------+------------+
	GetDepositAddressV3(req *GetDepositAddressV3Req, ctx context.Context) (*GetDepositAddressV3Resp, error)

	// GetDepositHistory Get Deposit History
	// Description: Request via this endpoint to get deposit list Items are paginated and sorted to show the latest first. See the Pagination section for retrieving additional entries after the first page.
	// Documentation: https://www.kucoin.com/docs-new/api-3470141
	// +---------------------+------------+
	// | Extra API Info      | Value      |
	// +---------------------+------------+
	// | API-DOMAIN          | SPOT       |
	// | API-CHANNEL         | PRIVATE    |
	// | API-PERMISSION      | GENERAL    |
	// | API-RATE-LIMIT-POOL | MANAGEMENT |
	// | API-RATE-LIMIT      | 5          |
	// +---------------------+------------+
	GetDepositHistory(req *GetDepositHistoryReq, ctx context.Context) (*GetDepositHistoryResp, error)

	// GetDepositAddressV2 Get Deposit Addresses(V2)
	// Description: Get all deposit addresses for the currency you intend to deposit. If the returned data is empty, you may need to Add Deposit Address first.
	// Documentation: https://www.kucoin.com/docs-new/api-3470300
	// +---------------------+------------+
	// | Extra API Info      | Value      |
	// +---------------------+------------+
	// | API-DOMAIN          | SPOT       |
	// | API-CHANNEL         | PRIVATE    |
	// | API-PERMISSION      | GENERAL    |
	// | API-RATE-LIMIT-POOL | MANAGEMENT |
	// | API-RATE-LIMIT      | 5          |
	// +---------------------+------------+
	// Deprecated
	GetDepositAddressV2(req *GetDepositAddressV2Req, ctx context.Context) (*GetDepositAddressV2Resp, error)

	// GetDepositAddressV1 Get Deposit Addresses - V1
	// Description: Get all deposit addresses for the currency you intend to deposit. If the returned data is empty, you may need to Add Deposit Address first.
	// Documentation: https://www.kucoin.com/docs-new/api-3470305
	// +---------------------+------------+
	// | Extra API Info      | Value      |
	// +---------------------+------------+
	// | API-DOMAIN          | SPOT       |
	// | API-CHANNEL         | PRIVATE    |
	// | API-PERMISSION      | GENERAL    |
	// | API-RATE-LIMIT-POOL | MANAGEMENT |
	// | API-RATE-LIMIT      | 5          |
	// +---------------------+------------+
	// Deprecated
	GetDepositAddressV1(req *GetDepositAddressV1Req, ctx context.Context) (*GetDepositAddressV1Resp, error)

	// GetDepositHistoryOld Get Deposit History - Old
	// Description: Request via this endpoint to get the V1 historical deposits list on KuCoin. The return value is the data after Pagination, sorted in descending order according to time.
	// Documentation: https://www.kucoin.com/docs-new/api-3470306
	// +---------------------+------------+
	// | Extra API Info      | Value      |
	// +---------------------+------------+
	// | API-DOMAIN          | SPOT       |
	// | API-CHANNEL         | PRIVATE    |
	// | API-PERMISSION      | GENERAL    |
	// | API-RATE-LIMIT-POOL | MANAGEMENT |
	// | API-RATE-LIMIT      | 5          |
	// +---------------------+------------+
	// Deprecated
	GetDepositHistoryOld(req *GetDepositHistoryOldReq, ctx context.Context) (*GetDepositHistoryOldResp, error)

	// AddDepositAddressV1 Add Deposit Address - V1
	// Description: Request via this endpoint to create a deposit address for a currency you intend to deposit.
	// Documentation: https://www.kucoin.com/docs-new/api-3470309
	// +---------------------+------------+
	// | Extra API Info      | Value      |
	// +---------------------+------------+
	// | API-DOMAIN          | SPOT       |
	// | API-CHANNEL         | PRIVATE    |
	// | API-PERMISSION      | GENERAL    |
	// | API-RATE-LIMIT-POOL | MANAGEMENT |
	// | API-RATE-LIMIT      | 20         |
	// +---------------------+------------+
	// Deprecated
	AddDepositAddressV1(req *AddDepositAddressV1Req, ctx context.Context) (*AddDepositAddressV1Resp, error)
}

type DepositAPIImpl struct {
	transport interfaces.Transport
}

func NewDepositAPIImp(transport interfaces.Transport) *DepositAPIImpl {
	return &DepositAPIImpl{transport: transport}
}

func (impl *DepositAPIImpl) AddDepositAddressV3(req *AddDepositAddressV3Req, ctx context.Context) (*AddDepositAddressV3Resp, error) {
	resp := &AddDepositAddressV3Resp{}
	err := impl.transport.Call(ctx, "spot", false, "Post", "/api/v3/deposit-address/create", req, resp, false)
	return resp, err
}

func (impl *DepositAPIImpl) GetDepositAddressV3(req *GetDepositAddressV3Req, ctx context.Context) (*GetDepositAddressV3Resp, error) {
	resp := &GetDepositAddressV3Resp{}
	err := impl.transport.Call(ctx, "spot", false, "Get", "/api/v3/deposit-addresses", req, resp, false)
	return resp, err
}

func (impl *DepositAPIImpl) GetDepositHistory(req *GetDepositHistoryReq, ctx context.Context) (*GetDepositHistoryResp, error) {
	resp := &GetDepositHistoryResp{}
	err := impl.transport.Call(ctx, "spot", false, "Get", "/api/v1/deposits", req, resp, false)
	return resp, err
}

func (impl *DepositAPIImpl) GetDepositAddressV2(req *GetDepositAddressV2Req, ctx context.Context) (*GetDepositAddressV2Resp, error) {
	resp := &GetDepositAddressV2Resp{}
	err := impl.transport.Call(ctx, "spot", false, "Get", "/api/v2/deposit-addresses", req, resp, false)
	return resp, err
}

func (impl *DepositAPIImpl) GetDepositAddressV1(req *GetDepositAddressV1Req, ctx context.Context) (*GetDepositAddressV1Resp, error) {
	resp := &GetDepositAddressV1Resp{}
	err := impl.transport.Call(ctx, "spot", false, "Get", "/api/v1/deposit-addresses", req, resp, false)
	return resp, err
}

func (impl *DepositAPIImpl) GetDepositHistoryOld(req *GetDepositHistoryOldReq, ctx context.Context) (*GetDepositHistoryOldResp, error) {
	resp := &GetDepositHistoryOldResp{}
	err := impl.transport.Call(ctx, "spot", false, "Get", "/api/v1/hist-deposits", req, resp, false)
	return resp, err
}

func (impl *DepositAPIImpl) AddDepositAddressV1(req *AddDepositAddressV1Req, ctx context.Context) (*AddDepositAddressV1Resp, error) {
	resp := &AddDepositAddressV1Resp{}
	err := impl.transport.Call(ctx, "spot", false, "Post", "/api/v1/deposit-addresses", req, resp, false)
	return resp, err
}
