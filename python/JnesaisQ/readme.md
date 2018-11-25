# This was "JSON Query Tool", now JnesaisQ

**_Along with a name change, this will target enhanced functionality_**

![You do](https://github.com/ErikPohl-Lot49-Projects/Erik-Pohl-Repo/blob/master/media/you-do-have-a-certain-je-ne-sais-quoi-metal-prints.jpg "Je ne sais quoi")


**The document below will change as I adapt the new JnesaisQ class for demo usages**

_Imagine you are handling a sufficient amount of JSON input data._

The data has a bevy of keys, including deeply nested keys.

You want to query the JSON data flexibly.

For example, you might want to allow a user to designate some keys they are interested in querying, ignoring the others, and allowing for wildcards in the values for the keys they are interested in.

Or imagine you want to find negative cases: JSON values which do not match a pattern.  

You want to be able to have granular designations: 
* where does the query match the actual JSON?  
* which query clauses match in an OR query?  what were the actual values which matched?
* specifically demonstrate all ANDs are matched in an AND query, and by which values.
* for mismatches, which specific clauses mismatched?  
* for mismatches, were keys left out of the queried JSON?

This JSON Query tool returns, based on a parameter switch, either AND match results, OR match results, or mismatches given a JSON query format (using regex expressions for the values in the query format) and a JSON expression to match against.

Using this function in a loop of all the data in your input will help you encapsulate the hard parts of searching the input JSON using highly flexible query expressions.

---------

compare_json_to_query_clause accepts a JSON format description and a JSON expression.

Using Python's regex module (re) and the JSON format description, this returns a list of mismatches or matches if certain conditions are met:
a) are all query format JSON keys present in and mode?  in or mode for matches, which matches qualify?
b) do the values in the JSON expression for all the format description keys match regular expression definitions set up in the format description?

The goal here, whether using it in mismatch mode or match mode, is to be able to filter nested JSON for certain match conditions which are customizable and accept regex expressions.

In Mismatch mode, it can act as a validation, returning all the conditions which fail so that they can be corrected -- think: is this JSON missing a value or does it have a bad value?  Where are the mismatches between the expected format and the actual value?

In Match mode, it can act as a filter, retriving only some keys from a JSON source or permitting code which calls this to return JSON which has a match (AND mode or OR mode).  

So if a client were being served JSON and it only wanted the deeply nested foo key values, you could use this to get them.  

If a client were being served JSON, and it only wanted to display the JSON with foo keys whose values matche one regex string and bar keys whose values match another, this functionality is addressed in match mode.  ANDs and ORs are handled in match mode.


# Example cases

#### Import some stuff
````
from json import loads
from JnesaisQ import JnesaisQ
````

#### Create demo case 1
````
test_json_str =         '{"hello": "1", "zap": {"h1": "one", "h2": "two", "single": "."}}'
json_query_format_str = '{"zap": {"h1": ".*"}, "hello": ".*"}'
test_json = loads(test_json_str)
json_query_format = loads(json_query_format_str)
print("starting test_json", test_json)
print("starting json_query_format", json_query_format)
````

#### Run demo case 1
````
JNSQ = JnesaisQ(json_query_format)
result = JNSQ.compare(test_json,  debug_mode=0)
print("mismatches", result.json_query_matches)
print("matches", result.json_query_mismatches)
print("Overall result", JNSQ.comp_bool(result))
````

#### Output from case 1
````
starting test_json {'hello': '1', 'zap': {'h1': 'one', 'h2': 'two', 'single': '.'}}
starting json_query_format {'zap': {'h1': '.*'}, 'hello': '.*'}
mismatches [json_query_finding(current_json_path='/zap/h1', actual_finding_value='one'), json_query_finding(current_json_path='/hello', actual_finding_value='1')]
matches []
Overall result ['AND_match']
````

# Important disclaimer

The code here does not represent work I'd submit for production code-review.  Standards differ, and I have worked within many different
sets, helping to establish and build on them.

Here are some elements I expect to be able to provide, if needed:

a) Linting the code for PEP 8 standardization.
b) Requirements documents, user-facing documents and presentations, and other documents consistent with Agile User Stories to add value.

## Future work

- [ ] Lint the code and clean up.
- [x] Make this a class definition.
- [ ] Rework example cases in GitHub repo to be up-to-date with current revisions.
- [ ] Provide better demo usage cases.
- [ ] Tie this to the list_of_xs_sorter.
- [ ] Evaluate the output format.
- [ ] Change regex value matchers to include also functional value matchers?

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
