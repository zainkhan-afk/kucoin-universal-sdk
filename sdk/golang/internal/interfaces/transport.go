package interfaces

import "context"

// Transport is an interface that represents a generic transport layer.
// It has a single method, called Call, which accepts a context, a method name,
// a path, a request payload and a response struct. The method should perform
// a call to some remote service using the provided information and fill the
// response with the obtained data. In case of any errors during this process,
// the method should return them to the caller.
type Transport interface {
	Call(ctx context.Context, domain string, isBroker bool, method string, path string, request interface{}, response Response, requestJson bool) error

	Close() error
}
