from unittest import TestCase
from kleene_project.kleene import kleene
import re

class testKleene(TestCase):
    
    def test_lov_xor(self):
        lov = ['Hello', 'Goodbye', 'Aloha']
        clean = kleene()
        regex_pattern_string = clean.list_of_values(lov)
        print(regex_pattern_string)
        xor_satisfied = bool(re.match(regex_pattern_string, 'Hello' ))
        xor_unsatisfied = bool(re.match(regex_pattern_string, 'HelloGoodbye'))
        xor_too_much = bool(re.match(regex_pattern_string, 'AlohaAloah' ))
        xor_not_found = bool(re.match(regex_pattern_string, 'Aloah' ))
        self.assertEqual(xor_satisfied, True, msg='xor satisfied')
        self.assertEqual(xor_unsatisfied, False, msg='xor unsatisfied')
        self.assertEqual(xor_too_much, False, msg='xor too much')
        self.assertEqual(xor_too_much, False, msg='xor not found')
