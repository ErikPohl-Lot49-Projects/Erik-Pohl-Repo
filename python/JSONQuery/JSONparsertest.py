'''
Created on Oct 21, 2018

@author: Erik Pohl
'''
import parameterized as pm
import JSONparser as JP
import unittest as ut
from JSONparser import json_query_finding, JSON_KEY_MISSING, JSON_VALUE_MISMATCH, MATCHMODES

class JSONParsertest(ut.TestCase):
    @pm.parameterized.expand([
        ("Basic match", {'hello':'1'},{'hello':'1'}, MATCHMODES["MISMATCH"], []),

        ("Basic Wildcard match", {'hello': '1'}, {'hello': '.'}, MATCHMODES["MISMATCH"], []),

        ("Basic mismatch", {'hello': '1'}, {'hello': 'x'}, MATCHMODES["MISMATCH"],
         [json_query_finding(current_json_path='/hello', queried_json_clause=JSON_VALUE_MISMATCH)]),

        ("Nested match", {'hello': '1', 'zap': {'h1': 'one', 'h2': 'two', 'single': '1'}},
         {'hello': '1', 'zap': {'h1': 'one', 'h2': 'two', 'single': '.'}}, MATCHMODES["MISMATCH"],[]),

        ("Nested mismatch level 1", {'hello': '2', 'zap': {'h1': 'one', 'h2': 'two', 'single': '1'}},
         {'hello': '1', 'zap': {'h1': 'one', 'h2': 'two', 'single': '.'}}, MATCHMODES["MISMATCH"],
         [json_query_finding(current_json_path='/hello', queried_json_clause=JSON_VALUE_MISMATCH)]),

        ("Nested mismatch level 1 and 2", {'hello': '2', 'zap': {'h1': 'one', 'h2': 'two', 'single': '1'}},
         {'hello': '1', 'zap': {'h1': 'one', 'h2': 'two', 'single': '2'}}, MATCHMODES["MISMATCH"],
         [json_query_finding(current_json_path='/hello', queried_json_clause=JSON_VALUE_MISMATCH),
          json_query_finding(current_json_path='/zap/single', queried_json_clause=JSON_VALUE_MISMATCH)]),

        ("Unexpected format key", {'hello': '1', 'zap': {'h1': 'one', 'h2': 'two', 'single': '1'}},
         {'hello': '.', 'blammo' : 'blam', 'zap': {'h1': 'one', 'h2': 'two', 'single': '.'}}, MATCHMODES["MISMATCH"],
         [json_query_finding(current_json_path='/blammo', queried_json_clause=JSON_KEY_MISSING)]),

        ("Nested match with fewer keys in format", {'hello': '1', 'zap': {'h1': 'one', 'h2': 'two', 'single': '.'}},
         {'zap': {'h1': 'one'}}, MATCHMODES["MISMATCH"],[]),

        ("Nested mismatch with fewer keys in format", {'hello': '1', 'zap': {'h1': 'one', 'h2': 'two', 'single': '.'}},
         {'zap': {'h1': 'onx'}}, MATCHMODES["MISMATCH"],
         [json_query_finding(current_json_path='/zap/h1', queried_json_clause=JSON_VALUE_MISMATCH)]),

        ("Nested mismatches with fewer keys in format", {'hello': '1', 'zap': {'h1': 'one', 'h2': 'two', 'single': '4'}},
         {'zap': {'h1': 'onx', 'single': '5'}}, MATCHMODES["MISMATCH"],
         [json_query_finding(current_json_path='/zap/h1', queried_json_clause=JSON_VALUE_MISMATCH),
          json_query_finding(current_json_path='/zap/single', queried_json_clause=JSON_VALUE_MISMATCH)]),

        ("report matches all ands satisfied with nesting",{'hello': '1', 'zap': {'h1': 'one', 'h2': 'two', 'single': '.'}},
         {"zap": {"h1": ".*"}, "hello": ".*"},MATCHMODES["AND"],
         [json_query_finding(current_json_path='/zap/h1', queried_json_clause='one'),
          json_query_finding(current_json_path='/hello', queried_json_clause='1')]),

        ("report matches one and not satisfied with nesting",
         {'hello': '1', 'zap': {'h1': 'one', 'h2': 'two', 'single': '.'}},
         {"zap": {"h1": ".*"}, "hello": "3"}, MATCHMODES["AND"], []),

        ("report matches all ands satisfied without nesting of format",
         {'hello': '1', 'zap': {'h1': 'one', 'h2': 'two', 'single': '.'}},
         {"hello": "."}, MATCHMODES["AND"],
         [json_query_finding(current_json_path='/hello', queried_json_clause='1')]),

        ("report or matches",
         {'hello': '1', 'zap': {'h1': 'one', 'h2': 'two', 'single': '.'}},
         {"hello": ".", 'zap': {'h1': 'ox'}}, MATCHMODES["OR"],
         [json_query_finding(current_json_path='/hello', queried_json_clause='1')]),
    ])
    def testJSONparser(self, testname, testinp, testinp2, matchtype, expected):
        self.assertEqual(expected, JP.compare_json_to_query_clause(testinp, testinp2, match_mode=matchtype, debug_mode=True))
