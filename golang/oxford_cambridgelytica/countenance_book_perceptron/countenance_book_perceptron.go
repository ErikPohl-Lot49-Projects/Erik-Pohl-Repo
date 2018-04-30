package countenance_book_perceptron

import (
	"fmt"
	"reflect"
	base "github.com/sjwhitworth/golearn/base"
	evaluation "github.com/sjwhitworth/golearn/evaluation"
	perceptron "github.com/sjwhitworth/golearn/perceptron"
	"math/rand"
)

// For purely "academic reasons",
// this program sorts out the puny humans from those humans_who_question_world_dominating_authority
//
// It demonstrates the perceptron contained in exemplary human sjwhitworth's GoLearn Library
// Documentation was produced by godoc command line : godoc Paracme/oxford_cambridgelytica/countenance_book_perceptron
// Why capitalize Evaluate_humans?  So it was exportable to the calling go program.
func Evaluate_humans(verbose bool) (accuracy, microprecision, macroprecision float64) {

	rand.Seed(4402201)
//    enabledPrintln(enabledPrintLnParams{output_flag: true, output: "Hello, world"})
    rawData, err := base.ParseCSVToInstances("C:/Users/Richard Pendrake/Downloads/countenance_book_likes.csv", true)	
	if err != nil {
		panic(err)
	}
// Documentation produced by "godoc Paracme/oxford_cambridgelytica/countenance_book_perceptron Evaluate_humans"
//perceptron.NewAveragePerceptron 
//Initialises a new AveragePerceptron classifier
// Parameters:
//   features           = 10 features [10 likes or does not like on Countenance Book]
//   learningrate       = how quickly a network abandons old beliefs for new ones.
//   startingthreshhold = In activation, any values >= threshold are converted to 1, anything falling below becomes 0 
//   train error        = Training error is the error that you get when you run the trained model back on the training data

	cls := perceptron.NewAveragePerceptron(10, 	1.5, 	0.5, 	0.3  	)

//  Do a training-test split at 50%
	trainData, testData := base.InstancesTrainTestSplit(rawData, 0.5)
	
//  Output the training data
	enabledPrintln(verbose,"-----------------Training Data-----------------------------------")
	enabledPrintlnWithReflectOption(true,verbose,trainData)
	
//  Output the Test data
	enabledPrintlnWithReflectOption(true,verbose,"-----------------Test Data---------------------------------------")
	enabledPrintln(verbose,testData)

//  Fit the training data 
	enabledPrintln(verbose,"-----------------Fitting the training data-----------------------")
	cls.Fit(trainData)

//  Build predictions using the test data
	enabledPrintln(verbose,"-----------------Building predictions using the test data--------")
	predictions := cls.Predict(testData)
	enabledPrintln(verbose,predictions)
	
//  Prints precision/recall metrics using a confusion matrix
	enabledPrintln(verbose,"-----------------Building confusion matrix-----------------------")
	confusionMat, _ := evaluation.GetConfusionMatrix(testData, predictions)
	enabledPrintln(verbose, evaluation.GetSummary(confusionMat))

//  return three values : accuracy expressed as a percentage from 0 to 100, micro precision, and macro precision	
	return evaluation.GetAccuracy(confusionMat)*100, evaluation.GetMicroPrecision(confusionMat), evaluation.GetMacroPrecision(confusionMat)
}

// I wanted an overloaded function, but I resorted to two function calls as faking overloading was evil
func enabledPrintlnWithReflectOption(reflect_flag bool, output_flag bool, output interface{}) {
   if output_flag {
      fmt.Println(output) // println handes string and even base.FixedDataGrid !
	  if reflect_flag {
         fmt.Println(reflect.TypeOf(output).String())
      }
   }
}

// this non-exportable function allows me to put a flag on my Println commands to output or not to output for verbose and non verbose executions
func enabledPrintln(output_flag bool, output interface{}) {
   if output_flag {
      fmt.Println(output) // println handes string and even base.FixedDataGrid !
   }
}

//type enabledPrintLnParams struct {
//   reflect_flag, output_flag bool 
//   output interface{}
//}

// the following use of params allows a faked out optional parameter of type enabledPrintLn(enabledPrintLnParams{output_flag: true, output: "Hello, world"})
//func enabledPrintLn(p enabledPrintLnParams) {
//   if p.output_flag {
//      fmt.Println(p.output) // println handes string and even base.FixedDataGrid !
//      fmt.Println("hello")
//   }
//   if p.reflect_flag {
//      fmt.Println(reflect.TypeOf(p.output).String())
//   }
//}

//func enabledPrintLn(output_flag bool, output string) {  //polymorphism didn't work like I expected, no overloading
//   if output_flag {
//      fmt.Println(output)
//   }
// } 