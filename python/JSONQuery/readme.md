# JSON Query Tool

This accepts a JSON format description and a JSON expression.
Using Python's regex module (re) and the JSON format description, this returns a list of mismatches or matches if certain conditions are met:
a) are all query format JSON keys present in and mode?  in or mode for matches, which matches qualify?
b) do the values in the JSON expression for all the format description keys match regular expression definitions set up in the format description?

The goal here, whether using it in mismatch mode or match mode, is to be able to filter nested JSON for certain match conditions which are customizable and accept regex expressions.

In Mismatch mode, it can act as a validation, returning all the conditions which fail so that they can be corrected -- think: is this JSON missing a value or does it have a bad value?  Where are the mismatches between the expected format and the actual value?

In Match mode, it can act as a filter, retriving only some keys from a JSON source or permitting code which calls this to return JSON which has a match (and mode or or mode).  So if a client were being served JSON and it only wanted the deeply nested foo key values, you could use this to get them.  If a client were being served JSON, and it only wanted to display the JSON with foo which matches one regex string and bar which matches another, this functionality is addressed in match mode.


# Example cases

#### No mismatches in a basic format-- this would be a find against a JSON dictionary 
        json_format_compare({'hello':'1'},{'hello':'1'})
        
        []
        
#### No mismatches in a basic format using a wildcard-- this would be a find against a JSON dictionary 
        json_format_compare({'hello':'1'},{'hello': '.'})
        
        []

#### Mismatch in a basic format -- this would be a record mismatch and would not produce a find against a JSON dictionary 
        json_format_compare({'hello':'1'},{'hello': 'x'})
        
        ['/hello']

#### No mismatches in a nested format-- this would be a find against a JSON dictionary 
        json_format_compare({'hello': '1', 'zap': {'h1': 'one', 'h2': 'two', 'single': '1'}},
        {'hello': '1', 'zap': {'h1': 'one', 'h2': 'two', 'single': '.'}})
        
        []

#### Mismatches in a nested format level 1 -- this would be a record mismatch and would not produce a find against a JSON dictionary  
        json_format_compare({'hello': '2', 'zap': {'h1': 'one', 'h2': 'two', 'single': '1'}},
        {'hello': '1', 'zap': {'h1': 'one', 'h2': 'two', 'single': '.'}})
        
        ['/hello']

#### Mismatches in a nested format level 1/2 -- this would be a record mismatch and would not produce a find against a JSON dictionary  
        json_format_compare({'hello': '2', 'zap': {'h1': 'one', 'h2': 'two', 'single': '1'}},
        {'hello': '1', 'zap': {'h1': 'one', 'h2': 'two', 'single': '2'}})
        
        ['/hello', '/zap/single'])

#### Unexpected format key
        json_format_compare({'hello': '2', 'zap': {'h1': 'one', 'h2': 'two', 'single': '1'}},
        {'hello': '.', 'blammo' : 'blam', 'zap': {'h1': 'one', 'h2': 'two', 'single': '.'}})
        
        ['/blammo']
        
#### No mismatches in a nested format with format using only some keys in test data -- this would be a find against a JSON dictionary 
        json_format_compare({'hello': '1', 'zap': {'h1': 'one', 'h2': 'two', 'single': '.'}},
        {'zap': {'h1': 'one'}})
        
        []      

#### Mismatch in a nested format with format using only some keys in test data -- this would be a find against a JSON dictionary 
        json_format_compare({'hello': '1', 'zap': {'h1': 'one', 'h2': 'two', 'single': '.'}},
        {'zap': {'h1': 'onx'}})
        
        ['/zap/h1']) 

#### Mismatches in a nested format with format using only some keys in test data -- this would be a find against a JSON dictionary 
        json_format_compare({'hello': '1', 'zap': {'h1': 'one', 'h2': 'two', 'single': '4'},
       'zap': {'h1': 'onx', 'single': '5'}})
        
        [['/zap/h1', '/zap/single']]) 
        
#### Match found using a format looking for any character string in a field -- will return this filtered match result and path
        json_format_compare({'hello': '1', 'zap': {'h1': 'one', 'h2': 'two', 'single': '.'}},
        {"zap": {"h1": ".*"}, matchmode=1)
        
        [('/zap/h1', 'one')]
        
#### Match found using or mode where only one format criteria is matching
        json_format_compare({'hello': '1', 'zap': {'h1': 'one', 'h2': 'two', 'single': '.'}},
        {"hello": ".", 'zap': {'h1': 'ox'}}, matchmode=2)
        
        [('/hello', '1')]

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
