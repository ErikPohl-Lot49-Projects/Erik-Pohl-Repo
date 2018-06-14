package CountenanceBookKNN

import (
	"fmt"
	"github.com/sjwhitworth/golearn/base"
	"github.com/sjwhitworth/golearn/evaluation"
	"github.com/sjwhitworth/golearn/knn"
)

func EvaluateHumans(dataset string, verbose bool)  (accuracy, microprecision, macroprecision float64) {
	rawData,
	err := base.ParseCSVToInstances(dataset, true)
	if err != nil {
		panic(err)
	}

	//Initialises a new KNN classifier
	cls := knn.NewKnnClassifier("euclidean", "linear", 2)

	//Do a training-test split
	trainData, testData := base.InstancesTrainTestSplit(rawData, 0.50)
	cls.Fit(trainData)

	//Calculates the Euclidean distance and returns the most popular label
	predictions, err := cls.Predict(testData)
	if err != nil {
		panic(err)
	}
	if (verbose) {
		fmt.Println(predictions)
	}

	// Prints precision/recall metrics
	confusionMat,
	err := evaluation.GetConfusionMatrix(testData, predictions)
	if err != nil {
		panic(fmt.Sprintf("Unable to get confusion matrix: %s", err.Error()))
	}
	if (verbose) {
		fmt.Println(evaluation.GetSummary(confusionMat))
	}
	return evaluation.GetAccuracy(confusionMat)*100, evaluation.GetMicroPrecision(confusionMat), evaluation.GetMacroPrecision(confusionMat)
}
