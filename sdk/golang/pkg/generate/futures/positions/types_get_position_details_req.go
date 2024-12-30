// Code generated by Kucoin Universal SDK Generator; DO NOT EDIT.

package positions

// GetPositionDetailsReq struct for GetPositionDetailsReq
type GetPositionDetailsReq struct {
	// Symbol of the contract, Please refer to [Get Symbol endpoint: symbol](https://www.kucoin.com/docs-new/api-3470220)
	Symbol *string `json:"symbol,omitempty" url:"symbol,omitempty"`
}

// NewGetPositionDetailsReq instantiates a new GetPositionDetailsReq object
// This constructor will assign default values to properties that have it defined
func NewGetPositionDetailsReq() *GetPositionDetailsReq {
	this := GetPositionDetailsReq{}
	return &this
}

// NewGetPositionDetailsReqWithDefaults instantiates a new GetPositionDetailsReq object
// This constructor will only assign default values to properties that have it defined,
func NewGetPositionDetailsReqWithDefaults() *GetPositionDetailsReq {
	this := GetPositionDetailsReq{}
	return &this
}

func (o *GetPositionDetailsReq) ToMap() map[string]interface{} {
	toSerialize := map[string]interface{}{}
	toSerialize["symbol"] = o.Symbol
	return toSerialize
}

type GetPositionDetailsReqBuilder struct {
	obj *GetPositionDetailsReq
}

func NewGetPositionDetailsReqBuilder() *GetPositionDetailsReqBuilder {
	return &GetPositionDetailsReqBuilder{obj: NewGetPositionDetailsReqWithDefaults()}
}

// Symbol of the contract, Please refer to [Get Symbol endpoint: symbol](https://www.kucoin.com/docs-new/api-3470220)
func (builder *GetPositionDetailsReqBuilder) SetSymbol(value string) *GetPositionDetailsReqBuilder {
	builder.obj.Symbol = &value
	return builder
}

func (builder *GetPositionDetailsReqBuilder) Build() *GetPositionDetailsReq {
	return builder.obj
}
