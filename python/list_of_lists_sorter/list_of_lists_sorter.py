from collections import namedtuple
from datetime import date


class list_of_list_sorter:
    sort_field = namedtuple('sort_field', 'position field_type')

    STRINGDATEPREFIX = 'datestringdelimiter'

    def __init__(self, list_of_lists):
        self.list_of_lists = list_of_lists
        self.sort_fields = []
        self.reverse_sort = False
        self.has_header = False

    def add_sort_field_by_position(self, column_position, sort_field_type="string"):
        self.sort_fields.append(self.sort_field(column_position, sort_field_type))

    def add_sort_field_by_header_field_name(self, field_name, sort_field_type="string"):
        if self.has_header:
            self.sort_fields.append(self.sort_field(self.list_of_lists[0].index(field_name), sort_field_type))

    def add_multiple_fields_by_position(self, position_type_list):
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

    def add_multiple_fields_by_header_field(self, position_type_list):
        for sort_field_add in position_type_list:
            if type(sort_field_add) is not tuple:
                sort_field_add = (sort_field_add, "string")
            self.sort_fields.append(self.sort_field(self.list_of_lists[0].index(sort_field_add[0]), sort_field_add[1]))

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
        self.sort_fields = []

    def field_type_convert(self, raw, field_type):
        datetuple = namedtuple('datetuple', 'month day year')
        if field_type.startswith(self.STRINGDATEPREFIX):
            return datetuple(*raw.split(field_type[-1]))
        return raw

    def sort_choice(self, x, its):
        return [self.field_type_convert(x[y.position], y.field_type) for y in its]

    def sort(self):
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
