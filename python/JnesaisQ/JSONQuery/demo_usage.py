from json import loads
from JSONparser import compare_json_to_query_clause

test_json_str =         '{"hello": "1", "zap": {"h1": "one", "h2": "two", "single": "."}}'
json_query_format_str = '{"zap": {"h1": ".*"}, "hello": ".*"}'
test_json = loads(test_json_str)
json_query_format = loads(json_query_format_str)
print("starting test_json", test_json)
print("starting json_query_format", json_query_format)
print("mismatches", compare_json_to_query_clause(test_json, json_query_format, debug_mode=0))
print("matches", compare_json_to_query_clause(test_json, json_query_format, match_mode=1, debug_mode=1))
test_json = {'hello': '1', 'zap': {'h1': 'one', 'h2': 'two', 'single': '.'}}
json_query_format= {"zap": {"h1": ".*"}, "hello": ".*"}
matches = compare_json_to_query_clause(test_json, json_query_format, match_mode=2, debug_mode=1)
print("matches", matches)
