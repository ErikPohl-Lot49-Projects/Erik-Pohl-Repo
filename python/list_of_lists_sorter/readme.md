# Special note
You will also find a list_of_dicts_sorter class and a list_of_string_lists_sorter class along with the named list_of_lists_sorter class.

This enabled me to create a list_of_xs_sorter class which chooses between them and provides a common interface (only list of Xs with headers are compatible).

I intend to sharpen the pattern of the list_of_xs_sorter.

# List of lists sorter class

Python offers a graceful method to sort lists of lists.

Why gild the lily?

_Because the lily is there._  And because it teaches me things about a language I love.

This class adds to the sort method the following features:
1. Define sort fields using encapsulated methods to prevent explicitly creating lambda functions and using itemgetters.

2. Gracefully handle list of lists which have a single row column header as well as headerless list of lists.

3. Select sort fields with field headers or column positions.

4. Handle strings which represent dates in the sort as dates conditionally.


# Examples

#### Set up a list of lists with a header row
```
output_list_with_header = [
    ['zero', 'one', 'two', 'three', 'four', 'five', 'six'],
    [1, 2, 3, 7, 1, 7, '1-1-15'],
    [1, 2, 3, 7, 2, 6, '1-1-14'],
    ]
```
#### Establish list of lists sort object and then declare a header
```
sorter = list_of_list_sorter(output_list_with_header)
sorter.has_header = True
```
#### Add a sort field on the sixth column using a date conversion from string with a - delimiter 
```
sorter.add_sort_field_by_header_field_name('six', 'datestringdel-')
```
#### Perform the sort using these criteria
```
print(sorter.sort())
```

    [1, 2, 3, 7, 1, 7, '1-1-14'],
    [1, 2, 3, 7, 2, 6, '1-1-15']



# Future plans

1. Consider reasonable exception handling without stifling exceptions.
2. Lint the code. (Weekend of 11/17)
3. Other list of xs sorter classes are here, and I'd like to make my list_of_xs_sorter class more svelte using a design pattern
  
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
