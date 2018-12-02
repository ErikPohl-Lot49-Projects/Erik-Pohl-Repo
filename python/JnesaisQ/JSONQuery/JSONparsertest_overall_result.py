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
        ("Basic match", {'hello':'1'},{'hello':'1'}, MATCHMODES["MISMATCH"], False),

        ("Basic Wildcard match", {'hello': '1'}, {'hello': '.'}, MATCHMODES["MISMATCH"], False),

        ("Basic mismatch", {'hello': '1'}, {'hello': 'x'}, MATCHMODES["MISMATCH"],
         True),

        ("Nested match", {'hello': '1', 'zap': {'h1': 'one', 'h2': 'two', 'single': '1'}},
         {'hello': '1', 'zap': {'h1': 'one', 'h2': 'two', 'single': '.'}}, MATCHMODES["MISMATCH"],False),

        ("Nested mismatch level 1", {'hello': '2', 'zap': {'h1': 'one', 'h2': 'two', 'single': '1'}},
         {'hello': '1', 'zap': {'h1': 'one', 'h2': 'two', 'single': '.'}}, MATCHMODES["MISMATCH"],
         False),

        ("Nested mismatch level 1 and 2", {'hello': '2', 'zap': {'h1': 'one', 'h2': 'two', 'single': '1'}},
         {'hello': '1', 'zap': {'h1': 'one', 'h2': 'two', 'single': '2'}}, MATCHMODES["MISMATCH"],
         False),

        ("Unexpected format key", {'hello': '1', 'zap': {'h1': 'one', 'h2': 'two', 'single': '1'}},
         {'hello': '.', 'blammo' : 'blam', 'zap': {'h1': 'one', 'h2': 'two', 'single': '.'}}, MATCHMODES["MISMATCH"],
         False),

        ("Nested match with fewer keys in format", {'hello': '1', 'zap': {'h1': 'one', 'h2': 'two', 'single': '.'}},
         {'zap': {'h1': 'one'}}, MATCHMODES["MISMATCH"],
         False),

        ("Nested mismatch with fewer keys in format", {'hello': '1', 'zap': {'h1': 'one', 'h2': 'two', 'single': '.'}},
         {'zap': {'h1': 'onx'}}, MATCHMODES["MISMATCH"],
         True),

        ("Nested mismatches with fewer keys in format",
         {'hello': '1', 'zap': {'h1': 'one', 'h2': 'two', 'single': '4'}},
         {'zap': {'h1': 'onx', 'single': '5'}},
         MATCHMODES["MISMATCH"],
         True),

        ("report matches all ands satisfied with nesting",
         {'hello': '1', 'zap': {'h1': 'one', 'h2': 'two', 'single': '.'}},
         {"zap": {"h1": ".*"}, "hello": ".*"},MATCHMODES["AND"],
         True),

        ("report matches one and not satisfied with nesting",
         {'hello': '1', 'zap': {'h1': 'one', 'h2': 'two', 'single': '.'}},
         {"zap": {"h1": ".*"}, "hello": "3"}, MATCHMODES["AND"],
         False),

        ("report matches all ands satisfied without nesting of format",
         {'hello': '1', 'zap': {'h1': 'one', 'h2': 'two', 'single': '.'}},
         {"hello": "."}, MATCHMODES["AND"],
         True
         ),

        ("report or matches with all criteria not met",
         {'hello': '1', 'zap': {'h1': 'one', 'h2': 'two', 'single': '.'}},
         {"hello": ".", 'zap': {'h1': 'ox'}}, MATCHMODES["OR"],
         False),

        ("report or matches with all criteria met",
         {'hello': '1', 'zap': {'h1': 'one', 'h2': 'two', 'single': '.'}},
         {"hello": ".", 'zap': {'h1': '.*'}}, MATCHMODES["OR"],
         True),
    ])
    def testJSONparser(self, testname, testinp, testinp2, matchtype, expected):
        actual = JP.compare_json_to_query_clause(testinp, testinp2, match_mode=matchtype, debug_mode=True)
        print(actual.all_criteria_met)
        self.assertEqual(expected, actual.all_criteria_met)
