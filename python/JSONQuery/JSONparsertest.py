'''
Created on Oct 21, 2018

@author: Erik Pohl
'''
import parameterized as pm
import JSONparser as JP
import unittest as ut
from JSONparser import json_query_finding

class JSONParsertest(ut.TestCase):
    @pm.parameterized.expand([
        ("Basic match", {'hello':'1'},{'hello':'1'}, 0, []),

        ("Basic Wildcard match", {'hello': '1'}, {'hello': '.'}, 0, []),

        ("Basic mismatch", {'hello': '1'}, {'hello': 'x'}, 0,
         [json_query_finding(current_json_path='/hello', queried_json_clause='mismatch')]),

        ("Nested match", {'hello': '1', 'zap': {'h1': 'one', 'h2': 'two', 'single': '1'}},
         {'hello': '1', 'zap': {'h1': 'one', 'h2': 'two', 'single': '.'}}, 0,[]),

        ("Nested mismatch level 1", {'hello': '2', 'zap': {'h1': 'one', 'h2': 'two', 'single': '1'}},
         {'hello': '1', 'zap': {'h1': 'one', 'h2': 'two', 'single': '.'}}, 0,
         [json_query_finding(current_json_path='/hello', queried_json_clause='mismatch')]),

        ("Nested mismatch level 1 and 2", {'hello': '2', 'zap': {'h1': 'one', 'h2': 'two', 'single': '1'}},
         {'hello': '1', 'zap': {'h1': 'one', 'h2': 'two', 'single': '2'}}, 0,
         [json_query_finding(current_json_path='/hello', queried_json_clause='mismatch'),
          json_query_finding(current_json_path='/zap/single', queried_json_clause='mismatch')]),

        ("Unexpected format key", {'hello': '1', 'zap': {'h1': 'one', 'h2': 'two', 'single': '1'}},
         {'hello': '.', 'blammo' : 'blam', 'zap': {'h1': 'one', 'h2': 'two', 'single': '.'}}, 0,
         [json_query_finding(current_json_path='/blammo', queried_json_clause='key_not_found')]),

        ("Nested match with fewer keys in format", {'hello': '1', 'zap': {'h1': 'one', 'h2': 'two', 'single': '.'}},
         {'zap': {'h1': 'one'}}, 0,[]),

        ("Nested mismatch with fewer keys in format", {'hello': '1', 'zap': {'h1': 'one', 'h2': 'two', 'single': '.'}},
         {'zap': {'h1': 'onx'}}, 0,
         [json_query_finding(current_json_path='/zap/h1', queried_json_clause='mismatch')]),

        ("Nested mismatches with fewer keys in format", {'hello': '1', 'zap': {'h1': 'one', 'h2': 'two', 'single': '4'}},
         {'zap': {'h1': 'onx', 'single': '5'}}, 0,
         [json_query_finding(current_json_path='/zap/h1', queried_json_clause='mismatch'),
          json_query_finding(current_json_path='/zap/single', queried_json_clause='mismatch')]),

        ("report matches all ands satisfied with nesting",{'hello': '1', 'zap': {'h1': 'one', 'h2': 'two', 'single': '.'}},
         {"zap": {"h1": ".*"}, "hello": ".*"},1,
         [json_query_finding(current_json_path='/zap/h1', queried_json_clause='one'),
          json_query_finding(current_json_path='/hello', queried_json_clause='1')]),

        ("report matches one and not satisfied with nesting",
         {'hello': '1', 'zap': {'h1': 'one', 'h2': 'two', 'single': '.'}},
         {"zap": {"h1": ".*"}, "hello": "3"}, 1, []),

        ("report matches all ands satisfied without nesting of format",
         {'hello': '1', 'zap': {'h1': 'one', 'h2': 'two', 'single': '.'}},
         {"hello": "."}, 1,
         [json_query_finding(current_json_path='/hello', queried_json_clause='1')]),

        ("report or matches",
         {'hello': '1', 'zap': {'h1': 'one', 'h2': 'two', 'single': '.'}},
         {"hello": ".", 'zap': {'h1': 'ox'}}, 2,
         [json_query_finding(current_json_path='/hello', queried_json_clause='1')]),
    ])
    def testJSONparser(self, testname, testinp, testinp2, matchtype, expected):
        self.assertEqual(expected,JP.json_format_compare(testinp, testinp2, matchmode=matchtype,debugmode=True))
