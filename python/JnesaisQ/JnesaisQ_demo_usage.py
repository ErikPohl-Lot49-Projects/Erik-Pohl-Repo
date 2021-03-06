# !/usr/bin/env python
# -*- coding: utf-8 -*-
from json import loads
from JnesaisQ import JnesaisQ, jnesaisq_compare

__author__ = "Erik Pohl"
__copyright__ = "None"
__credits__ = ["Erik Pohl"]
__license__ = "GPL"
__version__ = "1.0.0"
__maintainer__ = "Erik Pohl"
__email__ = "erik.pohl.444@gmail.com"
__status__ = "Beta"


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

JNSQ = JnesaisQ(json_query_format)
result = JNSQ.compare_verbose(test_json, debug_mode=0)
print("mismatches", result.json_query_mismatches)
print("matches", result.json_query_matches)
print("Overall result", JNSQ.overall_result(result))

print("testing a list of test json dictionaries")
print(JNSQ.list_of_compares(test_json_list))

with jnesaisq_compare(json_query_format) as j:
    print(j(test_json))
