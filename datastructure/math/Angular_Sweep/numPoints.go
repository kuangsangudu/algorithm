// referring to https://www.geeksforgeeks.org/angular-sweep-maximum-points-can-enclosed-circle-given-radius/
// referring to the leetcode 1453. Maximum Number of Darts Inside of a Circular Dartboard

package leetcode

import (
	"math"
	"sort"
)

func NumPoints(darts [][]int, r int) int {
	dis := make([][]float64, len(darts))
	for i := range dis {
		dis[i] = make([]float64, len(darts))
	}
	for i, val := range darts {
		for j := i + 1; j < len(darts); j++ {
			dis[i][j] = math.Sqrt(math.Pow(float64(val[0])-float64(darts[j][0]), 2) + math.Pow(float64(val[1])-float64(darts[j][1]), 2))
			dis[j][i] = dis[i][j]
		}
	}

	type angle struct {
		x float64
		y bool
	}

	f := func(i, n int, r float64) int {
		eps := 0.00001
		angles := make([]angle, 0)
		for j := 0; j < n; j++ {
			if i != j && dis[i][j] <= 2*r+eps {
				b := math.Atan2(float64(darts[j][1])-float64(darts[i][1]), float64(darts[j][0])-float64(darts[i][0]))
				a := math.Acos(dis[i][j] / (2 * r))

				angles = append(angles, angle{x: b - a, y: true})
				angles = append(angles, angle{x: b + a, y: false})
			}
		}

		sort.Slice(angles, func(i, j int) bool {
			if angles[i].x < angles[j].x {
				return true
			} else if angles[i].x == angles[j].x && angles[i].y {
				return true
			} else {
				return false
			}
		})

		count := 1
		re := 1
		for _, ang := range angles {
			if ang.y {
				count += 1
			} else {
				count -= 1
			}
			if count > re {
				re = count
			}
		}
		return re
	}

	ret := 1
	for i := 0; i < len(darts); i++ {
		re := f(i, len(darts), float64(r))
		if re > ret {
			ret = re
		}
	}
	return ret
}
