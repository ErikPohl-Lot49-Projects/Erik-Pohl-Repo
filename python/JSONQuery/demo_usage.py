from json import loads
from JSONparser import json_format_compare

test_json_str =         '{"hello": "1", "zap": {"h1": "one", "h2": "two", "single": "."}}'
json_query_format_str = '{"zap": {"h1": ".*"}, "hello": ".*"}'
test_json = loads(test_json_str)
json_query_format = loads(json_query_format_str)
print("starting test_json", test_json)
print("starting json_query_format", json_query_format)
print("mismatches", json_format_compare(test_json, json_query_format, debugmode=0))
print("matches", json_format_compare(test_json, json_query_format, matchmode=1, debugmode=1))
test_json = {'hello': '1', 'zap': {'h1': 'one', 'h2': 'two', 'single': '.'}}
json_query_format= {"zap": {"h1": ".*"}, "hello": ".*"}
matches = json_format_compare(test_json, json_query_format, matchmode=2, debugmode=1)
print("matches", matches)
