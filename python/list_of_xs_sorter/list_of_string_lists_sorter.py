from collections import namedtuple
from datetime import date
from list_of_lists_sorter import list_of_lists_sorter
from list_of_xs_converter import list_of_xs_converter

#TODO: infer delimiter?
#TODO: add regression tests
class list_of_string_lists_sorter:
    '''
    This class allows you to flexibly define and execute sorts on lists of string lists
    with and without headers
    with and without reverse sort
    '''
    sort_field = namedtuple('sort_field', 'position field_type')

    STRINGDATEPREFIX = 'datestringdelimiter'


    def __init__(self, list_of_string_lists, string_list_delimiter):
        self.list_of_string_lists = list_of_string_lists
        self.string_list_delimiter = string_list_delimiter
        self.sort_fields = []
        self.output_as_list_of = str
        self.reverse_sort = False
        self.has_header = False


    def add_sort_field_by_position(self, column_position, sort_field_type="string"):
        '''
        add a sort field to the sort field criteria by position in the list, sort field type default is string
        '''
        self.sort_fields.append(self.sort_field(column_position, sort_field_type))

    def add_sort_field_by_header_field_name(self, field_name, sort_field_type="string"):
        '''
        add a sort field to the sort field criteria by header field name in the list, sort field type default is string
        '''
        if self.has_header:
            self.sort_fields.append(self.sort_field(self.list_of_string_lists[0].split(self.string_list_delimiter)
                                                    .index(field_name), sort_field_type))

    def add_multiple_fields_by_position(self, position_type_list):
        '''
        add a multiple sort fields to the sort field criteria by position in the list, sort field type default is string
        '''
        for sort_field_add in position_type_list:
            if type(sort_field_add) is not tuple:
                sort_field_add = (sort_field_add, "string")
            self.sort_fields.append(self.sort_field(sort_field_add[0], sort_field_add[1]))

    def add_multiple_fields_by_header_field(self, header_type_list):
        '''
        add a multiple sort fields to the sort field criteria by header field name in the list, sort field type default is string
        '''
        for sort_field_add in header_type_list:
            if type(sort_field_add) is not tuple:
                sort_field_add = (sort_field_add, "string")
            self.sort_fields.append(self.sort_field(self.list_of_lists[0].split(self.string_list_delimiter)
                                                    .index(sort_field_add[0]), sort_field_add[1]))

    def clear_sort_fields(self):
        '''
        clear the sort fields criteria list
        '''
        self.sort_fields = []

    def field_type_convert(self, raw, field_type):
        '''
        convert the field data from string to a date if applicable
        '''
        datetuple = namedtuple('datetuple', 'month day year')
        if field_type.startswith(self.STRINGDATEPREFIX):
            return datetuple(*raw.split(field_type[-1]))
        return raw

    def sort(self):
        '''
        execute the sort based on all of the criteria and setups in the instantiation
        '''
        xvert_list = [i.split(self.string_list_delimiter) for i in self.list_of_string_lists]
        self._list_of_lists_sorter = list_of_lists_sorter(xvert_list)
        self._list_of_lists_sorter.has_header = self.has_header
        self._list_of_lists_sorter.reverse_sort = self.reverse_sort
        self._list_of_lists_sorter.sort_fields = self.sort_fields
        unxvert_list = [self.string_list_delimiter.join(i) for i in self._list_of_lists_sorter.sort()]
        return list_of_xs_converter(list_of_xs=unxvert_list,
                                    to_list_of=self.output_as_list_of,
                                    output_as_string_delimiter= self.string_list_delimiter)
