from unittest import TestCase
from list_of_lists_sorter import list_of_lists_sorter

class ListofListsTests(TestCase):

    def testCaseBasicInitialization(self):
        output_list_without_header = [
            [1, 2, 3, 7, 1, 7, '1-1-15'],
            [1, 2, 3, 7, 2, 6, '1-1-14']
        ]
        lolsorter = list_of_lists_sorter(output_list_without_header)
        self.assertEqual(lolsorter.list_of_lists, output_list_without_header)   # initialized value
        self.assertEqual(lolsorter.has_header, False)                           # default value
        self.assertEqual(lolsorter.reverse_sort,False)                          # default value
        output_list_with_header = [['one','two'],['1','2']]
        lolsorter_header = list_of_lists_sorter(output_list_with_header)
        sort_style = [("one"), ("two")]
        lolsorter_header.add_multiple_fields_by_header_field(sort_style)
        print(lolsorter_header.sort_fields)
    def testCaseBasicPositionalPositionalSortFields(self):
        output_list_without_header = [
            [1, 2, 3, 7, 1, 7, '1-1-15'],
            [1, 2, 3, 7, 2, 6, '1-1-14']
        ]
        lolsorter = list_of_lists_sorter(output_list_without_header)
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


    def testCaseBasicNonHeaderTestDateSort(self):
        output_list_without_header = [
            [1, 2, 3, 7, 1, 7, '1-1-15'],
            [1, 2, 3, 7, 2, 6, '1-1-14']
        ]
        lolsorter = list_of_lists_sorter(output_list_without_header)
        lolsorter.add_sort_field_by_position(6, 'datestringdelimiter-')
        sorted_output = lolsorter.sort()
        self.assertEqual(sorted_output,[
            [1, 2, 3, 7, 2, 6, '1-1-14'],
            [1, 2, 3, 7, 1, 7, '1-1-15']
        ])
        lolsorter.reverse_sort = True
        sorted_output = lolsorter.sort()
        self.assertEqual(sorted_output,[
            [1, 2, 3, 7, 1, 7, '1-1-15'],
            [1, 2, 3, 7, 2, 6, '1-1-14']
        ])

    def testCaseBasicNonHeaderTestNumberSort(self):
        output_list_without_header = [
            [1, 2, 3, 7, 1, 7, '1-1-15'],
            [1, 2, 3, 7, 2, 6, '1-1-14']
        ]
        lolsorter = list_of_lists_sorter(output_list_without_header)
        lolsorter.add_sort_field_by_position(5)
        sorted_output = lolsorter.sort()
        self.assertEqual(sorted_output, [
            [1, 2, 3, 7, 2, 6, '1-1-14'],
            [1, 2, 3, 7, 1, 7, '1-1-15']
        ])
        lolsorter.reverse_sort = True
        sorted_output = lolsorter.sort()
        self.assertEqual(sorted_output, [
            [1, 2, 3, 7, 1, 7, '1-1-15'],
            [1, 2, 3, 7, 2, 6, '1-1-14']
        ])

    def testCaseBasicHeaderTestDateSort(self):
        output_list_with_header = [
            ['field1','field2','field3','field4', 'field5', 'field6', 'datefield1'],
            [1, 2, 3, 7, 1, 7, '1-1-15'],
            [1, 2, 3, 7, 2, 6, '1-1-14']
        ]
        lolsorter2 = list_of_lists_sorter(output_list_with_header)
        lolsorter2.has_header = True
        lolsorter2.add_sort_field_by_header_field_name('datefield1', 'datestringdelimiter-')
        print("sortfields", lolsorter2.sort_fields)
        sorted_output = lolsorter2.sort()
        print("sorted", sorted_output)
        self.assertEqual(sorted_output, [
            ['field1', 'field2', 'field3', 'field4', 'field5', 'field6', 'datefield1'],
            [1, 2, 3, 7, 2, 6, '1-1-14'],
            [1, 2, 3, 7, 1, 7, '1-1-15']
        ])
        lolsorter2.reverse_sort = True
        sorted_output = lolsorter2.sort()
        self.assertEqual(sorted_output, [
            ['field1', 'field2', 'field3', 'field4', 'field5', 'field6', 'datefield1'],
            [1, 2, 3, 7, 1, 7, '1-1-15'],
            [1, 2, 3, 7, 2, 6, '1-1-14']
        ])

    def testCaseBasicNonHeaderTestNumberSort(self):
        output_list_with_header = [
            ['field1', 'field2', 'field3', 'field4', 'field5', 'field6', 'datefield1'],
            [1, 2, 3, 7, 1, 7, '1-1-15'],
            [1, 2, 3, 7, 2, 6, '1-1-14']
        ]
        lolsorter = list_of_lists_sorter(output_list_with_header)
        lolsorter.has_header = True
        lolsorter.add_sort_field_by_position(5)
        sorted_output = lolsorter.sort()
        self.assertEqual(sorted_output, [
            ['field1', 'field2', 'field3', 'field4', 'field5', 'field6', 'datefield1'],
            [1, 2, 3, 7, 2, 6, '1-1-14'],
            [1, 2, 3, 7, 1, 7, '1-1-15']
        ])
        lolsorter.reverse_sort = True
        sorted_output = lolsorter.sort()
        self.assertEqual(sorted_output, [
            ['field1', 'field2', 'field3', 'field4', 'field5', 'field6', 'datefield1'],
            [1, 2, 3, 7, 1, 7, '1-1-15'],
            [1, 2, 3, 7, 2, 6, '1-1-14']
        ])









