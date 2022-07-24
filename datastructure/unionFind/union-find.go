package tools

type Union_find struct {
	U, Rank  []int
	SetCount int
}

func NewUnionFind(n int) *Union_find {
	parent := make([]int, n)
	size := make([]int, n)
	for i := range parent {
		parent[i] = i
		size[i] = 1
	}
	return &Union_find{parent, size, n}
}

func (uf *Union_find) Find(x int) int {
	for {
		if uf.U[x] == x {
			break
		}
		x = uf.U[x]
	}
	return x
}

func (uf *Union_find) Union(x, y int) bool {
	parx, pary := uf.Find(x), uf.Find(y)
	if parx == pary {
		return false
	}
	if uf.Rank[parx] > uf.Rank[pary] {
		parx, pary = pary, parx
	}
	uf.Rank[pary] += uf.Rank[parx]
	uf.U[parx] = pary
	uf.SetCount--
	return true
}
