# List of Xs sorter class

This is a class which provides a common interface for many list of Xs sorter classes. 


<p align="center">
  <img src="https://github.com/ErikPohl-Lot49-Projects/Erik-Pohl-Repo/blob/master/media/arranged_by_order.png">
</p>
<p align="center">
(Some Xs which were sorted!)
</p>

It began with a list of lists sorter class.

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

#### Import the sorters
```
from list_of_lists_sorter import list_of_lists_sorter
from list_of_string_lists_sorter import list_of_string_lists_sorter
from list_of_xs_sorter import  list_of_xs_sorter
from list_of_dicts_sorter import list_of_dicts_sorter
```

#### Create a sample list of lists with a header list
```
output_list_with_header = [
    ['zero', 'one', 'two', 'three', 'four', 'five', 'six'],
    [1, 2, 3, 7, 1, 7, '1-1-15'],
    [1, 2, 3, 7, 2, 6, '1-1-14'],
    [1, 2, 3, 5, 3, 5, '1-1-13'],
    [1, 2, 3, 4, 4, 4, '1-1-12'],
    [1, 2, 3, 3, 5, 3, '1-1-11'],
    [1, 2, 3, 2, 6, 2, '1-1-10'],
    [1, 2, 3, 1, 7, 1, '1-1-18']
]
```
#### Sort it by header ('six') using a date sort with a dash
```
sorter = list_of_lists_sorter(output_list_with_header)
sorter.has_header = True
sorter.add_sort_field_by_header_field_name('six', 'datestringdel-')
print(sorter.sort())
```

#### Create a list of lists without a header list
```
output_list_without_header = [
    [1, 2, 3, 7, 1, 7, '1-1-15'],
    [1, 2, 3, 7, 2, 6, '1-1-14'],
    [1, 2, 3, 5, 3, 5, '1-1-13'],
    [1, 2, 3, 4, 4, 4, '1-1-12'],
    [1, 2, 3, 3, 5, 3, '1-1-11'],
    [1, 2, 3, 2, 6, 2, '1-1-10'],
    [1, 2, 3, 1, 7, 1, '1-1-18']
]
```

#### Now reset the sorter from the above example for sort fields by position and reverse sort using the headerless list of lists
```
sorter.clear_sort_fields()
sorter.add_sort_field_by_position(6, 'datestringdel-')
sorter.has_header = False
sorter.reverse_sort = True
sorter.list_of_lists =output_list_without_header
print(sorter.sort())
```

#### Reset the sorter and sort again by position, adding positions to sort in one multiple position designation
```
sorter.clear_sort_fields()
sorter.add_multiple_fields_by_position([(6, 'datestringdel-'), (4)])
sorter.has_header = False
sorter.reverse_sort = False
sorter.list_of_lists =output_list_without_header
print(sorter.sort())
```

#### Reset and sort the list of lists with a header by a different header column
```
sorter = list_of_lists_sorter(output_list_with_header)
sorter.has_header = True
sorter.add_sort_field_by_header_field_name('five')
print(sorter.sort())
```

#### more examples to come



# Future plans

- [ ] Consider reasonable exception handling without stifling exceptions.
- [x] Lint the code. (Weekend of 11/24)
- [ ] Make the list_of_xs_sorter class more svelte using a design pattern.
- [x] Move demo usage code to one file and out of my list_of_xs_sorter class file.
- [x] Write "output as" methods for each individual sorter class to permit outputting as other list of x types.
- [ ] Better example cases for the readme
- [ ] Allow a user to inject a sort order type (Month, day names as an example) to sort by custom values. 
  
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
