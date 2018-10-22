'''
Created on Oct 21, 2018

@author: Erik Pohl
'''
import parameterized as pm
import JSONparser as JP
import unittest as ut

class JSONParsertest(ut.TestCase):
    @pm.parameterized.expand([
        ("Basic match", {'hello':'1'},{'hello':'1'}, 0, []),
        ("Basic Wildcard match", {'hello': '1'}, {'hello': '.'}, 0, []),
        ("Basic mismatch", {'hello': '1'}, {'hello': 'x'}, 0,['/hello']),
        ("Nested match", {'hello': '1', 'zap': {'h1': 'one', 'h2': 'two', 'single': '1'}},
         {'hello': '1', 'zap': {'h1': 'one', 'h2': 'two', 'single': '.'}}, 0,[]),
        ("Nested mismatch level 1", {'hello': '2', 'zap': {'h1': 'one', 'h2': 'two', 'single': '1'}},
         {'hello': '1', 'zap': {'h1': 'one', 'h2': 'two', 'single': '.'}}, 0,['/hello']),
        ("Nested mismatch level 1 and 2", {'hello': '2', 'zap': {'h1': 'one', 'h2': 'two', 'single': '1'}},
         {'hello': '1', 'zap': {'h1': 'one', 'h2': 'two', 'single': '2'}}, 0,['/hello', '/zap/single']),
        ("Unexpected format key", {'hello': '1', 'zap': {'h1': 'one', 'h2': 'two', 'single': '1'}},
         {'hello': '.', 'blammo' : 'blam', 'zap': {'h1': 'one', 'h2': 'two', 'single': '.'}}, 0,['/blammo'] ),
        ("Nested match with fewer keys in format", {'hello': '1', 'zap': {'h1': 'one', 'h2': 'two', 'single': '.'}},
         {'zap': {'h1': 'one'}}, 0,[]),
        ("Nested mismatch with fewer keys in format", {'hello': '1', 'zap': {'h1': 'one', 'h2': 'two', 'single': '.'}},
         {'zap': {'h1': 'onx'}}, 0,['/zap/h1']),
        ("Nested mismatches with fewer keys in format", {'hello': '1', 'zap': {'h1': 'one', 'h2': 'two', 'single': '4'}},
         {'zap': {'h1': 'onx', 'single': '5'}}, 0,['/zap/h1', '/zap/single']),
        ("report matches all ands satisfied with nesting",{'hello': '1', 'zap': {'h1': 'one', 'h2': 'two', 'single': '.'}},
         {"zap": {"h1": ".*"}, "hello": ".*"},1,[('/zap/h1', 'one'), ('/hello', '1')]),
        ("report matches one and not satisfied with nesting",
         {'hello': '1', 'zap': {'h1': 'one', 'h2': 'two', 'single': '.'}},
         {"zap": {"h1": ".*"}, "hello": "3"}, 1, []),
        ("report matches all ands satisfied without nesting of format",
         {'hello': '1', 'zap': {'h1': 'one', 'h2': 'two', 'single': '.'}},
         {"hello": "."}, 1, [('/hello', '1')]),
    ])
    def testJSONparser(self, testname, testinp, testinp2, matchtype, expected):
        self.assertEqual(expected,JP.json_format_compare(testinp, testinp2, matchmode=matchtype))
