// Code generated by Kucoin Universal SDK Generator; DO NOT EDIT.

package order

// AddOrderReq struct for AddOrderReq
type AddOrderReq struct {
	// Unique order id created by users to identify their orders, the maximum length cannot exceed 40, e.g. UUID, Only allows numbers, characters, underline(_), and separator(-)
	ClientOid string `json:"clientOid,omitempty"`
	// specify if the order is to 'buy' or 'sell'
	Side string `json:"side,omitempty"`
	// Symbol of the contract, Please refer to [Get Symbol endpoint: symbol](https://www.kucoin.com/docs-new/api-3470220)
	Symbol string `json:"symbol,omitempty"`
	// Used to calculate the margin to be frozen for the order. If you are to close the position, this parameter is not required.
	Leverage int32 `json:"leverage,omitempty"`
	// specify if the order is an 'limit' order or 'market' order
	Type *string `json:"type,omitempty"`
	// remark for the order, length cannot exceed 100 utf8 characters
	Remark *string `json:"remark,omitempty"`
	// Either 'down' or 'up'.  If stop is used,parameter stopPrice and stopPriceType also need to be provieded.
	Stop *string `json:"stop,omitempty"`
	// Either 'TP', 'IP' or 'MP', Need to be defined if stop is specified.
	StopPriceType *string `json:"stopPriceType,omitempty"`
	// Need to be defined if stop is specified.
	StopPrice *string `json:"stopPrice,omitempty"`
	// A mark to reduce the position size only. Set to false by default. Need to set the position size when reduceOnly is true. If set to true, only the orders reducing the position size will be executed. If the reduce-only order size exceeds the position size, the extra size will be canceled.
	ReduceOnly *bool `json:"reduceOnly,omitempty"`
	// A mark to close the position. Set to false by default. If closeOrder is set to true, the system will close the position and the position size will become 0. Side, Size and Leverage fields can be left empty and the system will determine the side and size automatically.
	CloseOrder *bool `json:"closeOrder,omitempty"`
	// A mark to forcely hold the funds for an order, even though it's an order to reduce the position size. This helps the order stay on the order book and not get canceled when the position size changes. Set to false by default. The system will forcely freeze certain amount of funds for this order, including orders whose direction is opposite to the current positions. This feature is to ensure that the order won’t be canceled by the matching engine in such a circumstance that not enough funds are frozen for the order.
	ForceHold *bool `json:"forceHold,omitempty"`
	// [Self Trade Prevention](https://www.kucoin.com/docs-new/doc-338146) is divided into these strategies: CN, CO, CB. Not supported DC at the moment.
	Stp *string `json:"stp,omitempty"`
	// Margin mode: ISOLATED, CROSS, default: ISOLATED
	MarginMode *string `json:"marginMode,omitempty"`
	// Required for type is 'limit' order, indicating the operating price
	Price *string `json:"price,omitempty"`
	// **Choose one of size, qty, valueQty**, Order size (Lot), must be a positive integer. The quantity unit of coin-swap contracts is size(lot), and other units are not supported.
	Size *int32 `json:"size,omitempty"`
	// Optional for type is 'limit' order, [Time in force](https://www.kucoin.com/docs-new/doc-338146) is a special strategy used during trading, default is GTC
	TimeInForce *string `json:"timeInForce,omitempty"`
	// Optional for type is 'limit' order,  post only flag, invalid when timeInForce is IOC. When postOnly is true, not allowed choose hidden or iceberg. The post-only flag ensures that the trader always pays the maker fee and provides liquidity to the order book. If any part of the order is going to pay taker fee, the order will be fully rejected.
	PostOnly *bool `json:"postOnly,omitempty"`
	// Optional for type is 'limit' order, orders not displaying in order book. When hidden chose, not allowed choose postOnly.
	Hidden *bool `json:"hidden,omitempty"`
	// Optional for type is 'limit' order, Only visible portion of the order is displayed in the order book. When iceberg chose, not allowed choose postOnly.
	Iceberg *bool `json:"iceberg,omitempty"`
	// Optional for type is 'limit' order, The maximum visible size of an iceberg order. please place order in size (lots), The units of qty (base currency) and valueQty (value) are not supported.
	VisibleSize *string `json:"visibleSize,omitempty"`
	// **Choose one of size, qty, valueQty**, Order size (Base currency) must be an integer multiple of the multiplier. The unit of the quantity of coin-swap is size(lot), which is not supported
	Qty *string `json:"qty,omitempty"`
	// **Choose one of size, qty, valueQty**, Order size (Value), USDS-Swap correspond to USDT or USDC. The unit of the quantity of coin-swap is size(lot), which is not supported
	ValueQty *string `json:"valueQty,omitempty"`
}

// NewAddOrderReq instantiates a new AddOrderReq object
// This constructor will assign default values to properties that have it defined
func NewAddOrderReq(clientOid string, side string, symbol string, leverage int32) *AddOrderReq {
	this := AddOrderReq{}
	this.ClientOid = clientOid
	this.Side = side
	this.Symbol = symbol
	this.Leverage = leverage
	var Type_ string = "limit"
	this.Type = &Type_
	var reduceOnly bool = false
	this.ReduceOnly = &reduceOnly
	var closeOrder bool = false
	this.CloseOrder = &closeOrder
	var forceHold bool = false
	this.ForceHold = &forceHold
	var marginMode string = "ISOLATED"
	this.MarginMode = &marginMode
	var timeInForce string = "GTC"
	this.TimeInForce = &timeInForce
	var postOnly bool = false
	this.PostOnly = &postOnly
	var hidden bool = false
	this.Hidden = &hidden
	var iceberg bool = false
	this.Iceberg = &iceberg
	return &this
}

// NewAddOrderReqWithDefaults instantiates a new AddOrderReq object
// This constructor will only assign default values to properties that have it defined,
func NewAddOrderReqWithDefaults() *AddOrderReq {
	this := AddOrderReq{}
	var Type_ string = "limit"
	this.Type = &Type_
	var reduceOnly bool = false
	this.ReduceOnly = &reduceOnly
	var closeOrder bool = false
	this.CloseOrder = &closeOrder
	var forceHold bool = false
	this.ForceHold = &forceHold
	var marginMode string = "ISOLATED"
	this.MarginMode = &marginMode
	var timeInForce string = "GTC"
	this.TimeInForce = &timeInForce
	var postOnly bool = false
	this.PostOnly = &postOnly
	var hidden bool = false
	this.Hidden = &hidden
	var iceberg bool = false
	this.Iceberg = &iceberg
	return &this
}

func (o *AddOrderReq) ToMap() map[string]interface{} {
	toSerialize := map[string]interface{}{}
	toSerialize["clientOid"] = o.ClientOid
	toSerialize["side"] = o.Side
	toSerialize["symbol"] = o.Symbol
	toSerialize["leverage"] = o.Leverage
	toSerialize["type"] = o.Type
	toSerialize["remark"] = o.Remark
	toSerialize["stop"] = o.Stop
	toSerialize["stopPriceType"] = o.StopPriceType
	toSerialize["stopPrice"] = o.StopPrice
	toSerialize["reduceOnly"] = o.ReduceOnly
	toSerialize["closeOrder"] = o.CloseOrder
	toSerialize["forceHold"] = o.ForceHold
	toSerialize["stp"] = o.Stp
	toSerialize["marginMode"] = o.MarginMode
	toSerialize["price"] = o.Price
	toSerialize["size"] = o.Size
	toSerialize["timeInForce"] = o.TimeInForce
	toSerialize["postOnly"] = o.PostOnly
	toSerialize["hidden"] = o.Hidden
	toSerialize["iceberg"] = o.Iceberg
	toSerialize["visibleSize"] = o.VisibleSize
	toSerialize["qty"] = o.Qty
	toSerialize["valueQty"] = o.ValueQty
	return toSerialize
}

type AddOrderReqBuilder struct {
	obj *AddOrderReq
}

func NewAddOrderReqBuilder() *AddOrderReqBuilder {
	return &AddOrderReqBuilder{obj: NewAddOrderReqWithDefaults()}
}

// Unique order id created by users to identify their orders, the maximum length cannot exceed 40, e.g. UUID, Only allows numbers, characters, underline(_), and separator(-)
func (builder *AddOrderReqBuilder) SetClientOid(value string) *AddOrderReqBuilder {
	builder.obj.ClientOid = value
	return builder
}

// specify if the order is to 'buy' or 'sell'
func (builder *AddOrderReqBuilder) SetSide(value string) *AddOrderReqBuilder {
	builder.obj.Side = value
	return builder
}

// Symbol of the contract, Please refer to [Get Symbol endpoint: symbol](https://www.kucoin.com/docs-new/api-3470220)
func (builder *AddOrderReqBuilder) SetSymbol(value string) *AddOrderReqBuilder {
	builder.obj.Symbol = value
	return builder
}

// Used to calculate the margin to be frozen for the order. If you are to close the position, this parameter is not required.
func (builder *AddOrderReqBuilder) SetLeverage(value int32) *AddOrderReqBuilder {
	builder.obj.Leverage = value
	return builder
}

// specify if the order is an 'limit' order or 'market' order
func (builder *AddOrderReqBuilder) SetType(value string) *AddOrderReqBuilder {
	builder.obj.Type = &value
	return builder
}

// remark for the order, length cannot exceed 100 utf8 characters
func (builder *AddOrderReqBuilder) SetRemark(value string) *AddOrderReqBuilder {
	builder.obj.Remark = &value
	return builder
}

// Either 'down' or 'up'.  If stop is used,parameter stopPrice and stopPriceType also need to be provieded.
func (builder *AddOrderReqBuilder) SetStop(value string) *AddOrderReqBuilder {
	builder.obj.Stop = &value
	return builder
}

// Either 'TP', 'IP' or 'MP', Need to be defined if stop is specified.
func (builder *AddOrderReqBuilder) SetStopPriceType(value string) *AddOrderReqBuilder {
	builder.obj.StopPriceType = &value
	return builder
}

// Need to be defined if stop is specified.
func (builder *AddOrderReqBuilder) SetStopPrice(value string) *AddOrderReqBuilder {
	builder.obj.StopPrice = &value
	return builder
}

// A mark to reduce the position size only. Set to false by default. Need to set the position size when reduceOnly is true. If set to true, only the orders reducing the position size will be executed. If the reduce-only order size exceeds the position size, the extra size will be canceled.
func (builder *AddOrderReqBuilder) SetReduceOnly(value bool) *AddOrderReqBuilder {
	builder.obj.ReduceOnly = &value
	return builder
}

// A mark to close the position. Set to false by default. If closeOrder is set to true, the system will close the position and the position size will become 0. Side, Size and Leverage fields can be left empty and the system will determine the side and size automatically.
func (builder *AddOrderReqBuilder) SetCloseOrder(value bool) *AddOrderReqBuilder {
	builder.obj.CloseOrder = &value
	return builder
}

// A mark to forcely hold the funds for an order, even though it's an order to reduce the position size. This helps the order stay on the order book and not get canceled when the position size changes. Set to false by default. The system will forcely freeze certain amount of funds for this order, including orders whose direction is opposite to the current positions. This feature is to ensure that the order won’t be canceled by the matching engine in such a circumstance that not enough funds are frozen for the order.
func (builder *AddOrderReqBuilder) SetForceHold(value bool) *AddOrderReqBuilder {
	builder.obj.ForceHold = &value
	return builder
}

// [Self Trade Prevention](https://www.kucoin.com/docs-new/doc-338146) is divided into these strategies: CN, CO, CB. Not supported DC at the moment.
func (builder *AddOrderReqBuilder) SetStp(value string) *AddOrderReqBuilder {
	builder.obj.Stp = &value
	return builder
}

// Margin mode: ISOLATED, CROSS, default: ISOLATED
func (builder *AddOrderReqBuilder) SetMarginMode(value string) *AddOrderReqBuilder {
	builder.obj.MarginMode = &value
	return builder
}

// Required for type is 'limit' order, indicating the operating price
func (builder *AddOrderReqBuilder) SetPrice(value string) *AddOrderReqBuilder {
	builder.obj.Price = &value
	return builder
}

// **Choose one of size, qty, valueQty**, Order size (Lot), must be a positive integer. The quantity unit of coin-swap contracts is size(lot), and other units are not supported.
func (builder *AddOrderReqBuilder) SetSize(value int32) *AddOrderReqBuilder {
	builder.obj.Size = &value
	return builder
}

// Optional for type is 'limit' order, [Time in force](https://www.kucoin.com/docs-new/doc-338146) is a special strategy used during trading, default is GTC
func (builder *AddOrderReqBuilder) SetTimeInForce(value string) *AddOrderReqBuilder {
	builder.obj.TimeInForce = &value
	return builder
}

// Optional for type is 'limit' order,  post only flag, invalid when timeInForce is IOC. When postOnly is true, not allowed choose hidden or iceberg. The post-only flag ensures that the trader always pays the maker fee and provides liquidity to the order book. If any part of the order is going to pay taker fee, the order will be fully rejected.
func (builder *AddOrderReqBuilder) SetPostOnly(value bool) *AddOrderReqBuilder {
	builder.obj.PostOnly = &value
	return builder
}

// Optional for type is 'limit' order, orders not displaying in order book. When hidden chose, not allowed choose postOnly.
func (builder *AddOrderReqBuilder) SetHidden(value bool) *AddOrderReqBuilder {
	builder.obj.Hidden = &value
	return builder
}

// Optional for type is 'limit' order, Only visible portion of the order is displayed in the order book. When iceberg chose, not allowed choose postOnly.
func (builder *AddOrderReqBuilder) SetIceberg(value bool) *AddOrderReqBuilder {
	builder.obj.Iceberg = &value
	return builder
}

// Optional for type is 'limit' order, The maximum visible size of an iceberg order. please place order in size (lots), The units of qty (base currency) and valueQty (value) are not supported.
func (builder *AddOrderReqBuilder) SetVisibleSize(value string) *AddOrderReqBuilder {
	builder.obj.VisibleSize = &value
	return builder
}

// **Choose one of size, qty, valueQty**, Order size (Base currency) must be an integer multiple of the multiplier. The unit of the quantity of coin-swap is size(lot), which is not supported
func (builder *AddOrderReqBuilder) SetQty(value string) *AddOrderReqBuilder {
	builder.obj.Qty = &value
	return builder
}

// **Choose one of size, qty, valueQty**, Order size (Value), USDS-Swap correspond to USDT or USDC. The unit of the quantity of coin-swap is size(lot), which is not supported
func (builder *AddOrderReqBuilder) SetValueQty(value string) *AddOrderReqBuilder {
	builder.obj.ValueQty = &value
	return builder
}

func (builder *AddOrderReqBuilder) Build() *AddOrderReq {
	return builder.obj
}
