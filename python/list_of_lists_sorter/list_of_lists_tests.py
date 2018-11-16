from unittest import TestCase
from list_of_lists_sorter import list_of_list_sorter

class ListofListsTests(TestCase):

    def testCaseBasicInitialization(self):
        output_list_without_header = [
            [1, 2, 3, 7, 1, 7, '1-1-15'],
            [1, 2, 3, 7, 2, 6, '1-1-14']
        ]
        lolsorter = list_of_list_sorter(output_list_without_header)
        self.assertEqual(lolsorter.list_of_lists, output_list_without_header)   # initialized value
        self.assertEqual(lolsorter.has_header, False)                           # default value
        self.assertEqual(lolsorter.reverse_sort,False)                          # default value
    def testCaseBasicPositionalPositionalSortFields(self):
        output_list_without_header = [
            [1, 2, 3, 7, 1, 7, '1-1-15'],
            [1, 2, 3, 7, 2, 6, '1-1-14']
        ]
        lolsorter = list_of_list_sorter(output_list_without_header)
        self.assertEqual(lolsorter.list_of_lists, output_list_without_header)   # initialized value
        lolsorter.add_sort_field_by_position(5)
        # the first item should have a defaulted string type and a position of 5
        self.assertEqual(lolsorter.sort_fields[0].position,5)
        self.assertEqual(lolsorter.sort_fields[0].field_type, 'string')
        lolsorter.add_sort_field_by_position(6, "datestringdelimiter")
        self.assertEqual(lolsorter.sort_fields[1].position,6)
        self.assertEqual(lolsorter.sort_fields[1].field_type, 'datestringdelimiter')

        lolsorter.clear_sort_fields()
        self.assertEqual(0,len(lolsorter.sort_fields))

        lolsorter.add_multiple_fields_by_position([(5), (6, 'datestringdelimiter'), (7,'string')])
        self.assertEqual(lolsorter.sort_fields[0].position,5)
        self.assertEqual(lolsorter.sort_fields[0].field_type, 'string')
        self.assertEqual(lolsorter.sort_fields[1].position,6)
        self.assertEqual(lolsorter.sort_fields[1].field_type, 'datestringdelimiter')
        self.assertEqual(lolsorter.sort_fields[2].position,7)
        self.assertEqual(lolsorter.sort_fields[2].field_type, "string")
