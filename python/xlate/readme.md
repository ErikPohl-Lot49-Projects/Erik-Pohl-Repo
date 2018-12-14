# xlate


This class encapsulates logic to convert a string input from one format into another string format, or into a dictionary.


# Example usage

#### Import the xlate class
```
from xlate import xlate
```

#### Set up the class with an input string, an input string delimiter, and an input format
```
input_string = 'pohl erik 9/2/72 python arlington'
input_del = ' '
input_format = ['lname', 'fname', 'bdate', 'language_of_choice', 'hometown']
demo_usage = xlate(input_string, input_del, input_format)
```

#### Specify an output format with keyword fields
````
output_format = '{fname} {lname}, born on {bdate}, lives in {hometown} and prefers {language_of_choice}'
````

#### Using all the input definitions and the output format, output it as a string and then as a dictionary
````
print(demo_usage.to_string_using_keyword_format(output_format))
print(demo_usage.to_dictionary())
````

#### Now, let's try an output format with positionally-designated fields
````
output_format = '{0} {1}, born on {2}, lives in {3} and prefers {4}'
````

#### This time, our input will be specified with no input format-- just an input string and delimiters
````
demo_usage = xlate(input_string, input_del)
````

#### Let's output the contents of our input in the positionally-designated output format as a string then as a dictionary
````
print(demo_usage.to_string_using_keyword_format(output_format))
print(demo_usage.to_dictionary())
````

#### Now, let's try outputting that positionally-designated input one more time -- remember, no keyword designations but this time let's force a keyword output format to be positional instead

#### Here's the output format-- a keyword-designated one
````
output_format = '{fname} {lname}, born on {bdate}, lives in {hometown} and prefers {language_of_choice}'
````

#### Here's us outputting it as a string using forced positional fields
````
print(demo_usage.to_string_forcing_positional(output_format))
````

# Important disclaimer

The code here does not represent work I'd submit for production code-review.  Standards differ, and I have worked within many different
sets, helping to establish and build on them.

Here are some elements I expect to be able to provide, if needed:

- [ ] A complete regression test suite.
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
