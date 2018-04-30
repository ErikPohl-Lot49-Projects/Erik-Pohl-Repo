package countenance_book_perceptron_test

import (
	"testing"
	"fmt"
	cbp "Paracme/oxford_cambridgelytica/countenance_book_perceptron"
) 

//originally had this in the same folder as countenance_book_perceptron which is a no-no
// and which caused confusion and misleading error messages

// name after Test cannot start with lowercase letter
func TestDivisionTest(t *testing.T) {
   t.Log("Testing if 4 divided by 2 is equal to 2")
   if 4/2 != 2 {
      t.Fail()
   }
}

//name after Test cannot start with lowercase letter
func TestEvaluate_humansAccuracy(t *testing.T) {
   var accuracy, microprecision, macroprecision float64
   
   minimum_accuracy := 70.0 //shorthand to define a new var as a float
   t.Log("Testing if Evaluate_humans() exceeds minimum accuracy of this percent", minimum_accuracy)
   accuracy, microprecision, macroprecision = cbp.Evaluate_humans(false) 
   if accuracy < minimum_accuracy {
      t.Error("Minimum accuracy is set to : ", minimum_accuracy)
	  t.Error("Actual accuracy is         : ", accuracy)
      t.Error("Expected Evaluate_humans() to have an actual accuracy exceeding the minimum accuracy")
      t.Fail()
   } else {
      t.Log("Evaluate_humans was successfully accurate at this accuracy: ",accuracy)
	  t.Log("Microprecision: ",microprecision) // had to insert this code to make it work or else it failed for unused variables
	  t.Log("Macroprecision: ",macroprecision)
   }
}

//name after Test cannot start with lowercase letter
func TestEvaluate_humansMicroprecision(t *testing.T) {
   var accuracy, microprecision, macroprecision float64
   
   minimum_microprecision := 0.10 //shorthand to define a new var as a float
   t.Log("Testing if Evaluate_humans() exceeds minimum microprecision of this percent", minimum_microprecision)
   accuracy, microprecision, macroprecision = cbp.Evaluate_humans(false) 
   if microprecision < minimum_microprecision {
      t.Error("Minimum microprecision is set to : ", minimum_microprecision)
	  t.Error("Actual microprecision is         : ", microprecision)
      t.Error("Expected Evaluate_humans() to have an actual microprecision exceeding the minimum microprecision")
      t.Fail()
   } else {
   	  t.Log("Microprecision: ",accuracy) // had to insert this code to make it work or else it failed for unused variables
      t.Log("Evaluate_humans was successfully microprecise at this microprecision: ",microprecision)
	  t.Log("Macroprecision: ",macroprecision)
   }
}

func ExampleEvaluate_humans() {
   var accuracy, microprecision, macroprecision float64
   accuracy,microprecision,macroprecision = cbp.Evaluate_humans(false)
   fmt.Println(fmt.Sprintf("%.0f", accuracy))
   fmt.Println(fmt.Sprintf("%.1g", microprecision))
   fmt.Println(fmt.Sprintf("%.1g", macroprecision))
   // Output: 
   // 71
   // 0.7
   // 0.7
}

