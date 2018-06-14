package CountenanceBookPerceptronCombinations

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

	var testfeatures int;
	var testlearningrate, teststartingthreshhold, testtrainerror float64;
	var maxaccuracy float64 = 0;
	var maxmicroprecision float64 = 0.0
	var maxmacroprecision float64 = 0.0
	var maxtestfeatures = 0
	var maxtestlearningrate = 0.0
	var maxteststartingthreshhold = 0.0
	var maxtesttrainerror = 0.0

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

	testfeatures = 0
	for (testfeatures < 16) {
		testlearningrate = 0.0
		for (testlearningrate < 1.5) {
			teststartingthreshhold = 0.0
			for (teststartingthreshhold < 1.5) {
				testtrainerror = 0.0
				for (testtrainerror < 1.5) {
						cls := perceptron.NewAveragePerceptron(
							testfeatures,
							testlearningrate,
							teststartingthreshhold,
							testtrainerror)
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
					if (evaluation.GetAccuracy(confusionMat)*100 > maxaccuracy) {
						maxaccuracy = evaluation.GetAccuracy(confusionMat) * 100
						maxmicroprecision = evaluation.GetMicroPrecision(confusionMat)
						maxmacroprecision = evaluation.GetMacroPrecision(confusionMat)
						maxtestfeatures = testfeatures
						maxtestlearningrate = testlearningrate
						maxteststartingthreshhold = teststartingthreshhold
						maxtesttrainerror = testtrainerror
					}
					testtrainerror += .1
				}
				teststartingthreshhold = teststartingthreshhold + .1
			}
			testlearningrate = testlearningrate + .1
		}
		testfeatures = testfeatures + 1
	}
	fmt.Println("Best test features            :", maxtestfeatures)
	fmt.Println("Best test learning rate       :", maxtestlearningrate)
	fmt.Println("Best test starting threshhold :", maxteststartingthreshhold)
	fmt.Println("Best test train error         :", maxtesttrainerror)
	return maxaccuracy,
		maxmicroprecision,
		maxmacroprecision
}

// I wanted an overloaded function, but I resorted to two function calls as faking overloading was evil
func enabledPrintlnWithReflectOption(reflect_flag bool, output_flag bool, output interface{}) {
	if output_flag {
		fmt.Println(output)
		if reflect_flag {
			fmt.Println("Output type using reflect:")
			fmt.Println(reflect.TypeOf(output).String())
			fmt.Println("Output type using T verb:")
			fmt.Printf("%T\n", output)
		}
	}
}

func enabledPrintln(output_flag bool, output interface{}) {
	if output_flag {
		fmt.Println(output) // println handes string and even base.FixedDataGrid !
	}
}
