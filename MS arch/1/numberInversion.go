package main

import "fmt"

func main() {
	var num, inversedNum int16
	inversedNum = 0
	fmt.Scanln(&num)
	for num > 0 {
		inversedNum = inversedNum*10 + num%10
		num /= 10
	}
	fmt.Println(inversedNum)
}
