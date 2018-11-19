'''
Created on Oct 21, 2018

@author: Erik Pohl
'''
import parameterized as pm
import JSONparser as JP
import unittest as ut
from JSONparser import json_query_finding, JSON_KEY_MISSING, JSON_VALUE_MISMATCH, MATCHMODES

#TODO should a mismatch which is actually mismatched return an 'actual_finding_value' of the input json
class JSONParsertest(ut.TestCase):
    @pm.parameterized.expand([
        ("Basic match", {'hello':'1'},{'hello':'1'}, MATCHMODES["MISMATCH"], None),

        ("Basic Wildcard match", {'hello': '1'}, {'hello': '.'}, MATCHMODES["MISMATCH"], None),

        ("Basic mismatch", {'hello': '1'}, {'hello': 'x'}, MATCHMODES["MISMATCH"],
         None),

        ("Nested match", {'hello': '1', 'zap': {'h1': 'one', 'h2': 'two', 'single': '1'}},
         {'hello': '1', 'zap': {'h1': 'one', 'h2': 'two', 'single': '.'}}, MATCHMODES["MISMATCH"],None),

        ("Nested mismatch level 1", {'hello': '2', 'zap': {'h1': 'one', 'h2': 'two', 'single': '1'}},
         {'hello': '1', 'zap': {'h1': 'one', 'h2': 'two', 'single': '.'}}, MATCHMODES["MISMATCH"],
         None),

        ("Nested mismatch level 1 and 2", {'hello': '2', 'zap': {'h1': 'one', 'h2': 'two', 'single': '1'}},
         {'hello': '1', 'zap': {'h1': 'one', 'h2': 'two', 'single': '2'}}, MATCHMODES["MISMATCH"],
         None),

        ("Unexpected format key", {'hello': '1', 'zap': {'h1': 'one', 'h2': 'two', 'single': '1'}},
         {'hello': '.', 'blammo' : 'blam', 'zap': {'h1': 'one', 'h2': 'two', 'single': '.'}}, MATCHMODES["MISMATCH"],
         None),

        ("Nested match with fewer keys in format", {'hello': '1', 'zap': {'h1': 'one', 'h2': 'two', 'single': '.'}},
         {'zap': {'h1': 'one'}}, MATCHMODES["MISMATCH"],None),

        ("Nested mismatch with fewer keys in format", {'hello': '1', 'zap': {'h1': 'one', 'h2': 'two', 'single': '.'}},
         {'zap': {'h1': 'onx'}}, MATCHMODES["MISMATCH"],
         None),

        ("Nested mismatches with fewer keys in format",
         {'hello': '1', 'zap': {'h1': 'one', 'h2': 'two', 'single': '4'}},
         {'zap': {'h1': 'onx', 'single': '5'}},
         MATCHMODES["MISMATCH"],
         None),

        ("report matches all ands satisfied with nesting",
         {'hello': '1', 'zap': {'h1': 'one', 'h2': 'two', 'single': '.'}},
         {"zap": {"h1": ".*"}, "hello": ".*"},MATCHMODES["AND"],
         {'hello': '1', 'zap': {'h1': 'one', 'h2': 'two', 'single': '.'}}),

        ("report matches one and not satisfied with nesting",
         {'hello': '1', 'zap': {'h1': 'one', 'h2': 'two', 'single': '.'}},
         {"zap": {"h1": ".*"}, "hello": "3"}, MATCHMODES["AND"],
         None),

        ("report matches all ands satisfied without nesting of format",
         {'hello': '1', 'zap': {'h1': 'one', 'h2': 'two', 'single': '.'}},
         {"hello": "."}, MATCHMODES["AND"],
         {'hello': '1', 'zap': {'h1': 'one', 'h2': 'two', 'single': '.'}}
         ),

        ("report or matches",
         {'hello': '1', 'zap': {'h1': 'one', 'h2': 'two', 'single': '.'}},
         {"hello": ".", 'zap': {'h1': 'ox'}}, MATCHMODES["OR"],
         {'hello': '1', 'zap': {'h1': 'one', 'h2': 'two', 'single': '.'}}),
    ])
    def testJSONparser(self, testname, testinp, testinp2, matchtype, expected):
        actual = JP.compare_json_to_query_clause(testinp, testinp2, match_mode=matchtype, debug_mode=True)
        print(actual.overall_result)
        self.assertEqual(expected, actual.overall_result)