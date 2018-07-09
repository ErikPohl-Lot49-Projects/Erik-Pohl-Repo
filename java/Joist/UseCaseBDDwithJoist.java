import static org.junit.Assert.*;
 
import java.util.Arrays;

import org.junit.Assume;
import org.junit.BeforeClass;
import org.junit.Test;
import org.junit.runner.RunWith;
import org.junit.runners.Parameterized;
import org.junit.runners.Parameterized.Parameters;

@RunWith(Parameterized.class)
public class UseCaseBDDwithJoist {
	
	private static String applicationname = "FibonacciApplication";
    private String TestCase;
    private String TestCode;
    private static int testrun =0;
    private static int applicationid= 0;
	
		// retrieve parameters from joist using some identifiers
        @Parameters(name = "{index}: Test type {0} Testing scenario {1}")
        public static Iterable<Object[]> data() {
        		String testcase = "sample"; 
                return Arrays.asList(				
                                Joist.getJoist(testcase)
                                );
        }

       //constructor sets up generic test case
        public UseCaseBDDwithJoist(String testcase, String testcode)
        {
        		TestCase = testcase;
        		TestCode = testcode;
        }
        
        @BeforeClass public static void setUpTests() {
        	Joist x = new Joist(true, applicationname);
        	applicationid = x.getApplication(applicationname);
        	testrun = x.insertScenarioBatch(applicationid);        	
        	System.out.printf("Beginning to Joist the Junit testing of Application %s [%d].",applicationname,applicationid);
        }
       
        @Test
        public void executeTestFibwithJoist()
        {               	
                Assume.assumeTrue(TestCase.equals( "TestFibonacciFunction"));
                
                int fInput = Integer.parseInt(Joist.parseTestCode(TestCode, "Input"));
                int fExpected = Integer.parseInt(Joist.parseTestCode(TestCode, "ExpOut"));
                int scenarioid = Integer.parseInt(Joist.parseTestCode(TestCode, "JoistScenarioId"));
                int z = UseCase.fibonacci(fInput);
                Joist.assertEqualsJoist(fExpected, z, testrun, scenarioid);
        }
        
        @Test
        public void executeTestAddwithJoist()
        {      
                boolean testresult;
                Assume.assumeTrue(TestCase.equals( "TestAddFunction"));

                int fInp1 = Integer.parseInt(Joist.parseTestCode(TestCode, "Inp1"));
                int fInp2 = Integer.parseInt(Joist.parseTestCode(TestCode, "Inp2"));
                int fExpected = Integer.parseInt(Joist.parseTestCode(TestCode, "ExpOut"));
                int scenarioid = Integer.parseInt(Joist.parseTestCode(TestCode, "JoistScenarioId"));

                int z = UseCase.add(fInp1,fInp2);
                Joist.assertEqualsJoist(fExpected, z, testrun, scenarioid);
        }        
}