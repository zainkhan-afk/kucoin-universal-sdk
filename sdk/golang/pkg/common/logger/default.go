package logger

import (
	"fmt"
	"log"
	"os"
	"runtime"
	"strings"
	"sync/atomic"
	"time"
)

type DefaultLogger struct {
	Logger     *log.Logger
	Level      Level
	Formatter  string
	TimeFormat string
}

func NewDefaultLogger() *DefaultLogger {
	return &DefaultLogger{
		Logger:     log.New(os.Stdout, "", 0),
		Level:      INFO,
		Formatter:  "%s [%s] [%s+%d] [%s] %s",
		TimeFormat: "2006-01-02 15:04:05.000",
	}
}

func (d *DefaultLogger) formatLog(level string, args ...interface{}) string {
	// Get the caller information
	pc, file, line, ok := runtime.Caller(2) // Skip two levels to get the original caller of the log
	function := "unknown"
	if ok {
		function = runtime.FuncForPC(pc).Name()
		// Get only the base name of the file and function name
		file = file[strings.LastIndex(file, "/")+1:]
		function = function[strings.LastIndex(function, "/")+1:]
	}
	timestamp := time.Now().Format(d.TimeFormat)
	return fmt.Sprintf(d.Formatter, timestamp, level, file, line, function, fmt.Sprint(args...))
}

func (d *DefaultLogger) formatLogf(level, format string, args ...interface{}) string {
	// Get the caller information
	pc, file, line, ok := runtime.Caller(2) // Skip two levels to get the original caller of the log
	function := "unknown"
	if ok {
		function = runtime.FuncForPC(pc).Name()
		// Get only the base name of the file and function name
		file = file[strings.LastIndex(file, "/")+1:]
		function = function[strings.LastIndex(function, "/")+1:]
	}

	timestamp := time.Now().Format(d.TimeFormat)
	return fmt.Sprintf(d.Formatter, timestamp, level, file, line, function, fmt.Sprintf(format, args...))
}

func (d *DefaultLogger) Trace(args ...interface{}) {
	if d.Level.CheckLevel(TRACE) {
		d.Logger.Println(d.formatLog("TRACE", args...))
	}
}

func (d *DefaultLogger) Debug(args ...interface{}) {
	if d.Level.CheckLevel(DEBUG) {
		d.Logger.Println(d.formatLog("DEBUG", args...))
	}
}

func (d *DefaultLogger) Info(args ...interface{}) {
	if d.Level.CheckLevel(INFO) {
		d.Logger.Println(d.formatLog("INFO", args...))
	}
}

func (d *DefaultLogger) Warn(args ...interface{}) {
	if d.Level.CheckLevel(WARN) {
		d.Logger.Println(d.formatLog("WARN", args...))
	}
}

func (d *DefaultLogger) Error(args ...interface{}) {
	if d.Level.CheckLevel(ERROR) {
		d.Logger.Println(d.formatLog("ERROR", args...))
	}
}

func (d *DefaultLogger) Fatal(args ...interface{}) {
	if d.Level.CheckLevel(FATAL) {
		d.Logger.Fatal(d.formatLog("FATAL", args...))
	}
}

func (d *DefaultLogger) Panic(args ...interface{}) {
	if d.Level.CheckLevel(PANIC) {
		d.Logger.Panic(d.formatLog("PANIC", args...))
	}
}

func (d *DefaultLogger) Tracef(format string, args ...interface{}) {
	if d.Level.CheckLevel(TRACE) {
		d.Logger.Println(d.formatLogf("TRACE", format, args...))
	}
}

func (d *DefaultLogger) Debugf(format string, args ...interface{}) {
	if d.Level.CheckLevel(DEBUG) {
		d.Logger.Println(d.formatLogf("DEBUG", format, args...))
	}
}

func (d *DefaultLogger) Infof(format string, args ...interface{}) {
	if d.Level.CheckLevel(INFO) {
		d.Logger.Println(d.formatLogf("INFO", format, args...))
	}
}

func (d *DefaultLogger) Warnf(format string, args ...interface{}) {
	if d.Level.CheckLevel(WARN) {
		d.Logger.Println(d.formatLogf("WARN", format, args...))
	}
}

func (d *DefaultLogger) Errorf(format string, args ...interface{}) {
	if d.Level.CheckLevel(ERROR) {
		d.Logger.Println(d.formatLogf("ERROR", format, args...))
	}
}

func (d *DefaultLogger) Fatalf(format string, args ...interface{}) {
	if d.Level.CheckLevel(FATAL) {
		d.Logger.Fatalf(d.formatLogf("FATAL", format, args...))
	}
}

func (d *DefaultLogger) Panicf(format string, args ...interface{}) {
	if d.Level.CheckLevel(PANIC) {
		d.Logger.Panicf(d.formatLogf("PANIC", format, args...))
	}
}

func (d *DefaultLogger) SetLevel(level Level) {
	atomic.StoreUint32((*uint32)(&d.Level), uint32(level))
}

func (d *DefaultLogger) GetLevel() Level {
	return Level(atomic.LoadUint32((*uint32)(&d.Level)))
}
