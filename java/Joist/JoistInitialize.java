
public class JoistInitialize {
	public static void main(String[] args) 
	{
		Joist.buildJoistBase.createNewDatabase("test.db");
		
		Joist.buildJoistBase.createApplicationsTable();
		Joist.buildJoistBase.createArblesTable();
		Joist.buildJoistBase.createRoleFeatureReasonsTable();
		Joist.buildJoistBase.createBranchesTable();
		Joist.buildJoistBase.createScenarioBatchTable();
		Joist.buildJoistBase.createScenarios();
		Joist.buildJoistBase.createScenarioOutletsTable();
		Joist.buildJoistBase.createTestResultsTable();
		
	}
}
