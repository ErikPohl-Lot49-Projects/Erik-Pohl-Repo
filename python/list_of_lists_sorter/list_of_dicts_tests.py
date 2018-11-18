from unittest import TestCase
from list_of_dicts_sorter import list_of_dicts_sorter

class ListOfDictsTests(TestCase):

    def testCaseBasicInitialization(self):
        output_dict = [
            [{'one': 1, 'two': 5}],
            [{'one': 1, 'two': 4}]
        ]
        lodsorter = list_of_dicts_sorter(output_dict)
        self.assertEqual(lodsorter.list_of_dicts, output_dict)  # initialized value
        self.assertEqual(lodsorter.reverse_sort, False)  # default value
        sort_style = [("one"), ("two")]
        lodsorter.add_multiple_fields_by_key_names(sort_style)
        lodsorter.clear_sort_fields()
        sort_style = [("one"), ("two", lodsorter.STRINGDATEPREFIX+'-')]
        lodsorter.add_multiple_fields_by_key_names(sort_style)
        print(lodsorter.sort_fields)

    def testCaseTestDateSort(self):
        output_list_of_dicts = [
            {'one': 1, 'two': '1-1-15'},
            {'one': 1, 'two': '1-1-14'}
        ]
        lodsorter = list_of_dicts_sorter(output_list_of_dicts)
        lodsorter.add_sort_field_by_key_name('two','datestringdelimiter-')
        sorted_output = lodsorter.sort()
        self.assertEqual(sorted_output, [
            {'one': 1, 'two': '1-1-14'},
            {'one': 1, 'two': '1-1-15'}
        ])
        lodsorter.reverse_sort = True
        sorted_output = lodsorter.sort()
        self.assertEqual(sorted_output, [
            {'one': 1, 'two': '1-1-15'},
            {'one': 1, 'two': '1-1-14'}
        ])

    def testCaseNumberOnlySort(self):
        output_list_of_dicts = [
            {'one': 1, 'two': '5'},
            {'one': 1, 'two': '4'}
        ]
        lodsorter = list_of_dicts_sorter(output_list_of_dicts)
        lodsorter.add_sort_field_by_key_name('two')
        sorted_output = lodsorter.sort()
        self.assertEqual(sorted_output, [
            {'one': 1, 'two': '4'},
            {'one': 1, 'two': '5'}
        ])
        lodsorter.reverse_sort = True
        sorted_output = lodsorter.sort()
        self.assertEqual(sorted_output, [
            {'one': 1, 'two': '5'},
            {'one': 1, 'two': '4'}
        ])
        sort_style = [("two"), ("one")]
        lodsorter.add_multiple_fields_by_key_names(sort_style)
        lodsorter.reverse_sort = False
        sorted_output = lodsorter.sort()
        self.assertEqual(sorted_output, [
            {'one': 1, 'two': '4'},
            {'one': 1, 'two': '5'}
        ])

