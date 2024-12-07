package infra

import (
	"github.com/stretchr/testify/assert"
	"testing"
)

func TestDefaultTransport_processPathVariable(t1 *testing.T) {
	t := DefaultTransport{}

	req := struct {
		Currency string `path:"currency"`
	}{Currency: "BTC"}

	result := t.processPathVariable("/test/{currency}", req)

	assert.Equal(t1, "/test/BTC", result)
}

func TestDefaultTransport_processPathVariable2(t1 *testing.T) {
	t := DefaultTransport{}

	req := struct {
		Currency string `path:"currency"`
	}{Currency: "BTC"}

	result := t.processPathVariable("/test/symbol", req)

	assert.Equal(t1, "/test/symbol", result)
}

func TestDefaultTransport_processPathVariable3(t1 *testing.T) {
	t := DefaultTransport{}

	var currency string = "BTC"
	req := struct {
		Currency *string `path:"currency"`
	}{Currency: &currency}

	result := t.processPathVariable("/test/{currency}", req)

	assert.Equal(t1, "/test/BTC", result)
}
