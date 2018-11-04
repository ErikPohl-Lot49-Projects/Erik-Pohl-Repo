# PyJamb

I am mostly done with the code, but it is not ready for review.

This is a cleaned-up port of my original work in Java for a JUnit extension called Joist.
 
The extension allows non-techie users to build a human-language description of functionality for applications  
as the requirements are developed.

The features form a hierarchical tree, breaking functionality down from an overall functionality description of the application down to its lowest-most granularity feature descriptions.  All of the nodes which define functionality have a business value.  

All branches end in end in human language descriptions of test cases.

### This database is used by a PyUnit extension which records test results and can generate, based on test results, functional test coverage, and business value:

a) A to do list of what the engineering team should work on next : the most valuable untested functionality and that functionality which has failed tests associated with it, ranked by overall business value delivered by testing it

b) An assessment of total business value which has been tested versus total business value with failed tests or which does not have tests associated with it.

c) A history of test results which I would intend to link with Version Control APIs (example: GitHub)

d) Self-documenting and traceability: for each test case, you can see all the levels of functionality abstracted above it in a tree-branch leading up to the overall System Under Test-- meaning that you know from the least granular to the most granular at any time why you are building a test case, what it tests, and what business value it returns-- the traceability is enforced through the tree structure

e) A flag can be enabled to enforce TDD -- meaning a piece of functionality is not considered complete until it has green tests, and that developers are expected to iterate through Red, Green, and Refactor.




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
