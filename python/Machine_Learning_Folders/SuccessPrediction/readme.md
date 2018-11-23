# Machine Learning: Success Predictor

Code is underway and is not ready for GitHub.

Imagine you are a course provider.
You have a database of courses -- if instructors vary, a course has two primary keys: course and instructor.
For each course, you have a list of final grades which have been scrubbed for anonymity.  Student IDs are used, but they don't correspond to actual student ids which, if hacked, would reveal the students.
For each course and final grade, you have graded assignments and graded test results for the student.

Using this data, you can track a particular student's success against all of that student's courses and milestone course graded assignments and tests.

This code analyzes that data set to predict whether a student who has not taken a particular course or, within that course, a particular milestone graded assignment or graded test will succeed or fail at the course or milestone graded assignment or graded test.

I will make these assessments using sci-kit learn.  My best guess is that I will be using logistic regression for this task to anticipate granular success values or KNN to form a more binary understanding of success/failure.


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

Download these files to corresponding folders under your Python project folders.

### Prerequisites

I will list prereqs here.

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
 
* Thank you to the folks who inspired this.
