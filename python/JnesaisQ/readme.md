# JnesaisQ (was "JSONQuery")

**_Along with a name change, this will target enhanced functionality_**

![You do](https://github.com/ErikPohl-Lot49-Projects/Erik-Pohl-Repo/blob/master/media/you-do-have-a-certain-je-ne-sais-quoi-metal-prints.jpg "Je ne sais quoi")


_Imagine you are handling a sufficient amount of JSON input data._

The data has a bevy of keys, including deeply nested keys.

You want to query the JSON data flexibly.

JnesaisQ provides a useful handle to query JSON data by flexibly defined keys within the JSON and regex to query the values for those keys.

---------

Let's talk about one example use case.

You're loading JSON from an API.

You might want to allow a user to designate some keys they are interested in querying, while ignoring the other keys in the JSON.
You want to allow for wildcards in the values for the keys the user is interested in.

Or imagine you want to find negative cases: JSON values which do not match a pattern.  

You want to be able to have granular designations: 
* which query clauses match?  what were the actual values which matched?
* which query clauses mismatch?  what were the actual values which matched? were keys left out of the queried JSON?
* ultimately, was this an:
  * AND match (all query format criteria were met)
  * an OR match mismatch (some query format criteria matched and some mismatched)
  * AND mismatch (all query format criteria failed)
  
---------
  
My friend, you need a certain _je ne sais quoi_ to do this.  JnesaisQ returns this info for you.

Using this class in a loop of all the data in your input will help you encapsulate the hard parts of searching the input JSON using highly flexible query expressions.  

Or you can use the class method created specifically for this purpose.

---------

On instantiation, JnesaisQ accepts a JSON query format description.

Using a compare method, you can then compare against a JSON expression: either verbose or just the overall results.

Using Python's regex module (re) and the JSON format description, this returns a list of mismatches or matches if certain conditions are met in verbose mode.  It returns an overall conclusion if not in verbose mode.

The goal here is to be able to filter even deeply-nested JSON for certain match conditions: match conditions which are flexibly customizable and which accept regex expressions for value matches.

So, if a client were being served JSON and it only wanted the matches to the deeply nested key values for a single key (foo) deeply embedded in the JSON, you could use this to get those matches.  

If a client were being served JSON, and it only wanted to display the JSON with foo keys whose values matches one regex string and bar keys whose values match another, this functionality is also addressed.  

ANDs and ORs are diagnosed by a overall_result diagnosis.


# Example cases

#### Import some stuff
````
from json import loads
from JnesaisQ import JnesaisQ, jnesaisq_compare
````

#### Create the demonstration case
* **_test_json_str_ is the JSON to be queried**
* **_json_query_format_str_ is the JSON query itself-- a subset of JSON keys with regex for pattern-matching values**
* **_test_json_list_ will be used to test repetetive queries of JSON using the query format**
````
test_json_str = '{"hello": "1", "zap": {"h1": ' \
                '"one", "h2": "two", "single": "."}}'
json_query_format_str = '{"zap": {"h1": ".*"}, "hello": ".*"}'
test_json = loads(test_json_str)
json_query_format = loads(json_query_format_str)
test_json_list = []
for i in range(5):
    test_json_list.append(test_json)
print("starting test_json", test_json)
print("starting json_query_format", json_query_format)
````

#### The easiest way to use basic JnesaisQ functionality: with a context manager handle
````
with jnesaisq_compare(json_query_format) as j:
    print(j(test_json))
````

#### Instantiate JnesaisQ and get the verbose output for a query along with an overall result
````
JNSQ = JnesaisQ(json_query_format)
result = JNSQ.compare_verbose(test_json, debug_mode=0)
print("mismatches", result.json_query_mismatches)
print("matches", result.json_query_matches)
print("Overall result", JNSQ.overall_result(result))
````

#### Executing a query against a list 
````
print("testing a list of test json dictionaries")
print(JNSQ.list_of_compares(test_json_list))
````

# Important disclaimer

The code here does not represent work I'd submit for production code-review.  Standards differ, and I have worked within many different
sets, helping to establish and build on them.

Here are some elements I expect to be able to provide, if needed:

a) Requirements documents, user-facing documents and presentations, and other documents consistent with Agile User Stories to add value.

## Future work

- [x] Lint the code and clean up.
- [x] Make this a class definition.
- [x] Rework example cases in GitHub repo to be up-to-date with current revisions.
- [x] Provide additional demo usage cases.
- [x] Tie this to the list_of_xs_sorter by producing a list of dicts output for mass querying.
- [x] Re-evaluate the output format.
- [ ] Change regex value matchers to include also functional value matchers?
- [ ] Consider concurrency when querying lots of input data in the mass query function.

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
