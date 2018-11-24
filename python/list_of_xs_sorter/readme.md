# List of xs sorter class

This is a class which provides a common interface for many list of xs sorter classes.  It began with a list of lists sorter class.

# But why?

Python offers a graceful method to sort lists of lists and lists of other types.

Why gild the lily?

_Because the lily is there._  And because it teaches me things about a language I love.

This class adds to the sort method the following features:
1. Define sort fields using encapsulated methods to prevent explicitly creating lambda functions and using itemgetters.

2. Gracefully handle list of lists which have a single row column header as well as headerless list of lists.

3. Select sort fields with field headers or column positions.

4. Handle strings which represent dates in the sort as dates conditionally.


# Examples

See demo_usage.py for now!  This will be updated soon to reflect common usages.



# Future plans

- [ ] Consider reasonable exception handling without stifling exceptions.
- [ ] Lint the code. (Weekend of 11/24)
- [ ] Make the list_of_xs_sorter class more svelte using a design pattern.
- [x] Move demo usage code to one file and out of my list_of_xs_sorter class file.
- [x] Write "output as" methods for each individual sorter class to permit outputting as other list of x types.
- [ ] Better example cases for the readme

  
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
