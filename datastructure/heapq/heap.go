package tools

import (
	"sync"
)

type Item interface {
	Less(than Item) bool
}

type Int int

func (x Int) Less(than Item) bool {
	return x < than.(Int)
}

type heap struct {
	sync.Mutex
	arr []Item
}

func NewHeap() *heap {
	return &heap{arr: make([]Item, 1)}
}

func (h *heap) Head() Item {
	if len(h.arr) == 1 {
		return nil
	}
	return h.arr[1]
}

func (h *heap) Len() int {
	return len(h.arr) - 1
}

func (h *heap) Insert(n Item) {
	h.Lock()
	defer h.Unlock()
	h.arr = append(h.arr, n)
	h.siftUp()
}

func (h *heap) siftUp() {
	for i := len(h.arr) - 1; i > 1; i >>= 1 {
		if h.arr[i].Less(h.arr[i>>1]) {
			h.exchange(i, i>>1)
		} else {
			break
		}
	}
}

func (h *heap) Pop() Item {
	h.Lock()
	defer h.Unlock()
	ret := h.Head()
	if ret != nil {
		h.exchange(1, len(h.arr)-1)
		h.arr = h.arr[:len(h.arr)-1]
		h.sink()
	}
	return ret

}

func (h *heap) sink() {
	for i := 1; i < len(h.arr); {
		s := i
		lc, rc := i<<1, (i<<1)|1
		if lc < len(h.arr) && h.arr[lc].Less(h.arr[s]) {
			s = lc
		}
		if rc < len(h.arr) && h.arr[rc].Less(h.arr[s]) {
			s = rc
		}
		if s == i {
			break
		}
		h.exchange(i, s)
		i = s
	}
}

func (h *heap) exchange(i, j int) {
	h.arr[i], h.arr[j] = h.arr[j], h.arr[i]
}

func (h *heap) Sort() *[]Item {
	ret := make([]Item, len(h.arr)-1)
	arr := make([]Item, len(h.arr))
	copy(arr, h.arr)
	s := 0
	for {
		r := h.Pop()
		if r == nil {
			break
		}
		ret[s] = r
		s++
	}
	h.arr = arr
	return &ret
}
