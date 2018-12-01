# Semblance (was RestSemblance aka RestFul Testful aka DDRestTest)

## This is only a rough draft

### What it does:

It loads a series of endpoint mocked data from a pickle file.
It then feeds the endpoint mocked data to unit tests on a test case by test case basis: allowing multiple endpoints per case.

### What it doesn't do

* Instead of storing the business logic in a database as originally designed, it stores the business logic in a pickle file
* It does not contain expected results for test cases: the unittest file which utilizes Semblance will need to supply those
* Refactoring, refactoring, refactoring.  I look at this code and shake my head.  Everwhere there is opportunity to clean the code up!

### What it will eventually do

* It will eventually look cleaner and more clearly patterned
* I'm deciding whether or not to build in functionality here for mocked database reads, mocked file reads, etc.
* I like the database back-end concept, but for now am sticking with pickled dictionaries
* I'd like to entertain the notion of storing expected results in the test case definition in the pickle file (or db)

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
