// Code generated by Kucoin Universal SDK Generator; DO NOT EDIT.

package positions

import (
	"github.com/Kucoin/kucoin-universal-sdk/sdk/golang/pkg/types"
)

// GetMaxOpenSizeResp struct for GetMaxOpenSizeResp
type GetMaxOpenSizeResp struct {
	// common response
	CommonResponse *types.RestResponse
	// Symbol of the contract, Please refer to [Get Symbol endpoint: symbol](https://www.kucoin.com/docs-new/api-3470220)
	Symbol string `json:"symbol,omitempty"`
	// Maximum buy size
	MaxBuyOpenSize int32 `json:"maxBuyOpenSize,omitempty"`
	// Maximum buy size
	MaxSellOpenSize int32 `json:"maxSellOpenSize,omitempty"`
}

// NewGetMaxOpenSizeResp instantiates a new GetMaxOpenSizeResp object
// This constructor will assign default values to properties that have it defined
func NewGetMaxOpenSizeResp(symbol string, maxBuyOpenSize int32, maxSellOpenSize int32) *GetMaxOpenSizeResp {
	this := GetMaxOpenSizeResp{}
	this.Symbol = symbol
	this.MaxBuyOpenSize = maxBuyOpenSize
	this.MaxSellOpenSize = maxSellOpenSize
	return &this
}

// NewGetMaxOpenSizeRespWithDefaults instantiates a new GetMaxOpenSizeResp object
// This constructor will only assign default values to properties that have it defined,
func NewGetMaxOpenSizeRespWithDefaults() *GetMaxOpenSizeResp {
	this := GetMaxOpenSizeResp{}
	return &this
}

func (o *GetMaxOpenSizeResp) ToMap() map[string]interface{} {
	toSerialize := map[string]interface{}{}
	toSerialize["symbol"] = o.Symbol
	toSerialize["maxBuyOpenSize"] = o.MaxBuyOpenSize
	toSerialize["maxSellOpenSize"] = o.MaxSellOpenSize
	return toSerialize
}

func (o *GetMaxOpenSizeResp) SetCommonResponse(response *types.RestResponse) {
	o.CommonResponse = response
}
