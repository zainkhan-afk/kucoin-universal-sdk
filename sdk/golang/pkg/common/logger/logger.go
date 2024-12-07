package logger

import (
	"sync"
)

var (
	globalLogger Logger
	once         sync.Once
)

func SetLogger(log Logger) {
	once.Do(func() {
		globalLogger = log
	})
}

func GetLogger() Logger {
	once.Do(func() {
		globalLogger = NewDefaultLogger()
	})
	return globalLogger
}

type Logger interface {
	Trace(args ...interface{})
	Debug(args ...interface{})
	Info(args ...interface{})
	Warn(args ...interface{})
	Error(args ...interface{})
	Fatal(args ...interface{})
	Panic(args ...interface{})

	Tracef(format string, args ...interface{})
	Debugf(format string, args ...interface{})
	Infof(format string, args ...interface{})
	Warnf(format string, args ...interface{})
	Errorf(format string, args ...interface{})
	Fatalf(format string, args ...interface{})
	Panicf(format string, args ...interface{})

	SetLevel(level Level)
	GetLevel() Level
}

type Level uint32

const (
	TRACE Level = iota
	DEBUG
	INFO
	WARN
	ERROR
	FATAL
	PANIC
)

func (l Level) String() string {
	switch l {
	case TRACE:
		return "TRACE"
	case DEBUG:
		return "DEBUG"
	case INFO:
		return "INFO"
	case WARN:
		return "WARN"
	case ERROR:
		return "ERROR"
	case FATAL:
		return "FATAL"
	case PANIC:
		return "PANIC"
	default:
		return "UNKNOWN"
	}
}

func (l Level) CheckLevel(level Level) bool {
	return level >= l
}
