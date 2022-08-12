// referring to Leetcode  1157. Online Majority Element In Subarray
// https://oi-wiki.org/ds/persistent-seg/
// https://www.geeksforgeeks.org/persistent-segment-tree-set-1-introduction/

package leetcode

import (
	"sort"
)

type Node struct{
	val int
	l, r int
}

type MajorityChecker struct {
	N, idx int
	Nodes []Node
	root []int
	arr []int
}

func (this *MajorityChecker) build(l, r int)int{
	this.idx ++
	p := this.idx
	if l == r{
		return p
	}
	mid := (l+r)>>1
	this.Nodes[p].l = this.build(l, mid)
	this.Nodes[p].r = this.build(mid+1, r)
	return p
}

func (this *MajorityChecker)Insert(par, l, r, x int)int{
	this.idx++
	p := this.idx
	this.Nodes[p] = this.Nodes[par]
	if l == r{
		this.Nodes[p].val++
		return p
	}
	mid := (l+r)>>1
	if x <= mid{
		this.Nodes[p].l = this.Insert(this.Nodes[par].l, l, mid, x)
	}else{
		this.Nodes[p].r = this.Insert(this.Nodes[par].r, mid+1, r, x)
	}
    this.Nodes[p].val = this.Nodes[this.Nodes[p].l].val + this.Nodes[this.Nodes[p].r].val
	return p
}

func (this *MajorityChecker)query(par, now, l, r, k int)int{
	if l == r{
		if this.Nodes[now].val - this.Nodes[par].val >= k{
			return this.arr[l]
		}
		return -1
	}
	s := this.Nodes[this.Nodes[now].l].val - this.Nodes[this.Nodes[par].l].val
	mid := (l+r)>>1
	if s >= k{
		return this.query(this.Nodes[par].l, this.Nodes[now].l, l, mid, k)
	}else{
		return this.query(this.Nodes[par].r, this.Nodes[now].r, mid+1, r, k)
	}
}

func Constructor(arr []int) MajorityChecker {
	nodes := make([]Node, 20010 * 20)
	root := make([]int, len(arr)+1)
	m := MajorityChecker{Nodes: nodes, root: root, idx: 0}

	// Discretization
	maps := map[int]int{}
	for _, v := range arr{
		maps[v] ++
	}
	keys := make([]int, 0, len(maps))
	for k := range maps {
		keys = append(keys, k)
	}
	sort.Ints(keys)

	// Update versions in sequence
	m.arr = keys
    m.N = len(keys)
    m.root[0] = m.build(0, m.N-1)
	for i, v := range(arr){
		x := sort.Search(len(keys), func(i int) bool {return keys[i]>=v})
		m.root[i+1] = m.Insert(m.root[i], 0, len(keys)-1, x)
	}
	return m
}


func (this *MajorityChecker) Query(left int, right int, threshold int) int {
	return this.query(this.root[left], this.root[right+1], 0, this.N-1, threshold)
}


