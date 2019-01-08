# numerous_ants

This class allows a developer user to run a variety of algorithmic approaches multiple times each asynchronously to determine which one performs the best maintaining the same output for all inputs as a control algorithm.

![formicate](https://github.com/ErikPohl-Lot49-Projects/Erik-Pohl-Repo/blob/master/media/formicate.jpg "formicate")

It was inspired by a Dan Bader video in which a viewer asked him which of three or four if conditions were the most Pythonic/idiomatic.  I saw that at least one variation was missing, one which would perform much better.

Yet, I wanted to prove it.  
Proving it for a specific case was trivial.  

It was so trivial that I also wanted to make a tool to do the same in the future.  
Synchronous processing was simple.  

It was a good learning exercise to make it asynchronous.  I enjoy the thought of an army of myrmidons resolving a performance decision, a Pythonic episode of Black Mirror's "Hang The DJ" for performance comparisons.

There are probably a billion of performance comparison frameworks out there, but this is a start, just for practice, of my own.

This is really not much of anything, but it is good to have handy.

# Example usage

See demo usage file.

# Future work

- [ ] Implement multiprocessing 

# Important disclaimer

The code here does not represent work I'd submit for production code-review.  Standards differ, and I have worked within many different sets, helping to establish and build on them.

Here are some elements I expect to be able to provide, if needed:

- [ ] Apply this checklist to all new projects as step one
- [ ] A complete regression test suite in PyTest (until I can decide between that and unittest/Parameterized)
- [ ] Meaningful exceptions and exception-handling coverage.
- [ ] Thoughtful, self-documenting, variable, method, and function names.
- [ ] Adequate output to permit users to understand the results, assisting in the self-documenting nature of the code.
  - [ ] Specifically, would this benefit from comprehensive logging?
  - [ ] Would it benefit from a results page with stats to demonstrate accurate and complete results?
  - [ ] How do I want to manage output to stdout, stderr, file, etc?
  - [ ] How do comments and outputs help and assist one another without being redundant?
- [ ] Actual docstring comments at all levels of the code.
- [ ] Linting the code for PEP 8 standardization like PEP8 or Applying a PEP formatter to the code like Project Black.
- [ ] Requirements documents, user-facing documents and presentations, and other documents consistent with Agile User Stories to add value.
- [ ] Commit statements which facilitate an understanding of code history.
- [ ] Readme.md pages with more interesting usage of markdown which tell a code narrative. 
- [ ] For custom classes, create dunders as appropriate
- [ ] Make good decisions relating to
  - [ ] Exceptions versus return values
  - [ ] Using idiomatic Python versus clarity of code
  - [ ] Extend this list
  
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
