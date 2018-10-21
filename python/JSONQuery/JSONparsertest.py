'''
Created on Jan 7, 2018

@author: Erik Pohl
'''
import parameterized as pm
import JSONparser as JP
import unittest as ut

class JSONParsertest(ut.TestCase):
    @pm.parameterized.expand([
        ("Basic match", {'hello':'1'},{'hello':'1'}, []),
        ("Basic Wildcard match", {'hello': '1'}, {'hello': '.'}, []),
        ("Basic mismatch", {'hello': '1'}, {'hello': 'x'}, ['/hello']),
        ("Nested match", {'hello': '1', 'zap': {'h1': 'one', 'h2': 'two', 'single': '1'}},
         {'hello': '1', 'zap': {'h1': 'one', 'h2': 'two', 'single': '.'}}, []),
        ("Nested mismatch level 1", {'hello': '2', 'zap': {'h1': 'one', 'h2': 'two', 'single': '1'}},
         {'hello': '1', 'zap': {'h1': 'one', 'h2': 'two', 'single': '.'}}, ['/hello']),
        ("Nested mismatch level 1 and 2", {'hello': '2', 'zap': {'h1': 'one', 'h2': 'two', 'single': '1'}},
         {'hello': '1', 'zap': {'h1': 'one', 'h2': 'two', 'single': '2'}}, ['/hello', '/zap/single']),
        ("Unexpected format key", {'hello': '1', 'zap': {'h1': 'one', 'h2': 'two', 'single': '1'}},
         {'hello': '.', 'blammo' : 'blam', 'zap': {'h1': 'one', 'h2': 'two', 'single': '.'}}, ['/blammo'] ),
        ("Nested match with fewer keys in format", {'hello': '1', 'zap': {'h1': 'one', 'h2': 'two', 'single': '.'}},
         {'zap': {'h1': 'one'}}, []),
        ("Nested mismatch with fewer keys in format", {'hello': '1', 'zap': {'h1': 'one', 'h2': 'two', 'single': '.'}},
         {'zap': {'h1': 'onx'}}, ['/zap/h1']),
        ("Nested mismatches with fewer keys in format", {'hello': '1', 'zap': {'h1': 'one', 'h2': 'two', 'single': '4'}},
         {'zap': {'h1': 'onx', 'single': '5'}}, [['/zap/h1', '/zap/single']]),
    ])
    def testJSONparser(self, testname, testinp, testinp2, expected):
        self.assertEqual(JP.json_format_compare(testinp, testinp2, '', []), expected)
