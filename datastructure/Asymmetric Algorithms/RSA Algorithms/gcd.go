package tools

func gcd(a, b int) int {
	if b == 0 {
		return a
	}
	return gcd(b, a%b)
}

func Gcd(a, b int) int {
	for {
		if b == 0 {
			break
		}
		a, b = b, a%b
	}
	return a
}

func Exgcd(a, b int) (x, y, mod int) {
	if b == 0 {
		x, y, mod = 1, 0, a
		return
	}
	x1, y1, mod := Exgcd(b, a%b)
	x = y1
	y = x1 - y1*(a/b)
	return
}

func ModInverse(a, mod int) int {
	x, _, r := Exgcd(a, mod)
	if r == 1 {
		x %= mod
		if x < 0 {
			x += mod
		}
		return x
	}
	return -1
}
