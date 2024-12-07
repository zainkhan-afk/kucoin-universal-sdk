package util

import (
	"fmt"
	"math"
	"runtime"
	"sort"
	"sync"
)

type MemStatsTracker struct {
	mu         sync.Mutex
	allocs     []uint64
	sys        []uint64
	goroutines []int
}

func (tracker *MemStatsTracker) Record() {
	var memStats runtime.MemStats
	runtime.ReadMemStats(&memStats)

	tracker.mu.Lock()
	defer tracker.mu.Unlock()

	tracker.allocs = append(tracker.allocs, memStats.Alloc/1024) // KB
	tracker.sys = append(tracker.sys, memStats.Sys/1024)         // KB
	tracker.goroutines = append(tracker.goroutines, runtime.NumGoroutine())
}

func calculateStats(data []uint64) (min, max, avg, p95, p99 uint64) {
	if len(data) == 0 {
		return 0, 0, 0, 0, 0
	}

	min = math.MaxUint64
	var sum uint64

	for _, val := range data {
		if val < min {
			min = val
		}
		if val > max {
			max = val
		}
		sum += val
	}
	avg = sum / uint64(len(data))

	// Calculate P95 and P99
	sorted := append([]uint64{}, data...)
	sort.Slice(sorted, func(i, j int) bool { return sorted[i] < sorted[j] })

	p95Index := int(0.95 * float64(len(sorted)-1))
	p95 = sorted[p95Index]

	p99Index := int(0.99 * float64(len(sorted)-1))
	p99 = sorted[p99Index]

	return
}

// CheckTrend checks whether the data is increasing, decreasing, or mixed.
func checkTrend(data []uint64) string {
	if len(data) < 2 {
		return "Not enough data"
	}

	increasing := true
	decreasing := true

	for i := 1; i < len(data); i++ {
		if data[i] > data[i-1] {
			decreasing = false
		} else if data[i] < data[i-1] {
			increasing = false
		}
	}

	if increasing {
		return "Increasing"
	}
	if decreasing {
		return "Decreasing"
	}
	return "Mixed"
}

func calculateIntStats(data []int) (min, max, avg, p95, p99 int) {
	if len(data) == 0 {
		return 0, 0, 0, 0, 0
	}

	min = math.MaxInt
	var sum int

	for _, val := range data {
		if val < min {
			min = val
		}
		if val > max {
			max = val
		}
		sum += val
	}
	avg = sum / len(data)

	// Calculate P95 and P99
	sorted := append([]int{}, data...)
	sort.Slice(sorted, func(i, j int) bool { return sorted[i] < sorted[j] })

	p95Index := int(0.95 * float64(len(sorted)-1))
	p95 = sorted[p95Index]

	p99Index := int(0.99 * float64(len(sorted)-1))
	p99 = sorted[p99Index]

	return
}

func (tracker *MemStatsTracker) PrintStats() {
	tracker.mu.Lock()
	defer tracker.mu.Unlock()

	allocMin, allocMax, allocAvg, allocP95, allocP99 := calculateStats(tracker.allocs)
	sysMin, sysMax, sysAvg, sysP95, sysP99 := calculateStats(tracker.sys)
	goroutineMin, goroutineMax, goroutineAvg, goroutineP95, goroutineP99 := calculateIntStats(tracker.goroutines)

	allocTrend := checkTrend(tracker.allocs)
	sysTrend := checkTrend(tracker.sys)

	fmt.Printf(`===================
Summary:
Alloc (KB):
  Min: %v, Max: %v, Avg: %v, P95: %v, P99: %v
  Trend: %v
Sys (KB):
  Min: %v, Max: %v, Avg: %v, P95: %v, P99: %v
  Trend: %v
Goroutines:
  Min: %v, Max: %v, Avg: %v, P95: %v, P99: %v
===================
`, allocMin, allocMax, allocAvg, allocP95, allocP99, allocTrend,
		sysMin, sysMax, sysAvg, sysP95, sysP99, sysTrend,
		goroutineMin, goroutineMax, goroutineAvg, goroutineP95, goroutineP99)

	// Print every 10 points
	fmt.Println("Detailed Alloc (KB):")
	for i := 0; i < len(tracker.allocs); i++ {
		if i%10 == 0 || i == len(tracker.allocs)-1 {
			fmt.Printf("  Point %d: %d KB\n", i, tracker.allocs[i])
		}
	}

	fmt.Println("Detailed Sys (KB):")
	for i := 0; i < len(tracker.sys); i++ {
		if i%10 == 0 || i == len(tracker.sys)-1 {
			fmt.Printf("  Point %d: %d KB\n", i, tracker.sys[i])
		}
	}

	fmt.Println("Detailed Goroutines:")
	for i := 0; i < len(tracker.goroutines); i++ {
		if i%10 == 0 || i == len(tracker.goroutines)-1 {
			fmt.Printf("  Point %d: %d\n", i, tracker.goroutines[i])
		}
	}
}
