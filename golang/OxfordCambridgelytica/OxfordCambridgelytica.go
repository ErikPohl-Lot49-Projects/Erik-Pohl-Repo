package main

import (
	"fmt"
	// wicked plan to get around the compiler forcing me to use every library I import
	_ "math"
	cbp "Paracme/OxfordCambridgelytica/CountenanceBookPerceptron"
	"Paracme/OxfordCambridgelytica/CountenanceBookKNN"
	cbpc "Paracme/OxfordCambridgelytica/CountenanceBookPerceptronCombinations"
)

// For purely academic reasons only...
// This program sorts out the puny_human type of human
// from the type of human_who_questions_world_dominating_authority.
//
// It demonstrates the perceptron and the K-Nearest Neighbors contained
// in forward-looking human sjwhitworth's GoLearn Library
//
func main() {
	const HeterogeneousDataset = "C:/Users/Richard Pendrake/MLDatasets/countenance_book_likes_variety.csv"
	const UnanimousDataset = "C:/Users/Richard Pendrake/MLDatasets/countenance_book_likes_unanimity.csv"

	var microprecision, macroprecision, accuracy float64
	var unused_variable int;

	// wicked plan to get around compiler forcing me to use all the variables
	_ = unused_variable

	fmt.Println("Executing EvaluateHumans() with switch set to true for verbose output")

	accuracy,
		microprecision,
		macroprecision = cbp.EvaluateHumans(HeterogeneousDataset, true)
	fmt.Println("After executing EvaluateHumans() with switch set to true for verbose output,")
	fmt.Println("control is in main for oxford_cambridgelytica")

	fmt.Println("Accuracy : ", accuracy)
	fmt.Println("Microprecision : ", microprecision)
	fmt.Println("Macroprecision : ", macroprecision)

	// it didn't like it when fmt wasn't used and I tried "go run oxford_cambridgelytica.go"
	fmt.Println("This is me using fmt because I imported it before I put in other fmt commands above")

	fmt.Println("HERE IS RUNNING ALL COMBINATIONS: This takes a long time!!!!")
	accuracy, microprecision, macroprecision = cbpc.EvaluateHumans(HeterogeneousDataset,
		false)
	fmt.Println("Accuracy : ", accuracy)
	fmt.Println("Microprecision : ", microprecision)
	fmt.Println("Macroprecision : ", macroprecision)

	fmt.Println("Now K Nearest Neighbors")
	accuracy,
		microprecision,
		macroprecision = CountenanceBookKNN.EvaluateHumans(HeterogeneousDataset, false)

	fmt.Println("How I stumbled into the perceptron XOR problem")
	accuracy,
		microprecision,
		macroprecision = cbp.EvaluateHumans(UnanimousDataset, false)
	fmt.Printf("Accuracy for UnanimousDataset using a perceptron is %v percent\n", accuracy)
	fmt.Println("And I was stuck there a long time, trying different perceptron settings ")
	fmt.Println("until someone told me it is a problem with perceptrons")
	fmt.Println("https://www.quora.com/Why-cant-the-XOR-problem-be-solved-by-a-one-layer-perceptron")
	fmt.Println("See Minksy and Papert  Perceptrons: An Introduction to Computational Geometry (1969)")
	fmt.Println("And I was, like, let me try K-Nearest Neighbors instead, because it looks at clusters")
	accuracy,
		microprecision,
		macroprecision = CountenanceBookKNN.EvaluateHumans(UnanimousDataset, false)
	fmt.Printf("Accuracy for UnanimousDataset using a KNN is the expected %v percent\n", accuracy)
}
