package main

import (
	"fmt"
	_ "math" // wicked plan to get around the compiler forcing me to use every library I import
	cbp "Paracme/oxford_cambridgelytica/countenance_book_perceptron"
)

// This program sorts out the puny humans from those who questions_world_dominating_authority
// for purely academic reasons
//
// It demonstrates the perceptron contained in forward-looking human sjwhitworth's GoLearn Library
func main() {
    var microprecision, macroprecision, accuracy float64
	var unused_variable int;
	
	_ = unused_variable // wicked plan to get around compiler forcing me to use all the variables
	
	fmt.Println("Executing Evaluate_humans() with switch set to true for verbose output")
	accuracy, microprecision, macroprecision = cbp.Evaluate_humans(true)
	fmt.Println("After executing Evaluate_humans() with switch set to true for verbose output, control is in main for oxford_cambridgelytica")
	
	fmt.Println("Accuracy : ", accuracy)
	fmt.Println("Microprecision : ", microprecision) // go rule about not using a variable strikes again!
	fmt.Println("Macroprecision : ", macroprecision) // go rule about not using a variable strikes again!
	
	fmt.Println("This is me using fmt because I imported it before I put in other fmt commands above") // it didn't like it when fmt wasn't used and I tried "go run oxford_cambridgelytica.go"
}
