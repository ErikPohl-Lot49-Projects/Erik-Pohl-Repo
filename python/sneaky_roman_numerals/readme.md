# Sneaky Roman Numerals


This is the product of a kata performed at a coding dojo during a Boston Software Crafter's meetup last night.
The challenge was to convert roman numerals to arabic **_without using mathematical operations on ints**_ _(multiplication on strings was fine for repeated concatenation)._

This is an on-going refactoring kata, so I will use it as a sandbox for refactoring.

# Up Next
- [x] Parameterize test cases
- [x] Add more test cases
- [x] Rethink variable names and function names
- [x] Reconsider data structures
- [x] Docsys and other comments

# Important disclaimer

The code here does not represent work I'd submit for production code-review.  Standards differ, and I have worked within many different
sets, helping to establish and build on them.

Here are some elements I expect to be able to provide, if needed:

- [x] Meaningful exceptions and exception-handling coverage.
- [x] Adequate output to permit users to understand the results, assisting in the self-documenting nature of the code.
- [x] Actual docstring comments at all levels of the code.
- [ ] Requirements documents, user-facing documents and presentations, and other documents consistent with Agile User Stories to add value.


## Getting Started

1. Retrieve files from the sneaky_roman_numerals repo folder.  
2. Perform the installation steps in the Installing section of this readme.

### Prerequisites

Sneaky Roman Numerals was developed in Python 3.7.  However, it should be backwards compatible into Python 3.6.  I have not tested it in earlier releases of Python 3. 

### Installing

Download these Python files into a folder which has access to Python 3.6 or higher:

* sneaky_roman_numerals.py
* test_sneaky_roman_numerals.py

This is not necessary, but is helpful:
* sneaky_roman_numerals_demo_usage.py

## Running the tests

Tests have been batched in one Python module.  To execute it, run this command from the command line in the folder in which the files are installed:
```
python -m unittest -v test_plural_roman_numerals.py
```

## Contributing

For now, I'd be excited to receive pull requests.  I don't have rules for contributing right now.

## Authors

* **Erik Pohl** - *Initial work* - 

Also see the list of github contributors.

## License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details

## Acknowledgments

* Thanks to everyone who has motivated me to learn more.
