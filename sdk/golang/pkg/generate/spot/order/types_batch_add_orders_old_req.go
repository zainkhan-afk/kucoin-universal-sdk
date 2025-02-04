// Code generated by Kucoin Universal SDK Generator; DO NOT EDIT.

package order

// BatchAddOrdersOldReq struct for BatchAddOrdersOldReq
type BatchAddOrdersOldReq struct {
	OrderList []BatchAddOrdersOldOrderList `json:"orderList,omitempty"`
	Symbol    string                       `json:"symbol,omitempty"`
}

// NewBatchAddOrdersOldReq instantiates a new BatchAddOrdersOldReq object
// This constructor will assign default values to properties that have it defined
func NewBatchAddOrdersOldReq(symbol string) *BatchAddOrdersOldReq {
	this := BatchAddOrdersOldReq{}
	this.Symbol = symbol
	return &this
}

// NewBatchAddOrdersOldReqWithDefaults instantiates a new BatchAddOrdersOldReq object
// This constructor will only assign default values to properties that have it defined,
func NewBatchAddOrdersOldReqWithDefaults() *BatchAddOrdersOldReq {
	this := BatchAddOrdersOldReq{}
	return &this
}

func (o *BatchAddOrdersOldReq) ToMap() map[string]interface{} {
	toSerialize := map[string]interface{}{}
	toSerialize["orderList"] = o.OrderList
	toSerialize["symbol"] = o.Symbol
	return toSerialize
}

type BatchAddOrdersOldReqBuilder struct {
	obj *BatchAddOrdersOldReq
}

func NewBatchAddOrdersOldReqBuilder() *BatchAddOrdersOldReqBuilder {
	return &BatchAddOrdersOldReqBuilder{obj: NewBatchAddOrdersOldReqWithDefaults()}
}

func (builder *BatchAddOrdersOldReqBuilder) SetOrderList(value []BatchAddOrdersOldOrderList) *BatchAddOrdersOldReqBuilder {
	builder.obj.OrderList = value
	return builder
}

func (builder *BatchAddOrdersOldReqBuilder) SetSymbol(value string) *BatchAddOrdersOldReqBuilder {
	builder.obj.Symbol = value
	return builder
}

func (builder *BatchAddOrdersOldReqBuilder) Build() *BatchAddOrdersOldReq {
	return builder.obj
}
