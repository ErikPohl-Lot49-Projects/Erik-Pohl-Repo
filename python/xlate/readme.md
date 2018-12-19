# xlate


This class encapsulates logic to convert a string input from one string format into another string format, or into a dictionary.

--------------------------------------------

![about as good](https://github.com/ErikPohl-Lot49-Projects/Erik-Pohl-Repo/blob/master/media/google-translate-1401697.jpg "about as good")


# Example usage

### The easiest way to use xlate is with a context manager 
### (The context manager assumes string format to string format (not dictionary) conversions)

#### Import the tool
````
from xlate import xlate_string_formats
````

####  Set up some test cases
````
input_del = ' '
input_format = ['lname', 'fname', 'bdate', 'language_of_choice', 'hometown']
output_format = '{fname} {lname}, born on {bdate}, ' \
                'lives in {hometown} and prefers {language_of_choice}'

input_strings = [
        'pohl erik 9/2/72 python arlington',
        'pynchon thomas 5/5/45 muted_posthorn manhattan'
]
````
#### If you don't specify the input format with keywords, it converts the output format into a positional format
````
with xlate_string_formats(
        xlate_input_delimiter=input_del,
        xlate_output_format=output_format
) as f:
    [print(f(input_string)) for input_string in input_strings]
````

#### Here is an example where the input format has keywords
````
with xlate_string_formats(
        xlate_input_delimiter=input_del,
        xlate_input_format=input_format,
        xlate_output_format=output_format
) as f:
    [print(f(input_string)) for input_string in input_strings]
````

### Or you can use xlate as an explicitly instantiated class

#### Here is a use importing the xlate class explicitly
```
from xlate import xlate
```

#### Create some formats and inputs
````
input_string = 'pohl erik 9/2/72 python arlington'
input_del = ' '
input_format = ['lname', 'fname', 'bdate', 'language_of_choice', 'hometown']
output_format = '{fname} {lname}, born on {bdate}, ' \
                'lives in {hometown} and prefers {language_of_choice}'
````

#### Set up the class with an input format, input delimiter, and output format and it is ready to use
```
demo_usage = xlate(
    xlate_input_delimiter=input_del,
    xlate_input_format=input_format,
    xlate_output_format=output_format
)
```

#### Output an input string in the format out the output format using the input format keywords as a string then a dictionary
````
print(demo_usage.to_string_using_keyword_format(input_string))
print(demo_usage.to_dictionary(input_string))
````

#### Let's try again without an input format, and with a positional output format explicitly specified
````
output_format = '{0} {1}, born on {2}, lives in {3} and prefers {4}'
demo_usage = xlate(
    xlate_input_delimiter=input_del,
    xlate_output_format=output_format
)
print(demo_usage.to_string_using_keyword_format(input_string))
print(demo_usage.to_dictionary(input_string))
````

#### Now, let's not specify an input format and force the keyword output format to be positional
````
output_format = '{fname} {lname}, born on {bdate}, ' \
                'lives in {hometown} and prefers {language_of_choice}'
demo_usage = xlate(
    xlate_input_delimiter=input_del,
    xlate_output_format=output_format
)
print(demo_usage.to_string_forcing_positional(input_string))
````

# Important disclaimer

The code here does not represent work I'd submit for production code-review.  Standards differ, and I have worked within many different
sets, helping to establish and build on them.

Here are some elements I expect to be able to provide, if needed:
- [ ] A complete regression test suite.
- [ ] Meaningful exceptions and exception-handling coverage.
- [ ] Adequate output to permit users to understand the results, assisting in the self-documenting nature of the code.
- [ ] Actual docstring comments at all levels of the code.
- [ ] Requirements documents, user-facing documents and presentations, and other documents consistent with Agile User Stories to add value.


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
