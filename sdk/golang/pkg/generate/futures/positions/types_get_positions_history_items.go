// Code generated by Kucoin Universal SDK Generator; DO NOT EDIT.

package positions

// GetPositionsHistoryItems struct for GetPositionsHistoryItems
type GetPositionsHistoryItems struct {
	// Close ID
	CloseId string `json:"closeId,omitempty"`
	// User ID
	UserId string `json:"userId,omitempty"`
	// Symbol of the contract, Please refer to [Get Symbol endpoint: symbol](https://www.kucoin.com/docs-new/api-3470220)
	Symbol string `json:"symbol,omitempty"`
	// Currency used to settle trades
	SettleCurrency string `json:"settleCurrency,omitempty"`
	// Leverage applied to the order
	Leverage string `json:"leverage,omitempty"`
	// Type of closure
	Type string `json:"type,omitempty"`
	// Net profit and loss (after deducting fees and funding costs)
	Pnl string `json:"pnl,omitempty"`
	// Accumulated realised gross profit value
	RealisedGrossCost string `json:"realisedGrossCost,omitempty"`
	// Accumulated realised profit withdrawn from the position
	WithdrawPnl string `json:"withdrawPnl,omitempty"`
	// Accumulated trading fees
	TradeFee string `json:"tradeFee,omitempty"`
	// Accumulated funding fees
	FundingFee string `json:"fundingFee,omitempty"`
	// Time when the position was opened
	OpenTime int64 `json:"openTime,omitempty"`
	// Time when the position was closed (default sorted in descending order)
	CloseTime int64 `json:"closeTime,omitempty"`
	// Opening price of the position
	OpenPrice string `json:"openPrice,omitempty"`
	// Closing price of the position
	ClosePrice string `json:"closePrice,omitempty"`
	// Margin Mode: CROSS，ISOLATED
	MarginMode string `json:"marginMode,omitempty"`
}

// NewGetPositionsHistoryItems instantiates a new GetPositionsHistoryItems object
// This constructor will assign default values to properties that have it defined
func NewGetPositionsHistoryItems(closeId string, userId string, symbol string, settleCurrency string, leverage string, Type_ string, pnl string, realisedGrossCost string, withdrawPnl string, tradeFee string, fundingFee string, openTime int64, closeTime int64, openPrice string, closePrice string, marginMode string) *GetPositionsHistoryItems {
	this := GetPositionsHistoryItems{}
	this.CloseId = closeId
	this.UserId = userId
	this.Symbol = symbol
	this.SettleCurrency = settleCurrency
	this.Leverage = leverage
	this.Type = Type_
	this.Pnl = pnl
	this.RealisedGrossCost = realisedGrossCost
	this.WithdrawPnl = withdrawPnl
	this.TradeFee = tradeFee
	this.FundingFee = fundingFee
	this.OpenTime = openTime
	this.CloseTime = closeTime
	this.OpenPrice = openPrice
	this.ClosePrice = closePrice
	this.MarginMode = marginMode
	return &this
}

// NewGetPositionsHistoryItemsWithDefaults instantiates a new GetPositionsHistoryItems object
// This constructor will only assign default values to properties that have it defined,
func NewGetPositionsHistoryItemsWithDefaults() *GetPositionsHistoryItems {
	this := GetPositionsHistoryItems{}
	return &this
}

func (o *GetPositionsHistoryItems) ToMap() map[string]interface{} {
	toSerialize := map[string]interface{}{}
	toSerialize["closeId"] = o.CloseId
	toSerialize["userId"] = o.UserId
	toSerialize["symbol"] = o.Symbol
	toSerialize["settleCurrency"] = o.SettleCurrency
	toSerialize["leverage"] = o.Leverage
	toSerialize["type"] = o.Type
	toSerialize["pnl"] = o.Pnl
	toSerialize["realisedGrossCost"] = o.RealisedGrossCost
	toSerialize["withdrawPnl"] = o.WithdrawPnl
	toSerialize["tradeFee"] = o.TradeFee
	toSerialize["fundingFee"] = o.FundingFee
	toSerialize["openTime"] = o.OpenTime
	toSerialize["closeTime"] = o.CloseTime
	toSerialize["openPrice"] = o.OpenPrice
	toSerialize["closePrice"] = o.ClosePrice
	toSerialize["marginMode"] = o.MarginMode
	return toSerialize
}
