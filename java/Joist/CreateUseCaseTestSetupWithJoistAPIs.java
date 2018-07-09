
public class CreateUseCaseTestSetupWithJoistAPIs {

	public static void main(String[] args) {

		Joist a = new Joist(true, "");
		int x = a.getApplication(""); 
		System.out.printf("Got Application %d%nDone",x);
		a.insertArble("UseCaseApplicationFibonacci", 1);
		a.insertRoleFeatureReason(1, "Developer", "A BDD Test Framework", "I can evaluate how much value I add", 1000.0 );
		a.insertArble("FibonacciFunction", 1);
		a.insertRoleFeatureReason(2, "Developer", "Fibonacci function accepting one sequence number and returning the corresponding Fibonacci #", "I can yield Fibonacci numbers", 500.0 );
		a.insertArble("AddFunction", 1);
		a.insertRoleFeatureReason(3, "Developer", "Add function accepting two numbers and returning the sum", "I can add Fibonacci #s", 500.0 );
		a.insertBranch(1, 2);
    	//testrun = a.insertScenarioBatch("FibonacciApplication");
		a.insertArble("TestFibonacciFunction", 2);
		a.insertBranch(2, 4);
		a.insertScenario("Test first fibonacci", 4, 1);
		a.insertScenarioOutlet(1, 1, "Input", "Int", 1, "1");
		a.insertScenarioOutlet(1, 1, "ExpOut", "Int", 0, "1");
		
		a.insertScenario("Test second fibonacci", 4, 1);
		a.insertScenarioOutlet(1, 2, "Input", "Int", 1, "2");
		a.insertScenarioOutlet(1, 2, "ExpOut", "Int", 0, "1");
		
		a.insertScenario("Test third fibonacci", 4, 1);
		a.insertScenarioOutlet(1, 3, "Input", "Int", 1, "3");
		a.insertScenarioOutlet(1, 3, "ExpOut", "Int", 0, "2");
		
		a.insertScenario("Test third fibonacci", 4, 1);
		a.insertScenarioOutlet(1, 4, "Input", "Int", 1, "4");
		a.insertScenarioOutlet(1, 4, "ExpOut", "Int", 0, "3");
		
		a.insertScenario("Test third fibonacci", 4, 1);
		a.insertScenarioOutlet(1, 5, "Input", "Int", 1, "5");
		a.insertScenarioOutlet(1, 5, "ExpOut", "Int", 0, "5");
		
		a.insertScenario("Test third fibonacci", 4, 1);
		a.insertScenarioOutlet(1, 6, "Input", "Int", 1, "6");
		a.insertScenarioOutlet(1, 6, "ExpOut", "Int", 0, "8");
		
		
		
		a.insertArble("TestAddFunction", 2);
		a.insertBranch(3, 5);
		a.insertScenario("Test Add two positives", 5, 1);
		a.insertScenarioOutlet(1, 7, "Inp1", "Int", 1, "1");
		a.insertScenarioOutlet(1, 7, "Inp2", "Int", 1, "1");
		a.insertScenarioOutlet(1, 7, "ExpOut", "Int", 0, "2");
		
		a.insertScenario("Test add negative and positive", 5, 1);
		a.insertScenarioOutlet(1, 8, "Inp1", "Int", 1, "-1");
		a.insertScenarioOutlet(1, 8, "Inp2", "Int", 1, "1");
		a.insertScenarioOutlet(1, 8, "ExpOut", "Int", 0, "0");
		
		a.insertScenario("Test add negative and negative", 5, 1);
		a.insertScenarioOutlet(1, 9, "Inp1", "Int", 1, "-11");
		a.insertScenarioOutlet(1, 9, "Inp2", "Int", 1, "-1");
		a.insertScenarioOutlet(1, 9, "ExpOut", "Int", 0, "-12");
		
		a.insertScenario("Test add negative and zero", 5, 1);
		a.insertScenarioOutlet(1, 10, "Inp1", "Int", 1, "-1");
		a.insertScenarioOutlet(1, 10, "Inp2", "Int", 1, "0");
		a.insertScenarioOutlet(1, 10, "ExpOut", "Int", 0, "-1");
		
		a.insertScenario("Test add positive and zero", 5, 1);
		a.insertScenarioOutlet(1, 11, "Inp1", "Int", 1, "1");
		a.insertScenarioOutlet(1, 11, "Inp2", "Int", 1, "0");
		a.insertScenarioOutlet(1, 11, "ExpOut", "Int", 0, "1");	
		
    	//System.out.printf("Row ID: %d%n", testrun);
    	System.out.println("Done");
	}

}
