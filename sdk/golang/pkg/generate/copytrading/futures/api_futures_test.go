package futures

import (
	"encoding/json"
	"github.com/Kucoin/kucoin-universal-sdk/sdk/golang/pkg/types"
	"github.com/stretchr/testify/assert"
	"testing"
)

func TestFuturesAddOrderReqModel(t *testing.T) {
	// AddOrder
	// Add Order
	// /api/v1/copy-trade/futures/orders

	data := "{\"clientOid\": \"5c52e11203aa677f33e493fb\", \"side\": \"buy\", \"symbol\": \"XBTUSDTM\", \"leverage\": 3, \"type\": \"limit\", \"remark\": \"order remarks\", \"reduceOnly\": false, \"marginMode\": \"ISOLATED\", \"price\": \"0.1\", \"size\": 1, \"timeInForce\": \"GTC\"}"
	req := &AddOrderReq{}
	err := json.Unmarshal([]byte(data), req)
	req.ToMap()
	assert.Nil(t, err)
}

func TestFuturesAddOrderRespModel(t *testing.T) {
	// AddOrder
	// Add Order
	// /api/v1/copy-trade/futures/orders

	data := "{\n    \"code\": \"200000\",\n    \"data\": {\n        \"orderId\": \"263485113055133696\",\n        \"clientOid\": \"5c52e11203aa677f331e493fb\"\n    }\n}"
	commonResp := &types.RestResponse{}
	err := json.Unmarshal([]byte(data), commonResp)
	assert.Nil(t, err)
	assert.NotNil(t, commonResp.Data)
	resp := &AddOrderResp{}
	err = json.Unmarshal([]byte(commonResp.Data), resp)
	resp.ToMap()
	assert.Nil(t, err)
}

func TestFuturesAddOrderTestReqModel(t *testing.T) {
	// AddOrderTest
	// Add Order Test
	// /api/v1/copy-trade/futures/orders/test

	data := "{\"clientOid\": \"5c52e11203aa677f33e493fb\", \"side\": \"buy\", \"symbol\": \"XBTUSDTM\", \"leverage\": 3, \"type\": \"limit\", \"remark\": \"order remarks\", \"reduceOnly\": false, \"marginMode\": \"ISOLATED\", \"price\": \"0.1\", \"size\": 1, \"timeInForce\": \"GTC\"}"
	req := &AddOrderTestReq{}
	err := json.Unmarshal([]byte(data), req)
	req.ToMap()
	assert.Nil(t, err)
}

func TestFuturesAddOrderTestRespModel(t *testing.T) {
	// AddOrderTest
	// Add Order Test
	// /api/v1/copy-trade/futures/orders/test

	data := "{\n    \"code\": \"200000\",\n    \"data\": {\n        \"orderId\": \"234125150956625920\",\n        \"clientOid\": \"5c52e11203aa677f33e493fb\"\n    }\n}"
	commonResp := &types.RestResponse{}
	err := json.Unmarshal([]byte(data), commonResp)
	assert.Nil(t, err)
	assert.NotNil(t, commonResp.Data)
	resp := &AddOrderTestResp{}
	err = json.Unmarshal([]byte(commonResp.Data), resp)
	resp.ToMap()
	assert.Nil(t, err)
}

func TestFuturesAddTPSLOrderReqModel(t *testing.T) {
	// AddTPSLOrder
	// Add Take Profit And Stop Loss Order
	// /api/v1/copy-trade/futures/st-orders

	data := "{\"clientOid\": \"5c52e11203aa677f33e493fb\", \"side\": \"buy\", \"symbol\": \"XBTUSDTM\", \"leverage\": 3, \"type\": \"limit\", \"remark\": \"order remarks\", \"reduceOnly\": false, \"marginMode\": \"ISOLATED\", \"price\": \"0.2\", \"size\": 1, \"timeInForce\": \"GTC\", \"triggerStopUpPrice\": \"0.3\", \"triggerStopDownPrice\": \"0.1\", \"stopPriceType\": \"TP\"}"
	req := &AddTPSLOrderReq{}
	err := json.Unmarshal([]byte(data), req)
	req.ToMap()
	assert.Nil(t, err)
}

func TestFuturesAddTPSLOrderRespModel(t *testing.T) {
	// AddTPSLOrder
	// Add Take Profit And Stop Loss Order
	// /api/v1/copy-trade/futures/st-orders

	data := "{\n    \"code\": \"200000\",\n    \"data\": {\n        \"orderId\": \"234125150956625920\",\n        \"clientOid\": \"5c52e11203aa677f33e493fb\"\n    }\n}"
	commonResp := &types.RestResponse{}
	err := json.Unmarshal([]byte(data), commonResp)
	assert.Nil(t, err)
	assert.NotNil(t, commonResp.Data)
	resp := &AddTPSLOrderResp{}
	err = json.Unmarshal([]byte(commonResp.Data), resp)
	resp.ToMap()
	assert.Nil(t, err)
}

func TestFuturesCancelOrderByIdReqModel(t *testing.T) {
	// CancelOrderById
	// Cancel Order By OrderId
	// /api/v1/copy-trade/futures/orders

	data := "{\"orderId\": \"263485113055133696\"}"
	req := &CancelOrderByIdReq{}
	err := json.Unmarshal([]byte(data), req)
	req.ToMap()
	assert.Nil(t, err)
}

func TestFuturesCancelOrderByIdRespModel(t *testing.T) {
	// CancelOrderById
	// Cancel Order By OrderId
	// /api/v1/copy-trade/futures/orders

	data := "{\n    \"code\": \"200000\",\n    \"data\": {\n        \"cancelledOrderIds\": [\n            \"263485113055133696\"\n        ]\n    }\n}"
	commonResp := &types.RestResponse{}
	err := json.Unmarshal([]byte(data), commonResp)
	assert.Nil(t, err)
	assert.NotNil(t, commonResp.Data)
	resp := &CancelOrderByIdResp{}
	err = json.Unmarshal([]byte(commonResp.Data), resp)
	resp.ToMap()
	assert.Nil(t, err)
}

func TestFuturesCancelOrderByClientOidReqModel(t *testing.T) {
	// CancelOrderByClientOid
	// Cancel Order By ClientOid
	// /api/v1/copy-trade/futures/orders/client-order

	data := "{\"symbol\": \"XBTUSDTM\", \"clientOid\": \"5c52e11203aa677f331e493fb\"}"
	req := &CancelOrderByClientOidReq{}
	err := json.Unmarshal([]byte(data), req)
	req.ToMap()
	assert.Nil(t, err)
}

func TestFuturesCancelOrderByClientOidRespModel(t *testing.T) {
	// CancelOrderByClientOid
	// Cancel Order By ClientOid
	// /api/v1/copy-trade/futures/orders/client-order

	data := "{\n    \"code\": \"200000\",\n    \"data\": {\n        \"clientOid\": \"5c52e11203aa677f331e4913fb\"\n    }\n}"
	commonResp := &types.RestResponse{}
	err := json.Unmarshal([]byte(data), commonResp)
	assert.Nil(t, err)
	assert.NotNil(t, commonResp.Data)
	resp := &CancelOrderByClientOidResp{}
	err = json.Unmarshal([]byte(commonResp.Data), resp)
	resp.ToMap()
	assert.Nil(t, err)
}

func TestFuturesGetMaxOpenSizeReqModel(t *testing.T) {
	// GetMaxOpenSize
	// Get Max Open Size
	// /api/v1/copy-trade/futures/get-max-open-size

	data := "{\"symbol\": \"XBTUSDTM\", \"price\": \"example_string_default_value\", \"leverage\": 123456}"
	req := &GetMaxOpenSizeReq{}
	err := json.Unmarshal([]byte(data), req)
	req.ToMap()
	assert.Nil(t, err)
}

func TestFuturesGetMaxOpenSizeRespModel(t *testing.T) {
	// GetMaxOpenSize
	// Get Max Open Size
	// /api/v1/copy-trade/futures/get-max-open-size

	data := "{\n    \"code\": \"200000\",\n    \"data\": {\n        \"symbol\": \"XBTUSDTM\",\n        \"maxBuyOpenSize\": 8,\n        \"maxSellOpenSize\": 5\n    }\n}"
	commonResp := &types.RestResponse{}
	err := json.Unmarshal([]byte(data), commonResp)
	assert.Nil(t, err)
	assert.NotNil(t, commonResp.Data)
	resp := &GetMaxOpenSizeResp{}
	err = json.Unmarshal([]byte(commonResp.Data), resp)
	resp.ToMap()
	assert.Nil(t, err)
}

func TestFuturesGetMaxWithdrawMarginReqModel(t *testing.T) {
	// GetMaxWithdrawMargin
	// Get Max Withdraw Margin
	// /api/v1/copy-trade/futures/position/margin/max-withdraw-margin

	data := "{\"symbol\": \"example_string_default_value\"}"
	req := &GetMaxWithdrawMarginReq{}
	err := json.Unmarshal([]byte(data), req)
	req.ToMap()
	assert.Nil(t, err)
}

func TestFuturesGetMaxWithdrawMarginRespModel(t *testing.T) {
	// GetMaxWithdrawMargin
	// Get Max Withdraw Margin
	// /api/v1/copy-trade/futures/position/margin/max-withdraw-margin

	data := "{\n    \"code\": \"200000\",\n    \"data\": \"21.1135719252\"\n}"
	commonResp := &types.RestResponse{}
	err := json.Unmarshal([]byte(data), commonResp)
	assert.Nil(t, err)
	assert.NotNil(t, commonResp.Data)
	resp := &GetMaxWithdrawMarginResp{}
	err = json.Unmarshal([]byte(commonResp.Data), resp)
	resp.ToMap()
	assert.Nil(t, err)
}

func TestFuturesAddIsolatedMarginReqModel(t *testing.T) {
	// AddIsolatedMargin
	// Add Isolated Margin
	// /api/v1/copy-trade/futures/position/margin/deposit-margin

	data := "{\"symbol\": \"string\", \"margin\": 0, \"bizNo\": \"string\"}"
	req := &AddIsolatedMarginReq{}
	err := json.Unmarshal([]byte(data), req)
	req.ToMap()
	assert.Nil(t, err)
}

func TestFuturesAddIsolatedMarginRespModel(t *testing.T) {
	// AddIsolatedMargin
	// Add Isolated Margin
	// /api/v1/copy-trade/futures/position/margin/deposit-margin

	data := "{\n    \"code\": \"200000\",\n    \"data\": {\n        \"id\": \"6200c9b83aecfb000152ddcd\",\n        \"symbol\": \"XBTUSDTM\",\n        \"autoDeposit\": false,\n        \"maintMarginReq\": 0.005,\n        \"riskLimit\": 500000,\n        \"realLeverage\": 18.72,\n        \"crossMode\": false,\n        \"delevPercentage\": 0.66,\n        \"openingTimestamp\": 1646287090131,\n        \"currentTimestamp\": 1646295055021,\n        \"currentQty\": 1,\n        \"currentCost\": 43.388,\n        \"currentComm\": 0.0260328,\n        \"unrealisedCost\": 43.388,\n        \"realisedGrossCost\": 0,\n        \"realisedCost\": 0.0260328,\n        \"isOpen\": true,\n        \"markPrice\": 43536.65,\n        \"markValue\": 43.53665,\n        \"posCost\": 43.388,\n        \"posCross\": 0.000024985,\n        \"posInit\": 2.1694,\n        \"posComm\": 0.02733446,\n        \"posLoss\": 0,\n        \"posMargin\": 2.19675944,\n        \"posMaint\": 0.24861326,\n        \"maintMargin\": 2.34540944,\n        \"realisedGrossPnl\": 0,\n        \"realisedPnl\": -0.0260328,\n        \"unrealisedPnl\": 0.14865,\n        \"unrealisedPnlPcnt\": 0.0034,\n        \"unrealisedRoePcnt\": 0.0685,\n        \"avgEntryPrice\": 43388,\n        \"liquidationPrice\": 41440,\n        \"bankruptPrice\": 41218,\n        \"userId\": 1234321123,\n        \"settleCurrency\": \"USDT\"\n    }\n}"
	commonResp := &types.RestResponse{}
	err := json.Unmarshal([]byte(data), commonResp)
	assert.Nil(t, err)
	assert.NotNil(t, commonResp.Data)
	resp := &AddIsolatedMarginResp{}
	err = json.Unmarshal([]byte(commonResp.Data), resp)
	resp.ToMap()
	assert.Nil(t, err)
}

func TestFuturesRemoveIsolatedMarginReqModel(t *testing.T) {
	// RemoveIsolatedMargin
	// Remove Isolated Margin
	// /api/v1/copy-trade/futures/position/margin/withdraw-margin

	data := "{\"symbol\": \"XBTUSDTM\", \"withdrawAmount\": \"0.0000001\"}"
	req := &RemoveIsolatedMarginReq{}
	err := json.Unmarshal([]byte(data), req)
	req.ToMap()
	assert.Nil(t, err)
}

func TestFuturesRemoveIsolatedMarginRespModel(t *testing.T) {
	// RemoveIsolatedMargin
	// Remove Isolated Margin
	// /api/v1/copy-trade/futures/position/margin/withdraw-margin

	data := "{\n    \"code\": \"200000\",\n    \"data\": \"0.1\"\n}"
	commonResp := &types.RestResponse{}
	err := json.Unmarshal([]byte(data), commonResp)
	assert.Nil(t, err)
	assert.NotNil(t, commonResp.Data)
	resp := &RemoveIsolatedMarginResp{}
	err = json.Unmarshal([]byte(commonResp.Data), resp)
	resp.ToMap()
	assert.Nil(t, err)
}

func TestFuturesModifyIsolatedMarginRiskLimtReqModel(t *testing.T) {
	// ModifyIsolatedMarginRiskLimt
	// Modify Isolated Margin Risk Limit
	// /api/v1/copy-trade/futures/position/risk-limit-level/change

	data := "{\"symbol\": \"XBTUSDTM\", \"level\": 1}"
	req := &ModifyIsolatedMarginRiskLimtReq{}
	err := json.Unmarshal([]byte(data), req)
	req.ToMap()
	assert.Nil(t, err)
}

func TestFuturesModifyIsolatedMarginRiskLimtRespModel(t *testing.T) {
	// ModifyIsolatedMarginRiskLimt
	// Modify Isolated Margin Risk Limit
	// /api/v1/copy-trade/futures/position/risk-limit-level/change

	data := "{\n    \"code\": \"200000\",\n    \"data\": true\n}"
	commonResp := &types.RestResponse{}
	err := json.Unmarshal([]byte(data), commonResp)
	assert.Nil(t, err)
	assert.NotNil(t, commonResp.Data)
	resp := &ModifyIsolatedMarginRiskLimtResp{}
	err = json.Unmarshal([]byte(commonResp.Data), resp)
	resp.ToMap()
	assert.Nil(t, err)
}

func TestFuturesModifyAutoDepositStatusReqModel(t *testing.T) {
	// ModifyAutoDepositStatus
	// Modify Isolated Margin Auto-Deposit Status
	// /api/v1/copy-trade/futures/position/margin/auto-deposit-status

	data := "{\"symbol\": \"XBTUSDTM\", \"status\": true}"
	req := &ModifyAutoDepositStatusReq{}
	err := json.Unmarshal([]byte(data), req)
	req.ToMap()
	assert.Nil(t, err)
}

func TestFuturesModifyAutoDepositStatusRespModel(t *testing.T) {
	// ModifyAutoDepositStatus
	// Modify Isolated Margin Auto-Deposit Status
	// /api/v1/copy-trade/futures/position/margin/auto-deposit-status

	data := "{\n    \"code\": \"200000\",\n    \"data\": true\n}"
	commonResp := &types.RestResponse{}
	err := json.Unmarshal([]byte(data), commonResp)
	assert.Nil(t, err)
	assert.NotNil(t, commonResp.Data)
	resp := &ModifyAutoDepositStatusResp{}
	err = json.Unmarshal([]byte(commonResp.Data), resp)
	resp.ToMap()
	assert.Nil(t, err)
}
