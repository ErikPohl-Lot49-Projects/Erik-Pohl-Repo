# Semblance 

**Disclaimer: This is _not_ how I write classes and functions.  This is my Picasso-ing of a class for a particular effect.  I'm going to make it more Chuck Close than Picasso going forward.**

## A Use Case 

Your team has sketched out some process to utilize the company's brand-new Rest API endpoints:

* https://<i></i>www<i></i>&#46;par<i></i>acme&#46;com/<i></i>foo
* https://<i></i>www<i></i>&#46;par<i></i>acme&#46;com/<i></i>bar

You're ready to implement the new process you just designed, called Dead Parrot.  

Dead Parrot takes two parameters and adds them.
It then takes a key value from a request to the *foo* endpoint and a key value from the *bar* endpoint and adds those.
It multiples the two sums and returns that.

**The problem?**

_The APIs dependencies are not created yet.  They're behind schedule._

No worries... just get your QA team to fake results for the API calls to help you test Dead Parrot (your new process).  

*But wait!*

**How can we do it cleanly?**

The QA team can start building test cases immediately.  They set to work constructing a set of test cases for Dead Parrot.

They build a file containing the following for each test case:
* a test case name
* a list of positional argument values for the process test case
* a list of keyword arguments values for the process test case
* the endpoints your new process (Dead Parrot) will use, plus faked data for each endpoint for that test case

Meanwhile, your developers are building the Dead Parrot process itself.

By the time the developers are ready for a test case, QA has a list of them constructed, none of which took any coding at all.

The developers plug their Dead Parrot process into the test cases using a Semblance engine, and **wham!** your team's cycle of testing, resolution, refactoring has begun in earnest for all of the existing test cases.

Meanwhile, the QA team is adding more and more cases, independent of the code base.

## Origin Story

Every superhero needs an origin story, right?  Preferably one which establishes the motivation for that hero's mission!

![API Superhero](https://github.com/ErikPohl-Lot49-Projects/Erik-Pohl-Repo/blob/master/media/superhero.jpg "API Superhero")

There is no reason why you should ever hard-code faked get responses for testing a variety of REST API calls.

**_None._**

However, some people still do it :smiling_imp:. 

(I know of at least one who did it several months ago! :see_no_evil:)

That's why I made RestSemblance.  However, first, it was called DDRestTest, then RestFul Testful, finally RestSemblance.

Coming from an origin of hard-coded Rest API responses, it protects the business logic and the test engine by keeping them separate!

## How?

For now, you simply store test cases, each with any number of API endpoints to be mocked, in a dictionary pickle file.

You leverage Semblance to load the pickle file.

Then, you can iterate through your test cases, calling your API client function, and the results will be mocked for each endpoint in your unit tests -- like magic!

:sparkles: :sparkles: :sparkles: :sparkles: :sparkles: :sparkles: :sparkles: :sparkles:

It uses the concept of data driven development: an engine which cycles through a list of test cases in a data structure, instead of a series of individual test case procedures.

That lets us remove test case specifics from the unit testing engine, safely storing the test case specifications in a file whose only purpose is to describe test case data, nothing else :clipboard:.  

That is clean for the engine and clean for the test case data. :bulb:

Up next, obviously: create a front-end which will allow a non-technical user to create the JSON for the test cases pickle file.

## But wait!  Why did you switch from RestSemblance to Semblance mid-readme?  

There is a certain crisis of identity going on here.

I started out with RestSemblance, and now I'm wanting to expand this simple tool to handle other forms of mocked dependencies (file loads, function calls, etc.)

If I accomplish that, it will be called Semblance.  If I don't, I'll leave it as RestSemblance and make everything consistent.

## What it doesn't do

* Instead of storing the business logic in a database as originally designed, it stores the business logic in a pickle file
* It does not contain expected results for test cases: the unittest file which utilizes Semblance will need to supply those
* Refactoring, refactoring, refactoring.  I look at this code and shake my head.  Everwhere there is opportunity to clean the code up!

# There is a lot of work yet to be done here
## What it will eventually do

- [ ] It will eventually look cleaner and more clearly patterned
- [ ] I'm deciding whether or not to build in functionality here for mocked database reads, mocked file reads, etc.
- [ ] I like the database back-end concept, but for now am sticking with pickled dictionaries
- [x] I'd like to entertain the notion of storing expected results in the test case definition in the pickle file (or db)
- [ ] Front end to allow a non-technical user to modify and create API responses for each test case

## Important disclaimer

The code here does not yet represent work I'd submit for production code-review.  Standards differ, and I have worked within many different sets, helping to establish and build on them.

Here are some elements I expect to be able to provide, if needed:

- [ ] A complete regression test suite.
- [ ] Meaningful exceptions and exception-handling coverage.
- [ ] Adequate output to permit users to understand the results, assisting in the self-documenting nature of the code.
- [ ] Requirements documents, user-facing documents and presentations, and other documents consistent with Agile User Stories to add value.

## Getting Started

Download these files to corresponding folders under your Python src path.

## Prerequisites

I'll provide prereqs here.

## Installing

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
