package CountenanceBookPerceptronTest // physical file name still had to end in _test

import (
	"testing"
	cbp "Paracme/OxfordCambridgelytica/CountenanceBookPerceptron"
	"fmt"
)

//const HeterogeneousDataset = "C:/Users/Richard Pendrake/MLDatasets/countenance_book_likes_variety.csv"
const HeterogeneousDataset = "C:/Users/Richard Pendrake/MLDatasets/countenance_book_likes_variety.csv"
const UnanimousDataset = "C:/Users/Richard Pendrake/MLDatasets/countenance_book_likes_unanimity.csv"

//originally had this in the same folder as countenance_book_perceptron which is a no-no
// and which caused confusion and misleading error messages

// name after Test cannot start with lowercase letter -- i.e. Camelcase is good
func TestDivisionTest(t *testing.T) {
	t.Log("Testing if 4 divided by 2 is equal to 2")
	if 4/2 != 2 {
		t.Fail()
	}
}

//name after Test cannot start with lowercase letter
func TestEvaluateHumansAccuracy(t *testing.T) {
	var accuracy,
	microprecision,
	macroprecision float64

	minimum_accuracy := 70.0 //shorthand to define a new var as a float
	t.Log("Testing if EvaluateHumans() exceeds minimum accuracy of this percent", minimum_accuracy)
	accuracy,
		microprecision,
		macroprecision = cbp.EvaluateHumans(HeterogeneousDataset, false)
	if accuracy < minimum_accuracy {
		t.Error("Minimum accuracy is set to : ", minimum_accuracy)
		t.Error("Actual accuracy is         : ", accuracy)
		t.Error("Expected EvaluateHumans() to have an actual accuracy exceeding the minimum accuracy")
		t.Fail()
	} else {
		t.Log("EvaluateHumans was successfully accurate at this accuracy: ", accuracy)
		t.Log("Microprecision: ", microprecision) // had to insert this code to make it work or else it failed for unused variables
		t.Log("Macroprecision: ", macroprecision)
	}
}

//name after Test cannot start with lowercase letter
func TestEvaluateHumansMicroprecision(t *testing.T) {
	var accuracy,
	microprecision,
	macroprecision float64

	minimum_microprecision := 0.10 //shorthand to define a new var as a float
	t.Log("Testing if EvaluateHumans() exceeds minimum microprecision of this percent", minimum_microprecision)
	accuracy,
		microprecision,
		macroprecision = cbp.EvaluateHumans(HeterogeneousDataset, false)
	if microprecision < minimum_microprecision {
		t.Error("Minimum microprecision is set to : ", minimum_microprecision)
		t.Error("Actual microprecision is         : ", microprecision)
		t.Error("Expected EvaluateHumans() to have an actual microprecision exceeding the minimum microprecision")
		t.Fail()
	} else {
		t.Log("Microprecision: ", accuracy) // had to insert this code to make it work or else it failed for unused variables
		t.Log("EvaluateHumans was successfully microprecise at this microprecision: ", microprecision)
		t.Log("Macroprecision: ", macroprecision)
	}
}

func ExampleEvaluateHumans() {
	var accuracy,
	microprecision,
	macroprecision float64

	accuracy,
		microprecision,
		macroprecision = cbp.EvaluateHumans(HeterogeneousDataset, false)
	fmt.Println(fmt.Sprintf("%.0f", accuracy))
	fmt.Println(fmt.Sprintf("%.1g", microprecision))
	fmt.Println(fmt.Sprintf("%.1g", macroprecision))
	// Output:
	// 71
	// 0.7
	// 0.7
}

