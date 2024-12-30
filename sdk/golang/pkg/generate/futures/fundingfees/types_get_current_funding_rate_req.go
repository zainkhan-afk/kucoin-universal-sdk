// Code generated by Kucoin Universal SDK Generator; DO NOT EDIT.

package fundingfees

// GetCurrentFundingRateReq struct for GetCurrentFundingRateReq
type GetCurrentFundingRateReq struct {
	// Symbol of the contract, Please refer to [Get Symbol endpoint: symbol](https://www.kucoin.com/docs-new/api-3470220)
	Symbol *string `json:"symbol,omitempty" path:"symbol" url:"-"`
}

// NewGetCurrentFundingRateReq instantiates a new GetCurrentFundingRateReq object
// This constructor will assign default values to properties that have it defined
func NewGetCurrentFundingRateReq() *GetCurrentFundingRateReq {
	this := GetCurrentFundingRateReq{}
	return &this
}

// NewGetCurrentFundingRateReqWithDefaults instantiates a new GetCurrentFundingRateReq object
// This constructor will only assign default values to properties that have it defined,
func NewGetCurrentFundingRateReqWithDefaults() *GetCurrentFundingRateReq {
	this := GetCurrentFundingRateReq{}
	return &this
}

func (o *GetCurrentFundingRateReq) ToMap() map[string]interface{} {
	toSerialize := map[string]interface{}{}
	toSerialize["symbol"] = o.Symbol
	return toSerialize
}

type GetCurrentFundingRateReqBuilder struct {
	obj *GetCurrentFundingRateReq
}

func NewGetCurrentFundingRateReqBuilder() *GetCurrentFundingRateReqBuilder {
	return &GetCurrentFundingRateReqBuilder{obj: NewGetCurrentFundingRateReqWithDefaults()}
}

// Symbol of the contract, Please refer to [Get Symbol endpoint: symbol](https://www.kucoin.com/docs-new/api-3470220)
func (builder *GetCurrentFundingRateReqBuilder) SetSymbol(value string) *GetCurrentFundingRateReqBuilder {
	builder.obj.Symbol = &value
	return builder
}

func (builder *GetCurrentFundingRateReqBuilder) Build() *GetCurrentFundingRateReq {
	return builder.obj
}
