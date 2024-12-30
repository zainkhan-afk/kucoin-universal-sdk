// Code generated by Kucoin Universal SDK Generator; DO NOT EDIT.

package order

// GetTradeHistoryItems struct for GetTradeHistoryItems
type GetTradeHistoryItems struct {
	// Symbol of the contract, Please refer to [Get Symbol endpoint: symbol](https://www.kucoin.com/docs-new/api-3470220)
	Symbol string `json:"symbol,omitempty"`
	// Trade ID
	TradeId string `json:"tradeId,omitempty"`
	// Order ID
	OrderId string `json:"orderId,omitempty"`
	// Transaction side
	Side string `json:"side,omitempty"`
	// Liquidity- taker or maker
	Liquidity string `json:"liquidity,omitempty"`
	// Whether to force processing as a taker
	ForceTaker bool `json:"forceTaker,omitempty"`
	// Filled price
	Price string `json:"price,omitempty"`
	// Filled amount
	Size int32 `json:"size,omitempty"`
	// Order value
	Value string `json:"value,omitempty"`
	// Opening transaction fee
	OpenFeePay string `json:"openFeePay,omitempty"`
	// Closing transaction fee
	CloseFeePay string `json:"closeFeePay,omitempty"`
	// A mark to the stop order type
	Stop string `json:"stop,omitempty"`
	// Fee Rate
	FeeRate string `json:"feeRate,omitempty"`
	// Fixed fees(Deprecated field, no actual use of the value field)
	FixFee string `json:"fixFee,omitempty"`
	// Charging currency
	FeeCurrency string `json:"feeCurrency,omitempty"`
	// trade time in nanosecond
	TradeTime int64 `json:"tradeTime,omitempty"`
	// Deprecated field, no actual use of the value field
	SubTradeType string `json:"subTradeType,omitempty"`
	// Margin mode: ISOLATED (isolated), CROSS (cross margin).
	MarginMode string `json:"marginMode,omitempty"`
	// Settle Currency
	SettleCurrency string `json:"settleCurrency,omitempty"`
	// Order Type
	DisplayType string `json:"displayType,omitempty"`
	Fee         string `json:"fee,omitempty"`
	// Order type
	OrderType string `json:"orderType,omitempty"`
	// Trade type (trade, liquid, adl or settlement)
	TradeType string `json:"tradeType,omitempty"`
	// Time the order created
	CreatedAt int64 `json:"createdAt,omitempty"`
}

// NewGetTradeHistoryItems instantiates a new GetTradeHistoryItems object
// This constructor will assign default values to properties that have it defined
func NewGetTradeHistoryItems(symbol string, tradeId string, orderId string, side string, liquidity string, forceTaker bool, price string, size int32, value string, openFeePay string, closeFeePay string, stop string, feeRate string, fixFee string, feeCurrency string, tradeTime int64, subTradeType string, marginMode string, settleCurrency string, displayType string, fee string, orderType string, tradeType string, createdAt int64) *GetTradeHistoryItems {
	this := GetTradeHistoryItems{}
	this.Symbol = symbol
	this.TradeId = tradeId
	this.OrderId = orderId
	this.Side = side
	this.Liquidity = liquidity
	this.ForceTaker = forceTaker
	this.Price = price
	this.Size = size
	this.Value = value
	this.OpenFeePay = openFeePay
	this.CloseFeePay = closeFeePay
	this.Stop = stop
	this.FeeRate = feeRate
	this.FixFee = fixFee
	this.FeeCurrency = feeCurrency
	this.TradeTime = tradeTime
	this.SubTradeType = subTradeType
	this.MarginMode = marginMode
	this.SettleCurrency = settleCurrency
	this.DisplayType = displayType
	this.Fee = fee
	this.OrderType = orderType
	this.TradeType = tradeType
	this.CreatedAt = createdAt
	return &this
}

// NewGetTradeHistoryItemsWithDefaults instantiates a new GetTradeHistoryItems object
// This constructor will only assign default values to properties that have it defined,
func NewGetTradeHistoryItemsWithDefaults() *GetTradeHistoryItems {
	this := GetTradeHistoryItems{}
	return &this
}

func (o *GetTradeHistoryItems) ToMap() map[string]interface{} {
	toSerialize := map[string]interface{}{}
	toSerialize["symbol"] = o.Symbol
	toSerialize["tradeId"] = o.TradeId
	toSerialize["orderId"] = o.OrderId
	toSerialize["side"] = o.Side
	toSerialize["liquidity"] = o.Liquidity
	toSerialize["forceTaker"] = o.ForceTaker
	toSerialize["price"] = o.Price
	toSerialize["size"] = o.Size
	toSerialize["value"] = o.Value
	toSerialize["openFeePay"] = o.OpenFeePay
	toSerialize["closeFeePay"] = o.CloseFeePay
	toSerialize["stop"] = o.Stop
	toSerialize["feeRate"] = o.FeeRate
	toSerialize["fixFee"] = o.FixFee
	toSerialize["feeCurrency"] = o.FeeCurrency
	toSerialize["tradeTime"] = o.TradeTime
	toSerialize["subTradeType"] = o.SubTradeType
	toSerialize["marginMode"] = o.MarginMode
	toSerialize["settleCurrency"] = o.SettleCurrency
	toSerialize["displayType"] = o.DisplayType
	toSerialize["fee"] = o.Fee
	toSerialize["orderType"] = o.OrderType
	toSerialize["tradeType"] = o.TradeType
	toSerialize["createdAt"] = o.CreatedAt
	return toSerialize
}
