from collections import namedtuple
import datetime

class list_of_list_sorter:
    sort_field = namedtuple('sort_field', 'position type')
    sort_option = {'sort_fields': [], 'reverse': False}

    def __init__(self, list_of_lists):
        self.list_of_lists = list_of_lists
        self.sort_fields = []

    def add_sort_field(self, position, type):
        self.sort_fields.append(self.sort_field(position, type))
        self.sort_option['sort_fields'] = self.sort_fields

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
        return [self.field_type_convert(x[y.position],y.type) for y in its]

    def sort(self):
        self.list_of_lists.sort(
            key=lambda row: self.sort_choice(row,
                                             self.sort_option['sort_fields']),
                                            reverse=self.sort_option['reverse'])
        return self.list_of_lists


output_list = [
[1,2,3,7,1,7,'1-1-15'],
[1,2,3,7,2,6,'1-1-14'],
[1,2,3,5,3,5,'1-1-13'],
[1,2,3,4,4,4,'1-1-12'],
[1,2,3,3,5,3,'1-1-11'],
[1,2,3,2,6,2,'1-1-10'],
[1,2,3,1,7,1,'1-1-18']
]
sorter = list_of_list_sorter(output_list)
sorter.add_sort_field(6, 'datestringdel-')
print(sorter.sort())
