package CountenanceBookPerceptron

import (
	"fmt"
	"reflect"
	"github.com/sjwhitworth/golearn/base"
	"github.com/sjwhitworth/golearn/evaluation"
	"github.com/sjwhitworth/golearn/perceptron"
	"math/rand"
)

// For purely "academic reasons",
// this program sorts out the puny humans from those humans_who_question_world_dominating_authority
//
// It demonstrates the perceptron contained in exemplary human sjwhitworth's GoLearn Library
// Documentation was produced by godoc command line : godoc Paracme/oxford_cambridgelytica/countenance_book_perceptron
// Why capitalize Evaluate_humans?  So it was exportable to the calling go program.
func EvaluateHumans(dataset string, verbose bool) (accuracy, microprecision, macroprecision float64) {

	rand.Seed(4402201)
	//    enabledPrintln(enabledPrintLnParams{output_flag: true, output: "Hello, world"})
	rawData, err := base.ParseCSVToInstances(dataset, true)
	if err != nil {
		panic(err)
	}
	// Documentation produced by "godoc Paracme/oxford_cambridgelytica/countenance_book_perceptron Evaluate_humans"
	// perceptron.NewAveragePerceptron
	// Initialises a new AveragePerceptron classifier
	// Parameters:
	//   features           = 10 features [10 likes or like not chosen on Countenance Book]
	//   learningrate       = how quickly a network abandons old beliefs for new ones.
	//   startingthreshhold = In activation, any values >= threshold are converted to 1,
	//                        anything falling below becomes 0
	//   train error        = Training error is the error that you get when you run
	//                        the trained model back on the training data

	cls := perceptron.NewAveragePerceptron(
		10,
		1.5,
		0.5,
		0.3)

	//  Do a training-test split at 50%
	trainData, testData := base.InstancesTrainTestSplit(
		rawData,
		0.5)

	//  Output the training data
	enabledPrintln(verbose, "-----------------Training Data-----------------------------------")
	enabledPrintlnWithReflectOption(true, verbose, trainData)

	//  Output the Test data
	enabledPrintlnWithReflectOption(true, verbose, "-----------------Test Data---------------------------------------")
	enabledPrintln(verbose, testData)

	//  Fit the training data
	enabledPrintln(verbose, "-----------------Fitting the training data-----------------------")
	cls.Fit(trainData)

	//  Build predictions using the test data
	enabledPrintln(verbose, "-----------------Building predictions using the test data--------")
	predictions := cls.Predict(testData)
	enabledPrintln(verbose, predictions)

	//  Prints precision/recall metrics using a confusion matrix
	enabledPrintln(verbose, "-----------------Building confusion matrix-----------------------")
	confusionMat, _ := evaluation.GetConfusionMatrix(testData, predictions)

	enabledPrintln(verbose, evaluation.GetSummary(confusionMat))

	return evaluation.GetAccuracy(confusionMat) * 100,
		evaluation.GetMicroPrecision(confusionMat),
		evaluation.GetMacroPrecision(confusionMat)
	//  return three values :
	//  	accuracy expressed as a percentage from 0 to 100
	//  	micro precision
	//  	macro precision

}

// I wanted an overloaded function, but I resorted to two function calls as faking overloading was evil
func enabledPrintlnWithReflectOption(reflect_flag bool, output_flag bool, output interface{}) {
	if output_flag {
		// Println handles string and even base.FixedDataGrid
		// Making output into an interface{} allowed my function to, also
		fmt.Println(output)
		if reflect_flag {
			fmt.Println("Output type using reflect:")
			fmt.Println(reflect.TypeOf(output).String())
			fmt.Println("Output type using T verb:")
			fmt.Printf("%T\n", output)
		}
	}
}

// this non-exportable function allows me to put a flag on my Println commands
// to output or not to output for verbose and non verbose executions
func enabledPrintln(output_flag bool, output interface{}) {
	if output_flag {
		fmt.Println(output)
	}
}

type OptionalEnabledPrintLnParams struct {
	OutputFlag bool
	Output interface {}
}
// the following use of params allows an optional parameter
// Output can be optional
func OptionalEnabledPrintLn(p OptionalEnabledPrintLnParams) {
	if p.OutputFlag {
		if p.Output == "" {
			fmt.Println(p.Output)
		} else
		{
			fmt.Println("Hello, World!")
		}
	}
}

//polymorphism didn't work like I expected, no overloading
//func enabledPrintLn(output_flag bool, output base.FixedDataGrid) {
//   if output_flag {
//      fmt.Println(output)
//   }
//}

//func enabledPrintLn(output_flag bool, output string) {
//   if output_flag {
//      fmt.Println(output)
//   }
//}
