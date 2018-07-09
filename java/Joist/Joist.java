import java.sql.Connection;
import java.sql.DatabaseMetaData;
import java.sql.DriverManager;
import java.sql.PreparedStatement;
import java.sql.ResultSet;
import java.sql.SQLException;
import java.sql.Statement;
import junit.framework.Assert;


// TODO future work:
// api integration with github, change control for continuous deployment.integration
// branch down to code coverage, does a test have full code coverage?
// 
// interlock from feature to pseudocode to code in IDE to find wasted code
// and make metrics on the code base for a feature tree pathx`
//
//

public class Joist {

	public static class buildJoistBase {
		public static void createNewDatabase(String fileName) {

			String url = "jdbc:sqlite:C:/Users/Richard Pendrake/eclipse-workspace/Joist/" + fileName;

			try (Connection conn = DriverManager.getConnection(url)) {
				if (conn != null) {
					DatabaseMetaData meta = conn.getMetaData();
					System.out.println("The driver name is " + meta.getDriverName());
					System.out.println("A new database has been created.");
					System.out.println(url);
				}

			} catch (SQLException e) {
				System.out.println(e.getMessage());
			}
		}

		public static void createScenarioBatchTable() {
			// SQLite connection string
			String url = "jdbc:sqlite:C:/Users/Richard Pendrake/eclipse-workspace/Joist/" + "test.db";

			// SQL statement for creating a new table
			String sql = "CREATE TABLE IF NOT EXISTS ScenarioBatches (\n" + "	ScenarioBatchID integer,\n"
					+ "	ApplicationId integer,\n" + "	BatchBenefit integer,\n" + "	StartTime text,\n"
					+ " PRIMARY KEY (ScenarioBatchID)\n" + ");";

			try (Connection conn = DriverManager.getConnection(url); Statement stmt = conn.createStatement()) {
				// create a new table
				stmt.execute(sql);
				System.out.println("Created table: ScenarioBatches.");
			} catch (SQLException e) {
				System.out.println(e.getMessage());
			}
		}

		public static void createScenarios() {
			// SQLite connection string
			String url = "jdbc:sqlite:C:/Users/Richard Pendrake/eclipse-workspace/Joist/" + "test.db";

			// SQL statement for creating a new table
			String sql = "CREATE TABLE IF NOT EXISTS Scenarios (\n" + "	ScenarioId integer,\n"
					+ "	ScenarioName text,\n" + "	ArbleId integer,\n" + "	ApplicationID integer,\n"
					+ " PRIMARY KEY (ScenarioId)\n" + ");";

			try (Connection conn = DriverManager.getConnection(url); Statement stmt = conn.createStatement()) {
				// create a new table
				stmt.execute(sql);
				System.out.println("Created table: Scenarios.");
			} catch (SQLException e) {
				System.out.println(e.getMessage());
			}
		}

		public static void createScenarioOutletsTable() {
			// SQLite connection string
			String url = "jdbc:sqlite:C:/Users/Richard Pendrake/eclipse-workspace/Joist/" + "test.db";

			// SQL statement for creating a new table
			String sql = "CREATE TABLE IF NOT EXISTS ScenarioOutlets (\n" + "	OutletId integer,\n"
					+ "	ScenarioId integer,\n" + "	ParamName text NOT NULL,\n" + "	DataType text,\n"
					+ "	OutletType integer,\n" + " value text,\n" + " PRIMARY KEY (OutletId)\n" + ");";

			try (Connection conn = DriverManager.getConnection(url); Statement stmt = conn.createStatement()) {
				// create a new table
				stmt.execute(sql);
				System.out.println("Created table: ScenarioOutlets.");
			} catch (SQLException e) {
				System.out.println(e.getMessage());
			}
		}

		public static void createTestResultsTable() {
			// SQLite connection string
			String url = "jdbc:sqlite:C:/Users/Richard Pendrake/eclipse-workspace/Joist/" + "test.db";

			// SQL statement for creating a new table
			String sql = "CREATE TABLE IF NOT EXISTS TestResults (\n" 
			+ "	ResultId integer,\n"
					+ "	ScenarioBatchID integer,\n" 
			+ "	ScenarioId integer NOT NULL,\n" 
					//+ "	Value text\n"
					+ "	ResultTypeId integer,\n" 
					+ " PRIMARY KEY (ResultId)\n"
					+ ");";

			try (Connection conn = DriverManager.getConnection(url); Statement stmt = conn.createStatement()) {
				// create a new table
				stmt.execute(sql);
				System.out.println("Created table: TestResults.");
			} catch (SQLException e) {
				System.out.println(e.getMessage());
			}
		}
		
		public static void createApplicationsTable() {
			// SQLite connection string
			String url = "jdbc:sqlite:C:/Users/Richard Pendrake/eclipse-workspace/Joist/" + "test.db";

			// SQL statement for creating a new table
			String sql = "CREATE TABLE IF NOT EXISTS Applications (\n" + "	ApplicationId integer,\n"
					+ "	ApplicationName text,\n" + " PRIMARY KEY (ApplicationId)\n" + ");";

			try (Connection conn = DriverManager.getConnection(url); Statement stmt = conn.createStatement()) {
				// create a new table
				stmt.execute(sql);
				System.out.println("Created table: Applications.");
			} catch (SQLException e) {
				System.out.println(e.getMessage());
			}
		}

		public static void createArblesTable() {
			// SQLite connection string
			String url = "jdbc:sqlite:C:/Users/Richard Pendrake/eclipse-workspace/Joist/" + "test.db";

			// SQL statement for creating a new table
			String sql = "CREATE TABLE IF NOT EXISTS Arbles (\n" + "	ArbleID integer,\n" + "	Name text,\n"
					+ " ArbleType text,\n" + " PRIMARY KEY (ArbleID)\n" + ");";

			try (Connection conn = DriverManager.getConnection(url); Statement stmt = conn.createStatement()) {
				// create a new table
				stmt.execute(sql);
				System.out.println("Created table: Arbles.");
			} catch (SQLException e) {
				System.out.println(e.getMessage());
			}
		}

		public static void createRoleFeatureReasonsTable() {
			// SQLite connection string
			String url = "jdbc:sqlite:C:/Users/Richard Pendrake/eclipse-workspace/Joist/" + "test.db";

			// SQL statement for creating a new table
			String sql = "CREATE TABLE IF NOT EXISTS RoleFeatureReasons (\n" + "	RFRId integer,\n"
					+ "	ArbleId integer,\n" + "	AsA text,\n" + "	IWant text NOT NULL,\n" + " SoThat text,\n"
					+ " Benefit double,\n" + " PRIMARY KEY (RFRId)\n" + ");";

			try (Connection conn = DriverManager.getConnection(url); Statement stmt = conn.createStatement()) {
				// create a new table
				stmt.execute(sql);
				System.out.println("Created table: RoleFeatureReasons.");
			} catch (SQLException e) {
				System.out.println(e.getMessage());
			}
		}

		public static void createBranchesTable() {
			// SQLite connection string
			String url = "jdbc:sqlite:C:/Users/Richard Pendrake/eclipse-workspace/Joist/" + "test.db";

			// SQL statement for creating a new table
			String sql = "CREATE TABLE IF NOT EXISTS Branches (\n" + "	BranchID integer,\n" + "	RFRId integer,\n"
					+ "	ChildArbleID integer NOT NULL,\n" + " PRIMARY KEY (BranchID)\n" + ");";

			try (Connection conn = DriverManager.getConnection(url); Statement stmt = conn.createStatement()) {
				// create a new table
				stmt.execute(sql);
				System.out.println("Created table: Branches.");
			} catch (SQLException e) {
				System.out.println(e.getMessage());
			}
		}
	}

	protected static boolean isEquals(Object expected, Object actual) {
		return expected.equals(actual);
	}


	@SuppressWarnings("deprecation")
	public static void assertEqualsJoist(Object expected, Object actual, int testrun, int scenarioid) {
		if (isEquals(expected, actual)) {
			// update test to green
			// if all tests for feature have passed, do this
			System.out.println(expected);
			System.out.println(actual);
			updateScenarioBatchBenefit(testrun, 12.0);
			insertTestResults(testrun, scenarioid, 1); //green 
			Assert.assertEquals(expected, actual);
		} else {
			// update test to red
			updateScenarioBatchBenefit(testrun, 0.0);
			insertTestResults(testrun, scenarioid, 0); //red 
			Assert.fail();
		}

	}

	boolean forceRGR = true;
	String joistName = "";
	int testrun = 0;

	public Joist(boolean forceRGR, String joistName) {
		this.forceRGR = forceRGR;
		this.joistName = joistName;
		this.testrun = 0;
		this.insertApplication(joistName);
	}

	// get rgr force status
	public boolean getForceRGR() {
		return this.forceRGR;
	}

	// If force rgr then everything must be green before getting a new never green
	// case
	// turn on rgr force
	public void setForceRGROn() {
		this.forceRGR = true;
	}

	// If force rgr then everything must be green before getting a new never green
	// case
	// turn off rgr force
	public void setForceRGROff() {
		this.forceRGR = false;
	}

	private static Connection connect() {
		// SQLite connection string
		String url = "jdbc:sqlite:C:/Users/Richard Pendrake/eclipse-workspace/Joist/" + "test.db";
		Connection conn = null;
		try {
			conn = DriverManager.getConnection(url);
		} catch (SQLException e) {
			System.out.println(e.getMessage());
		}
		return conn;
	}

	public static int getApplication(String Name) {
		String sql = "select ApplicationId from Applications where ApplicationName = ?";
		int y = 0;
		try (Connection conn = connect(); PreparedStatement pstmt = conn.prepareStatement(sql)) {
			pstmt.setString(1, Name);
			ResultSet rs = pstmt.executeQuery();
			while (rs.next()) {
				y = rs.getInt("ApplicationId");
			}
			return y;
		} catch (SQLException e) {
			System.out.println(e.getMessage());
			return 0;
		}
	}

	// create an application in the database
	public void insertApplication(String Name) {
		int y = getApplication(Name);
		if (y >= 1) {
			System.out.printf("Welcome back to %s %d: %n", Name, y);
		} else if (Name != "") {
			String sql = "INSERT INTO Applications(ApplicationName) VALUES(?)";
			System.out.printf("Trying SQL: %s%n", sql);
			try (Connection conn = this.connect(); PreparedStatement pstmt = conn.prepareStatement(sql)) {
				pstmt.setString(1, Name);
				pstmt.executeUpdate();
				System.out.printf("Completed SQL: %s%n", sql);
			} catch (SQLException e) {
				System.out.println(e.getMessage());
			}
		}
	}

	// create an arble in the database
	public void insertArble(String Name, int Type) {
		String sql = "INSERT INTO Arbles(name,ArbleType) VALUES(?,?)";

		try (Connection conn = this.connect(); PreparedStatement pstmt = conn.prepareStatement(sql)) {
			pstmt.setString(1, Name);
			pstmt.setInt(2, Type);
			pstmt.executeUpdate();
			System.out.printf("Completed SQL: %s%n", sql);
		} catch (SQLException e) {
			System.out.println(e.getMessage());
		}
	}

	// create a RoleFeatureReason in the database
	public void insertRoleFeatureReason(int ArbleID, String AsA, String IWant, String SoThat, double Benefit) {
		String sql = "INSERT INTO RoleFeatureReasons(ArbleID,AsA, IWant, SoThat,Benefit) VALUES(?,?,?,?,?)";

		try (Connection conn = this.connect(); PreparedStatement pstmt = conn.prepareStatement(sql)) {
			pstmt.setInt(1, ArbleID);
			pstmt.setString(2, AsA);
			pstmt.setString(3, IWant);
			pstmt.setString(4, SoThat);
			pstmt.setDouble(5, Benefit);
			pstmt.executeUpdate();
			System.out.printf("Completed SQL: %s%n", sql);
		} catch (SQLException e) {
			System.out.println(e.getMessage());
		}
	}

	// create a ScenarioBatch in the database
	public int insertScenarioBatch(int ApplicationId) {
		String sql = "INSERT INTO ScenarioBatches(ApplicationId,BatchBenefit,StartTime) VALUES(?,?,?)";
		ResultSet x;
		Double StartBenefit = 0.0;
		String NowTime = "2018-07-08";
		try (Connection conn = this.connect(); PreparedStatement pstmt = conn.prepareStatement(sql)) {
			pstmt.setInt(1, ApplicationId);
			pstmt.setDouble(2, StartBenefit);
			pstmt.setString(3, NowTime);
			pstmt.executeUpdate();
			// System.out.printf("Completed SQL: %s%n", sql);
			x = pstmt.getGeneratedKeys();
			x.next();
			return x.getInt(1);
		} catch (SQLException e) {
			System.out.println(e.getMessage());
			return 0;
		}
	}

	// create a ScenarioOutlets in the database
	public void insertScenarioOutlet(int ApplicationId, int ScenarioId, String ParamName, String datatype,
			int outlettype, String value) {
		String sql = "INSERT INTO ScenarioOutlets(ScenarioId,ParamName,DataType,OutletType, value) VALUES(?,?,?,?,?)";
		ResultSet x;
		try (Connection conn = this.connect(); PreparedStatement pstmt = conn.prepareStatement(sql)) {
			pstmt.setInt(1, ScenarioId);
			pstmt.setString(2, ParamName);
			pstmt.setString(3, datatype);
			pstmt.setInt(4, outlettype);
			pstmt.setString(5, value);
			pstmt.executeUpdate();
			System.out.printf("Completed SQL: %s%n", sql);
		} catch (SQLException e) {
			System.out.println(e.getMessage());
		}
	}

	// create a ScenarioOutlets in the database
	public void insertScenario(String ScenarioName, int ArbleId, int ApplicationId) {
		String sql = "INSERT INTO Scenarios(ScenarioName,ArbleId,ApplicationId) VALUES(?,?,?)";
		ResultSet x;
		try (Connection conn = this.connect(); PreparedStatement pstmt = conn.prepareStatement(sql)) {
			pstmt.setString(1, ScenarioName);
			pstmt.setInt(2, ArbleId);
			pstmt.setInt(3, ApplicationId);
			pstmt.executeUpdate();
			System.out.printf("Completed SQL: %s%n", sql);
		} catch (SQLException e) {
			System.out.println(e.getMessage());
		}
	}
	
	// create a ScenarioOutlets in the database
	public static void insertTestResults(int ScenarioBatchId, int ScenarioId, int ResulttypeId) {
		System.out.println("In insertTestReults");
		String sql = "INSERT INTO TestResults(ScenarioBatchId,ScenarioId,ResultTypeId) VALUES(?,?,?)";
		ResultSet x;
		try (Connection conn = connect(); PreparedStatement pstmt = conn.prepareStatement(sql)) {
			pstmt.setInt(1, ScenarioBatchId);
			pstmt.setInt(2, ScenarioId);
			pstmt.setInt(3, ResulttypeId);
			pstmt.executeUpdate();
			System.out.printf("Completed SQL: %s%n", sql);
		} catch (SQLException e) {
			System.out.println(e.getMessage());
		}
	}

	// create a ScenarioBatch in the database
	public static void updateScenarioBatchBenefit(int ID, Double IncBenefit) {
		String sql = "UPDATE ScenarioBatches set BatchBenefit = BatchBenefit + ? where ScenarioBatchID = ?";
		try (Connection conn = connect(); PreparedStatement pstmt = conn.prepareStatement(sql)) {
			pstmt.setDouble(1, IncBenefit);
			pstmt.setInt(2, ID);
			pstmt.executeUpdate();
			// System.out.printf("Completed SQL: %s for %d%n", sql, ID);
		} catch (SQLException e) {
			System.out.println(e.getMessage());
		}
	}

	// create a Branch in the database
	public void insertBranch(int RFRId, int ChildArbleID) {
		String sql = "INSERT INTO Branches(RFRId,ChildArbleID) VALUES(?,?)";

		try (Connection conn = this.connect(); PreparedStatement pstmt = conn.prepareStatement(sql)) {
			pstmt.setInt(1, RFRId);
			pstmt.setInt(2, ChildArbleID);
			pstmt.executeUpdate();
			System.out.printf("Completed SQL: %s%n", sql);
		} catch (SQLException e) {
			System.out.println(e.getMessage());
		}
	}

	// get arble if rgr is enabled which is available for testing
	// use logic: get one new red row max
	// do not get any new red rows if stale reds are available, just get them
	// do not return anything if new red is not available and stale red is not
	// avaialbe
	// if forcergr is not enabled get all red tests
	// this should replace or be used in getjoist
	public void getarble() {
		;
		// get arble data
	}

	// get business value of a arble
	public int findValueof(int indexarble) {
		return 0;
	}

	// find all red tests and outputthem
	public void showRedTests() {
		;
	}

	// ???
	public int getValueof(String valueOf) {
		if (valueOf == "Red") {
			return 0;
		}
		if (valueOf == "Green") {
			return 1;
		}
		return 0;
	}

	// finds items not joined in
	public int findZeroChildrenRFR() {
		return 1;
	}

	// generate to do from features without all green tests [or with no tests]
	// ranked by values:
	// test cases needed entries
	// development to get to green entries -- rgr force on shows asterisk for
	// items pending and visible to developers
	public int findRedStatusTests(String kindofred) {
		if ((kindofred == "New") || (kindofred == "All")) { // red cases created and never green
			return 0;
		}
		if ((kindofred == "Stale") || (kindofred == "All")) { // red cases which were green
			return 0;
		}
		return 0;
	}

	public int getOrderedTodoList() {
		return findZeroChildrenRFR() + findRedStatusTests("RED");
	}

	public int lastTestValueReport() {
		// when a test run completes record value added
		// and lost by tests and final value proven with tests
		return 0;
	}

	public int cloneTests() {
		return 0;
	}

	public int exportTests() {
		// json or xml or csv
		return 0;
	}

	public static String parseTestCode(String X, String key) {
		String delims = "[;]+";
		String[] tokens = X.split(delims);
		for (String s : tokens) {
			String delims2 = "[=]";
			String[] keyvalue = s.split(delims2);
			if (keyvalue[0].equals(key)) {
				return keyvalue[1];
			}
		}
		return null;
	}


	// TODO make dynamic array dimensions
    //https://stackoverflow.com/questions/14082004/create-multiple-parameter-sets-in-one-parameterized-class-junit
	private static Object[][] returnRows(String casename) {
		// TODO given when then
		// given case name
		// when inputvalues = [input values]
		// then outputvalues [ output values]
		Object[][] x = readRows(1);
		return x;
	}

	// TODO heart of test case retrieval
	// TODO If force rgr then everything must be green before getting a new never green
	//		if forcergr is true then check [iseverything green?]
		// yes: pull all tests which have been tested + one never tested
		// no: pull all tests which have been tested 
		// if nothing has been tested
		// pull one test which has not been tested
    //https://stackoverflow.com/questions/14082004/create-multiple-parameter-sets-in-one-parameterized-class-junit
	public static Object[][] readRows(int ApplicationId) {
		Object[][] o = new Object[11][2];
		int rowcount = 0;
		int columncount = 0;
		int sid = 0;
		String sql = " select distinct s.scenarioid, ar.name, s.scenarioname longname \n"
				+ "from Arbles ar, Scenarios s, ScenarioOutlets so where \n"
				+ "ar.ArbleId = s.ArbleId and s.scenarioid = so.scenarioid \n" + " and s.ApplicationId = ?";
		String y = "";
		String yx = "";
		//create outer list
		try (Connection conn = connect(); PreparedStatement pstmt = conn.prepareStatement(sql)) {
			pstmt.setInt(1, ApplicationId);
			ResultSet rs = pstmt.executeQuery();
			while (rs.next()) {
				sid = Integer.parseInt(rs.getString("scenarioid"));
				yx = rs.getString("name");
				y = rs.getString("longname");
				String sql2 = " select so.ParamName||'='||ifnull(so.value,-999) longname2 \n"
						+ "from Arbles ar, Scenarios s, ScenarioOutlets so where \n"
						+ "ar.ArbleId = s.ArbleId and s.scenarioid = so.scenarioid \n"
						+ " and s.ApplicationId = ? and s.scenarioid = ?";
				String y2 = "";
				try (Connection conn2 = connect(); PreparedStatement pstmt2 = conn2.prepareStatement(sql2)) {
					pstmt2.setInt(1, ApplicationId);
					pstmt2.setInt(2, sid);
					ResultSet rs2 = pstmt2.executeQuery();
					while (rs2.next()) {
						y2 = rs2.getString("longname2");
						y = y + ";" + y2;
					}
					y=y+";JoistScenarioId="+sid;
					o[rowcount][0] = yx;
					o[rowcount][1] = y;
					//create two item list, add it to outer list
				} catch (SQLException e) {
				}
				rowcount += 1;
			}
		} catch (SQLException e) {
			System.out.println(e.getMessage());
		}
		return o;
	}


	public static Object[][] getJoist(String casename) {
		return returnRows(casename);
	}

}
