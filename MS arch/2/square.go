package main

import "fmt"

func main() {
	var num string
	fmt.Scanln(&num)
	digits := []rune(num)
	for i := 0; i < len(digits); i++ {
		digits[i] = digits[i] - rune('0')
		fmt.Print(digits[i] * digits[i])
	}
}
