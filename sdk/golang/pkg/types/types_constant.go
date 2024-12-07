package types

// Global API endpoints
const (
	GlobalApiEndpoint        = "https://api.kucoin.com"
	GlobalFuturesApiEndpoint = "https://api-futures.kucoin.com"
	GlobalBrokerApiEndpoint  = "https://api-broker.kucoin.com"
)

// Domain types
const (
	DomainTypeSpot    = "spot"
	DomainTypeFutures = "futures"
	DomainTypeBroker  = "broker"
)

// MessageType defines various types of messages that can be sent or received
const (
	WelcomeMessage     = "welcome"
	PingMessage        = "ping"
	PongMessage        = "pong"
	SubscribeMessage   = "subscribe"
	AckMessage         = "ack"
	UnsubscribeMessage = "unsubscribe"
	ErrorMessage       = "error"
	Message            = "message"
	Notice             = "notice"
	Command            = "command"
)

// API result codes
const (
	// CodeSuccess operation was successful
	CodeSuccess = "200000"
)
