from collections import namedtuple
from datetime import date


class list_of_dicts_sorter:
    '''
    This class allows you to flexibly define and execute sorts on lists of dicts
    with and without reverse sort
    '''
    sort_field = namedtuple('sort_field', 'key_name field_type')

    STRINGDATEPREFIX = 'datestringdelimiter'

    def __init__(self, list_of_dicts):
        self.list_of_dicts = list_of_dicts
        self.sort_fields = []
        self.reverse_sort = False

    def add_sort_field_by_key_name(self, field_name, sort_field_type="string"):
        '''
        add a sort field to the sort field criteria by key name in the dict, sort field type default is string
        '''
        #print(field_name, sort_field_type)
        self.sort_fields.append(self.sort_field(field_name, sort_field_type))

    def add_multiple_fields_by_key_names(self, key_type_list):
        '''
        add a multiple sort fields to the sort field criteria by key name in the dict, sort field type default is string
        '''
        for sort_field_add in key_type_list:
            if type(sort_field_add) is not tuple:
                sort_field_add = (sort_field_add, "string")
            print("add_multiple_fields_by_key_names given ", key_type_list)
            self.sort_fields.append((sort_field_add[0], sort_field_add[1]))

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
            return date(int(x.year), int(x.month),   int(x.day))

        return raw

    def sort_choice(self, unsorted_dict_row, sort_fields_to_apply):
        '''
        define the sort type based on the sort field list of criteria
        '''
        return [self.field_type_convert(unsorted_dict_row[sort_field_to_apply.key_name], sort_field_to_apply.field_type)
                for sort_field_to_apply in sort_fields_to_apply]

    def sort(self):
        '''
        execute the sort based on all of the criteria and setups in the instantiation
        '''
        return sorted(self.list_of_dicts, key=lambda row: self.sort_choice(row, self.sort_fields), reverse=self.reverse_sort)

