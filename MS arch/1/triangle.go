package main

import "fmt"

func main() {
	var a, b, c uint32
	fmt.Scanln(&a)
	fmt.Scanln(&b)
	fmt.Scanln(&c)
	if a*a+b*b != c*c {
		fmt.Print("не")
	}
	fmt.Println("прямоугольный")
}
