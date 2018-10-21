# RestfulTestful

I am mostly done with the code, but it is not ready for review.

This code provides classes for two key functions to automate Restful API testing.


# a) The test case database database development tool for which I will develop a web front end to permit non-developers to build cases.

This tool object provides methods to build and update RestfulTestful database table values:

i) Applications.  This is a humaan language description of the System Under Test

Columns:

AppId: Unique identifier for a System Under Test.

AppName: Human language name of the System Under Test.

AppDescription: Human language description of the System Under Test.

ii) Test Cases.  These are human language descriptions of test cases for the System Under Test.

Columns:

AppId: Joins to the System Under Test.

TestCaseId: Unique identifier for the test case.

TestCaseName: A user-friendly name of the test case.

TestCaseDescr: A human language description of the what the test case does.

iii) EndPoints.  These are one or many EndPoints to each Test Case.

AppId: Joins to the System Under Test.

TestCaseId: Joins to the Test Case.

EndPointId: Unique identifier for the endpoint.

EndPointURI: When the application code is called, this is the URI which will be used for this endpoint.

EndPointJSON: This is the JSON to return to the System Under Test in RestfulTestful for this endpoint for this test case.

iv) Expected results

This is in process.


# b) RestfulTestful

This object utilizes the database constructed in the former object.

This object generates mocked JSON results for a System Under Test based on entries in the database.

This object allows for certain cases:

a) suppose the System Under Test has multiple endpoints which need to be mocked

b) suppose you want to store all your regression test cases in a non-techie user-friendly database with a web-front end

c) suppose you want the code to simply iterate through all of the test cases in a way which utilizes the object and an App designation which moves the business logic of the test cases out of your code?



# Important disclaimer

The code here does not represent work I'd submit for production code-review.  Standards differ, and I have worked within many different
sets, helping to establish and build on them.

Here are some elements I expect to be able to provide, if needed:

a) A complete regression test suite.

b) Meaningful exceptions and exception-handling coverage.

c) Thoughtful, self-documenting, variable, method, and function names.

d) Adequate output to permit users to understand the results, assisting in the self-documenting nature of the code.

e) Actual docstring comments at all levels of the code.

f) Linting the code for PEP 8 standardization.

g) Requirements documents, user-facing documents and presentations, and other documents consistent with Agile User Stories to add value.

h) Commit statements which facilitate an understanding of code history.

## Getting Started

Download these files to corresponding folders under your Python src path.

### Prerequisites

I'll provide prereqs here.

### Installing

I will provide installation steps here.

## Running the tests

I will explain how to test the system here using the automated tests.

## Contributing

For now, I'd be excited to receive pull requests.  I don't have rules for contributing right now.

## Authors

* **Erik Pohl** - *Initial work* - 

Also see the list of github contributors.

## License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details

## Acknowledgments

* Thanks to everyone who has motivated me to learn more.
