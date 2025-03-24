package main

import "fmt"

func main() {
	var inputString string
	fmt.Scanln(&inputString)
	processedRunes := make([]rune, 0, len(inputString)*2-1)
	for i, letter := range inputString {
		if i != 0 {
			processedRunes = append(processedRunes, rune('*'))
		}
		processedRunes = append(processedRunes, rune(letter))
	}
	fmt.Println(string(processedRunes))
}
