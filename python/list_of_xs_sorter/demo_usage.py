from list_of_lists_sorter import list_of_lists_sorter
from list_of_string_lists_sorter import list_of_string_lists_sorter
from list_of_xs_sorter import  list_of_xs_sorter
from list_of_dicts_sorter import list_of_dicts_sorter

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
output_list_without_header = [
    [1, 2, 3, 7, 1, 7, '1-1-15'],
    [1, 2, 3, 7, 2, 6, '1-1-14'],
    [1, 2, 3, 5, 3, 5, '1-1-13'],
    [1, 2, 3, 4, 4, 4, '1-1-12'],
    [1, 2, 3, 3, 5, 3, '1-1-11'],
    [1, 2, 3, 2, 6, 2, '1-1-10'],
    [1, 2, 3, 1, 7, 1, '1-1-18']
]

sorter = list_of_lists_sorter(output_list_with_header)
sorter.has_header = True
sorter.add_sort_field_by_header_field_name('six', 'datestringdel-')
print(sorter.sort())

sorter.clear_sort_fields()
sorter.add_sort_field_by_position(6, 'datestringdel-')
sorter.has_header = False
sorter.reverse_sort = True
sorter.list_of_lists =output_list_without_header
print(sorter.sort())

sorter.clear_sort_fields()
sorter.add_multiple_fields_by_position([(6, 'datestringdel-'), (4)])
sorter.has_header = False
sorter.reverse_sort = False
sorter.list_of_lists =output_list_without_header
print(sorter.sort())

sorter = list_of_lists_sorter(output_list_with_header)
sorter.has_header = True
sorter.add_sort_field_by_header_field_name('five')
print(sorter.sort())

sorter.clear_sort_fields()
sorter.add_sort_field_by_position(6)
sorter.has_header = False
sorter.reverse_sort = True
sorter.list_of_lists =output_list_without_header
print(sorter.sort())


output_list_of_string_lists_with_header = [
    'zero one two three four five six',
    '1 2 3 7 1 7 1-1-15',
    '1 2 3 7 2 6 1-1-14',
    '1 2 3 5 3 5 1-1-13',
    '1 2 3 4 4 4 1-1-12',
    '1 2 3 3 5 3 1-1-11',
    '1 2 3 2 6 2 1-1-10',
    '1 2 3 1 7 1 1-1-18'
]
sorter = list_of_string_lists_sorter(output_list_of_string_lists_with_header, ' ')
sorter.has_header = True
sorter.string_list_delimiter = ' '
sorter.add_sort_field_by_header_field_name('six', 'datestringdel-')
sorter.reverse_sort = False
print(sorter.sort())


surprise_me_sorter = list_of_xs_sorter([
    {'one': 1, 'two': 5},
    {'one': 1, 'two': 4}
])
surprise_me_sorter.sort_factory()
surprise_me_sorter.add_sort_field_by_field_name('two', 'string')
z= surprise_me_sorter.sort()
#print(z)

surprise_me_sorter = list_of_xs_sorter([
    ['one', 'two'],
    ['1', '5'],
    ['1', '4']
])
surprise_me_sorter.sort_factory()
surprise_me_sorter.has_header = True
surprise_me_sorter.add_sort_field_by_field_name('two', 'string')
print(surprise_me_sorter.sort())


surprise_me_sorter = list_of_xs_sorter([
    'one two',
    '1 5',
    '1 4'
])
surprise_me_sorter.sort_factory()
surprise_me_sorter.has_header = True
surprise_me_sorter.add_sort_field_by_field_name('two', 'string')
print(surprise_me_sorter.sort())


print("list of dicts sorted and output as a list of lists or a list of string lists")
lod_sorter_list = list_of_dicts_sorter([
    {'one': '1', 'two': '5'},
    {'one': '1', 'two': '4'}
])
lod_sorter_list.add_sort_field_by_key_name('two', 'string')
z=lod_sorter_list.sort()
print(z)
lod_sorter_list.output_as_list_of = list
z= lod_sorter_list.sort()
print(z)
lod_sorter_list.output_as_list_of = str
z= lod_sorter_list.sort()
print(z)



print("list of lists sorted and output as a list of dicts or a list of string lists")
sorter = list_of_lists_sorter(output_list_with_header)
sorter.has_header = True
sorter.add_sort_field_by_header_field_name('six', 'datestringdel-')
sorter.output_as_list_of = dict
print(sorter.sort())

sorter = list_of_lists_sorter(output_list_with_header)
sorter.has_header = True
sorter.add_sort_field_by_header_field_name('six', 'datestringdel-')
sorter.output_as_list_of_string_delimiter = ' '
sorter.output_as_list_of = str
print(sorter.sort())



print("list of string lists sorted and output as a list of dicts or a list of lists")
output_list_of_string_lists_with_header = [
    'zero one two three four five six',
    '1 2 3 7 1 7 1-1-15',
    '1 2 3 7 2 6 1-1-14'
]
sorter = list_of_string_lists_sorter(output_list_of_string_lists_with_header, ' ')
sorter.has_header = True
sorter.string_list_delimiter = ' '
sorter.add_sort_field_by_header_field_name('six', 'datestringdel-')
sorter.reverse_sort = False
sorter.output_as_list_of = dict
print(sorter.sort())

output_list_of_string_lists_with_header = [
    'zero one two three four five six',
    '1 2 3 7 1 7 1-1-15',
    '1 2 3 7 2 6 1-1-14'
]
sorter = list_of_string_lists_sorter(output_list_of_string_lists_with_header, ' ')
sorter.has_header = True
sorter.string_list_delimiter = ' '
sorter.add_sort_field_by_header_field_name('six', 'datestringdel-')
sorter.reverse_sort = False
sorter.output_as_list_of = list
print(sorter.sort())



