package types

import (
	"time"
)

// WebSocketEvent defines the types of WebSocket events
type WebSocketEvent int

const (
	EventConnected        WebSocketEvent = iota // Connection established event
	EventDisconnected                           // Connection closed event
	EventTryReconnect                           // Try to reconnect event
	EventMessageReceived                        // Message received event
	EventErrorReceived                          // Error occurred event
	EventPongReceived                           // Pong message received event
	EventReadBufferFull                         // The read buffer of WebSocket is full.
	EventWriteBufferFull                        // The write buffer of WebSocket is full.
	EventCallbackError                          // An event triggered when an error occurs during a callback operation
	EventReSubscribeOK                          // ReSubscription success event
	EventReSubscribeError                       // ReSubscription error event
	EventClientFail                             // Client failure event.
	EventClientShutdown                         // Client shutdown event.
)

func (l WebSocketEvent) String() string {
	switch l {
	case EventConnected:
		return "EventConnected"
	case EventDisconnected:
		return "EventDisconnected"
	case EventTryReconnect:
		return "EventTryReconnect"
	case EventMessageReceived:
		return "EventMessageReceived"
	case EventErrorReceived:
		return "EventErrorReceived"
	case EventPongReceived:
		return "EventPongReceived"
	case EventReadBufferFull:
		return "EventReadBufferFull"
	case EventWriteBufferFull:
		return "EventWriteBufferFull"
	case EventCallbackError:
		return "EventCallbackError"
	case EventReSubscribeOK:
		return "EventReSubscribeOK"
	case EventReSubscribeError:
		return "EventReSubscribeError"
	case EventClientFail:
		return "EventClientFail"
	case EventClientShutdown:
		return "EventClientShutdown"
	default:
		return "UnknownEvent"
	}
}

// WebSocketCallback is a generic callback function type that handles all WebSocket events
type WebSocketCallback func(event WebSocketEvent, msg string)

// WebSocketClientOption contains the settings for the WebSocket client
type WebSocketClientOption struct {
	Reconnect          bool              // Enable auto-reconnect; default: true
	ReconnectAttempts  int               // Maximum reconnect attempts, -1 means forever; default: -1
	ReconnectInterval  time.Duration     // Interval between reconnect attempts; default: 5s
	DialTimeout        time.Duration     // Timeout for establishing a WebSocket connection; default: 10s
	ReadBufferBytes    int               // Specify I/O buffer sizes in bytes. The I/O buffer sizes do not limit the size of the messages that can be sent or received. default:2048000
	ReadMessageBuffer  int               // Read buffer for messages. Messages will be discarded if the buffer becomes full. default: 1024
	WriteMessageBuffer int               // Write buffer for message, Messages will be discarded if the buffer becomes full. default: 256
	WriteTimeout       time.Duration     // Write timeout; default: 30s
	EventCallback      WebSocketCallback // General callback function to handle all WebSocket events
}

func NewWebSocketClientOption() *WebSocketClientOption {
	return &WebSocketClientOption{
		Reconnect:          true,
		ReconnectAttempts:  -1,
		ReconnectInterval:  5 * time.Second,
		DialTimeout:        10 * time.Second,
		ReadBufferBytes:    2048000,
		ReadMessageBuffer:  1024,
		WriteMessageBuffer: 256,
		WriteTimeout:       30 * time.Second,
		EventCallback:      nil,
	}
}

// WebSocketClientOptionBuilder is a builder for WebSocketClientOption
type WebSocketClientOptionBuilder struct {
	option *WebSocketClientOption
}

// NewWebSocketClientOptionBuilder creates a new WebSocketClientOptionBuilder
func NewWebSocketClientOptionBuilder() *WebSocketClientOptionBuilder {
	return &WebSocketClientOptionBuilder{
		option: NewWebSocketClientOption(),
	}
}

// WithReconnect sets the Reconnect option
func (b *WebSocketClientOptionBuilder) WithReconnect(reconnect bool) *WebSocketClientOptionBuilder {
	b.option.Reconnect = reconnect
	return b
}

// WithReconnectAttempts sets the ReconnectAttempts option
func (b *WebSocketClientOptionBuilder) WithReconnectAttempts(attempts int) *WebSocketClientOptionBuilder {
	b.option.ReconnectAttempts = attempts
	return b
}

// WithReconnectInterval sets the ReconnectInterval option
func (b *WebSocketClientOptionBuilder) WithReconnectInterval(interval time.Duration) *WebSocketClientOptionBuilder {
	b.option.ReconnectInterval = interval
	return b
}

// WithDialTimeout sets the DialTimeout option
func (b *WebSocketClientOptionBuilder) WithDialTimeout(timeout time.Duration) *WebSocketClientOptionBuilder {
	b.option.DialTimeout = timeout
	return b
}

// WithReadBufferBytes set the read buffer bytes
func (b *WebSocketClientOptionBuilder) WithReadBufferBytes(readBufferBytes int) *WebSocketClientOptionBuilder {
	b.option.ReadBufferBytes = readBufferBytes
	return b
}

// WithReadMessageBuffer set the read message buffer
func (b *WebSocketClientOptionBuilder) WithReadMessageBuffer(readMessageBuffer int) *WebSocketClientOptionBuilder {
	b.option.ReadMessageBuffer = readMessageBuffer
	return b
}

// WithWriteMessageBuffer set the write message buffer
func (b *WebSocketClientOptionBuilder) WithWriteMessageBuffer(writeMessageBuffer int) *WebSocketClientOptionBuilder {
	b.option.WriteMessageBuffer = writeMessageBuffer
	return b
}

// WithWriteTimeout set the WriteTimeout option
func (b *WebSocketClientOptionBuilder) WithWriteTimeout(timeout time.Duration) *WebSocketClientOptionBuilder {
	b.option.WriteTimeout = timeout
	return b
}

// WithEventCallback sets the EventCallback option
func (b *WebSocketClientOptionBuilder) WithEventCallback(callback WebSocketCallback) *WebSocketClientOptionBuilder {
	b.option.EventCallback = callback
	return b
}

func (b *WebSocketClientOptionBuilder) Build() *WebSocketClientOption {
	return b.option
}
