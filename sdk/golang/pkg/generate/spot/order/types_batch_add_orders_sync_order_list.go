// Code generated by Kucoin Universal SDK Generator; DO NOT EDIT.

package order

// BatchAddOrdersSyncOrderList struct for BatchAddOrdersSyncOrderList
type BatchAddOrdersSyncOrderList struct {
	// Client Order Id，The ClientOid field is a unique ID created by the user（we recommend using a UUID）, and can only contain numbers, letters, underscores （_）, and hyphens （-）. This field is returned when order information is obtained. You can use clientOid to tag your orders. ClientOid is different from the order ID created by the service provider. Please do not initiate requests using the same clientOid. The maximum length for the ClientOid is 40 characters.
	ClientOid *string `json:"clientOid,omitempty"`
	// symbol
	Symbol string `json:"symbol,omitempty"`
	// Specify if the order is an 'limit' order or 'market' order.
	Type string `json:"type,omitempty"`
	// [Time in force](doc://link/pages/338146) is a special strategy used during trading
	TimeInForce *string `json:"timeInForce,omitempty"`
	// Specify if the order is to 'buy' or 'sell'
	Side string `json:"side,omitempty"`
	// Specify price for order
	Price string `json:"price,omitempty"`
	// Specify quantity for order  When **type** is limit, select one out of two: size or funds, size refers to the amount of trading targets (the asset name written in front) for the trading pair. Teh Size must be based on the baseIncrement of the trading pair. The baseIncrement represents the precision for the trading pair. The size of an order must be a positive-integer multiple of baseIncrement and must be between baseMinSize and baseMaxSize.  When **type** is market, select one out of two: size or funds
	Size *string `json:"size,omitempty"`
	// [Self Trade Prevention](doc://link/pages/338146) is divided into four strategies: CN, CO, CB , and DC
	Stp *string `json:"stp,omitempty"`
	// Cancel after n seconds，the order timing strategy is GTT
	CancelAfter *int64 `json:"cancelAfter,omitempty"`
	// passive order labels, this is disabled when the order timing strategy is IOC or FOK
	PostOnly *bool `json:"postOnly,omitempty"`
	// [Hidden order](doc://link/pages/338146) or not (not shown in order book)
	Hidden *bool `json:"hidden,omitempty"`
	// Whether or not only visible portions of orders are shown in [Iceberg orders](doc://link/pages/338146)
	Iceberg *bool `json:"iceberg,omitempty"`
	// Maximum visible quantity in iceberg orders
	VisibleSize *string `json:"visibleSize,omitempty"`
	// Order tag, length cannot exceed 20 characters (ASCII)
	Tags *string `json:"tags,omitempty"`
	// Order placement remarks, length cannot exceed 20 characters (ASCII)
	Remark *string `json:"remark,omitempty"`
	// When **type** is market, select one out of two: size or funds
	Funds *string `json:"funds,omitempty"`
}

// NewBatchAddOrdersSyncOrderList instantiates a new BatchAddOrdersSyncOrderList object
// This constructor will assign default values to properties that have it defined
func NewBatchAddOrdersSyncOrderList(symbol string, Type_ string, side string, price string) *BatchAddOrdersSyncOrderList {
	this := BatchAddOrdersSyncOrderList{}
	this.Symbol = symbol
	this.Type = Type_
	var timeInForce string = "GTC"
	this.TimeInForce = &timeInForce
	this.Side = side
	this.Price = price
	var postOnly bool = false
	this.PostOnly = &postOnly
	var hidden bool = false
	this.Hidden = &hidden
	var iceberg bool = false
	this.Iceberg = &iceberg
	return &this
}

// NewBatchAddOrdersSyncOrderListWithDefaults instantiates a new BatchAddOrdersSyncOrderList object
// This constructor will only assign default values to properties that have it defined,
func NewBatchAddOrdersSyncOrderListWithDefaults() *BatchAddOrdersSyncOrderList {
	this := BatchAddOrdersSyncOrderList{}
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

func (o *BatchAddOrdersSyncOrderList) ToMap() map[string]interface{} {
	toSerialize := map[string]interface{}{}
	toSerialize["clientOid"] = o.ClientOid
	toSerialize["symbol"] = o.Symbol
	toSerialize["type"] = o.Type
	toSerialize["timeInForce"] = o.TimeInForce
	toSerialize["side"] = o.Side
	toSerialize["price"] = o.Price
	toSerialize["size"] = o.Size
	toSerialize["stp"] = o.Stp
	toSerialize["cancelAfter"] = o.CancelAfter
	toSerialize["postOnly"] = o.PostOnly
	toSerialize["hidden"] = o.Hidden
	toSerialize["iceberg"] = o.Iceberg
	toSerialize["visibleSize"] = o.VisibleSize
	toSerialize["tags"] = o.Tags
	toSerialize["remark"] = o.Remark
	toSerialize["funds"] = o.Funds
	return toSerialize
}

type BatchAddOrdersSyncOrderListBuilder struct {
	obj *BatchAddOrdersSyncOrderList
}

func NewBatchAddOrdersSyncOrderListBuilder() *BatchAddOrdersSyncOrderListBuilder {
	return &BatchAddOrdersSyncOrderListBuilder{obj: NewBatchAddOrdersSyncOrderListWithDefaults()}
}

// Client Order Id，The ClientOid field is a unique ID created by the user（we recommend using a UUID）, and can only contain numbers, letters, underscores （_）, and hyphens （-）. This field is returned when order information is obtained. You can use clientOid to tag your orders. ClientOid is different from the order ID created by the service provider. Please do not initiate requests using the same clientOid. The maximum length for the ClientOid is 40 characters.
func (builder *BatchAddOrdersSyncOrderListBuilder) SetClientOid(value string) *BatchAddOrdersSyncOrderListBuilder {
	builder.obj.ClientOid = &value
	return builder
}

// symbol
func (builder *BatchAddOrdersSyncOrderListBuilder) SetSymbol(value string) *BatchAddOrdersSyncOrderListBuilder {
	builder.obj.Symbol = value
	return builder
}

// Specify if the order is an 'limit' order or 'market' order.
func (builder *BatchAddOrdersSyncOrderListBuilder) SetType(value string) *BatchAddOrdersSyncOrderListBuilder {
	builder.obj.Type = value
	return builder
}

// [Time in force](doc://link/pages/338146) is a special strategy used during trading
func (builder *BatchAddOrdersSyncOrderListBuilder) SetTimeInForce(value string) *BatchAddOrdersSyncOrderListBuilder {
	builder.obj.TimeInForce = &value
	return builder
}

// Specify if the order is to 'buy' or 'sell'
func (builder *BatchAddOrdersSyncOrderListBuilder) SetSide(value string) *BatchAddOrdersSyncOrderListBuilder {
	builder.obj.Side = value
	return builder
}

// Specify price for order
func (builder *BatchAddOrdersSyncOrderListBuilder) SetPrice(value string) *BatchAddOrdersSyncOrderListBuilder {
	builder.obj.Price = value
	return builder
}

// Specify quantity for order  When **type** is limit, select one out of two: size or funds, size refers to the amount of trading targets (the asset name written in front) for the trading pair. Teh Size must be based on the baseIncrement of the trading pair. The baseIncrement represents the precision for the trading pair. The size of an order must be a positive-integer multiple of baseIncrement and must be between baseMinSize and baseMaxSize.  When **type** is market, select one out of two: size or funds
func (builder *BatchAddOrdersSyncOrderListBuilder) SetSize(value string) *BatchAddOrdersSyncOrderListBuilder {
	builder.obj.Size = &value
	return builder
}

// [Self Trade Prevention](doc://link/pages/338146) is divided into four strategies: CN, CO, CB , and DC
func (builder *BatchAddOrdersSyncOrderListBuilder) SetStp(value string) *BatchAddOrdersSyncOrderListBuilder {
	builder.obj.Stp = &value
	return builder
}

// Cancel after n seconds，the order timing strategy is GTT
func (builder *BatchAddOrdersSyncOrderListBuilder) SetCancelAfter(value int64) *BatchAddOrdersSyncOrderListBuilder {
	builder.obj.CancelAfter = &value
	return builder
}

// passive order labels, this is disabled when the order timing strategy is IOC or FOK
func (builder *BatchAddOrdersSyncOrderListBuilder) SetPostOnly(value bool) *BatchAddOrdersSyncOrderListBuilder {
	builder.obj.PostOnly = &value
	return builder
}

// [Hidden order](doc://link/pages/338146) or not (not shown in order book)
func (builder *BatchAddOrdersSyncOrderListBuilder) SetHidden(value bool) *BatchAddOrdersSyncOrderListBuilder {
	builder.obj.Hidden = &value
	return builder
}

// Whether or not only visible portions of orders are shown in [Iceberg orders](doc://link/pages/338146)
func (builder *BatchAddOrdersSyncOrderListBuilder) SetIceberg(value bool) *BatchAddOrdersSyncOrderListBuilder {
	builder.obj.Iceberg = &value
	return builder
}

// Maximum visible quantity in iceberg orders
func (builder *BatchAddOrdersSyncOrderListBuilder) SetVisibleSize(value string) *BatchAddOrdersSyncOrderListBuilder {
	builder.obj.VisibleSize = &value
	return builder
}

// Order tag, length cannot exceed 20 characters (ASCII)
func (builder *BatchAddOrdersSyncOrderListBuilder) SetTags(value string) *BatchAddOrdersSyncOrderListBuilder {
	builder.obj.Tags = &value
	return builder
}

// Order placement remarks, length cannot exceed 20 characters (ASCII)
func (builder *BatchAddOrdersSyncOrderListBuilder) SetRemark(value string) *BatchAddOrdersSyncOrderListBuilder {
	builder.obj.Remark = &value
	return builder
}

// When **type** is market, select one out of two: size or funds
func (builder *BatchAddOrdersSyncOrderListBuilder) SetFunds(value string) *BatchAddOrdersSyncOrderListBuilder {
	builder.obj.Funds = &value
	return builder
}

func (builder *BatchAddOrdersSyncOrderListBuilder) Build() *BatchAddOrdersSyncOrderList {
	return builder.obj
}
