from collections import namedtuple
from datetime import date


class list_of_lists_sorter:
    '''
    This class allows you to flexibly define and execute sorts on lists of lists
    with and without headers
    with and without reverse sort
    '''
    sort_field = namedtuple('sort_field', 'position field_type')

    STRINGDATEPREFIX = 'datestringdelimiter'

    def __init__(self, list_of_lists):
        self.list_of_lists = list_of_lists
        self.sort_fields = []
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
            self.sort_fields.append(self.sort_field(self.list_of_lists[0].index(field_name), sort_field_type))

    def add_multiple_fields_by_position(self, position_type_list):
        '''
        add a multiple sort fields to the sort field criteria by position in the list, sort field type default is string
        '''
        for sort_field_add in position_type_list:
            if type(sort_field_add) is not tuple:
                sort_field_add = (sort_field_add, "string")
            self.sort_fields.append(self.sort_field(sort_field_add[0], sort_field_add[1]))

    def add_multiple_fields_by_position_list_comprehension(self, position_type_list):
        '''
        deprecated
        '''
        [self.sort_fields.append(self.sort_field(sort_field_add[0], sort_field_add[1]))
         if type(sort_field_add) is tuple
         else
         self.sort_fields.append(self.sort_field(sort_field_add, "string"))
         for sort_field_add in position_type_list]

    def add_multiple_fields_by_header_field(self, fieldheader_type_list):
        '''
        add a multiple sort fields to the sort field criteria by header field name in the list, sort field type default is string
        '''
        for sort_field_add in fieldheader_type_list:
            if type(sort_field_add) is not tuple:
                sort_field_add = (sort_field_add, "string")
            self.sort_fields.append((self.sort_field(self.list_of_lists[0].index(sort_field_add[0]), sort_field_add[1])))

    def add_multiple_fields_by_header_field_list_comprehension(self, position_type_list):
        '''
        deprecated
        '''
        [self.sort_fields.append(self.sort_field(self.list_of_lists[0].index(sort_field_add[0]), sort_field_add[1]))
         if type(sort_field_add) is tuple
         else
         self.sort_fields.append(self.sort_field(self.list_of_lists[0].index(sort_field_add), "string"))
         for sort_field_add in position_type_list]

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
            x = datetuple(*raw.split(field_type[-1]))
            return date(int(x.year), int(x.month), int(x.day))
        return raw

    def sort_choice(self, unsorted_list_row, sort_fields_to_apply):
        '''
        define the sort type based on the sort field list of criteria
        '''
        return [self.field_type_convert(unsorted_list_row[sort_field_to_apply.position], sort_field_to_apply.field_type)
                for sort_field_to_apply in sort_fields_to_apply]

    def sort(self):
        '''
        execute the sort based on all of the criteria and setups in the instantiation
        '''
        header_offset = int(self.has_header)
        if self.has_header:
            copyheader = self.list_of_lists[0]
        self.list_of_lists = self.list_of_lists[header_offset:]
        self.list_of_lists.sort(
            key=lambda row: self.sort_choice(row, self.sort_fields),
            reverse=self.reverse_sort)
        if self.has_header:
            self.list_of_lists[0:0] = [copyheader]
        return self.list_of_lists
