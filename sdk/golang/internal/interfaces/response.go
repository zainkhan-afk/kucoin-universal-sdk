package interfaces

import (
	"github.com/Kucoin/kucoin-universal-sdk/sdk/golang/pkg/types"
)

// Response defines methods for a common response structure
type Response interface {
	SetCommonResponse(response *types.RestResponse)
}
