from sort import list_of_list_sorter

output_list_with_header = [
    ['zero', 'one', 'two', 'three', 'four', 'five', 'six'],
    [1, 2, 3, 7, 1, 7, '1-1-15'],
    [1, 2, 3, 7, 2, 6, '1-1-14'],
    [1, 2, 3, 5, 3, 5, '1-1-13'],
    [1, 2, 3, 4, 4, 4, '1-1-12'],
    [1, 2, 3, 3, 5, 3, '1-1-11'],
    [1, 2, 3, 2, 6, 2, '1-1-10'],
    [1, 2, 3, 1, 7, 1, '1-1-18']
]
sorter = list_of_list_sorter(output_list_with_header)
sorter.has_header = True
sorter.add_sort_field_by_header_field_name('six', 'datestringdel-')
print(sorter.sort())

output_list_without_header = [
    [1, 2, 3, 7, 1, 7, '1-1-15'],
    [1, 2, 3, 7, 2, 6, '1-1-14'],
    [1, 2, 3, 5, 3, 5, '1-1-13'],
    [1, 2, 3, 4, 4, 4, '1-1-12'],
    [1, 2, 3, 3, 5, 3, '1-1-11'],
    [1, 2, 3, 2, 6, 2, '1-1-10'],
    [1, 2, 3, 1, 7, 1, '1-1-18']
]
sorter = list_of_list_sorter(output_list_without_header)
sorter.has_header = False
sorter.reverse_sort = True
sorter.add_sort_field_by_position(6, 'datestringdel-')
print(sorter.sort())

output_list_without_header = [
    [1, 2, 3, 7, 1, 7, '1-1-15'],
    [1, 2, 3, 7, 2, 6, '1-1-14'],
    [1, 2, 3, 5, 3, 5, '1-1-13'],
    [1, 2, 3, 4, 4, 4, '1-1-12'],
    [1, 2, 3, 3, 5, 3, '1-1-11'],
    [1, 2, 3, 2, 6, 2, '1-1-10'],
    [1, 2, 3, 1, 7, 1, '1-1-18']
]
sorter = list_of_list_sorter(output_list_without_header)
sorter.has_header = False
sorter.reverse_sort = False
sorter.add_multiple_fields_by_position([(6, 'datestringdel-'), (4, 'int')])
print(sorter.sort())
