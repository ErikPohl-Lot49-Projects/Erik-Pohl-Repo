from collections import namedtuple
import datetime


class list_of_list_sorter:
    sort_field = namedtuple('sort_field', 'position type')

    def __init__(self, list_of_lists):
        self.list_of_lists = list_of_lists
        self.sort_fields = []
        self.reverse_sort = False
        self.has_header = False

    def add_sort_field_by_position(self, position, type):
        self.sort_fields.append(self.sort_field(position, type))

    def add_sort_field_by_header_field_name(self, field_name, type):
        if self.has_header:
            self.sort_fields.append(self.sort_field(self.list_of_lists[0].index(field_name), type))

    def add_multiple_fields_by_position(self, postypelist):
        for sort_field_add in postypelist:
            self.sort_fields.append(self.sort_field(sort_field_add[0], sort_field_add[1]))

    def add_multiple_fields_by_header_field(self, postypelist):
        for sort_field_add in postypelist:
            self.sort_fields.append(self.sort_field(self.list_of_lists[0].index(sort_field_add[0]), sort_field_add[1]))

    def clear_sort_fields(self):
        self.sort_option['sort_fields'] = []

    def field_type_convert(self, raw, ftype):
        if ftype.startswith('datestringdel'):
            return (datetime.date
                (
                int(raw.split(ftype[-1])[2]),
                int(raw.split(ftype[-1])[0]),
                int(raw.split(ftype[-1])[1])
            )
            )
        return raw

    def sort_choice(self, x, its):
        return [self.field_type_convert(x[y.position], y.type) for y in its]

    def sort(self):
        header_offset = int(self.has_header)
        copy = self.list_of_lists[0]
        self.list_of_lists = self.list_of_lists[header_offset:]
        self.list_of_lists.sort(
            key=lambda row: self.sort_choice(row, self.sort_fields),
            reverse=self.reverse_sort)
        if self.has_header:
            self.list_of_lists[0:0] = copy
        return self.list_of_lists
