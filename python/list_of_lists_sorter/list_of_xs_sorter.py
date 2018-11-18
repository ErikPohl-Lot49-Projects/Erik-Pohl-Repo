#TODO use a design pattern to simplify this
from list_of_dicts_sorter import list_of_dicts_sorter
from list_of_lists_sorter import list_of_lists_sorter


class list_of_xs_sorter:

    def __init__(self, list_of_xs):
        self.list_of_xs = list_of_xs
        self.reverse_sort = False
        self.has_header = False
        self.sort_object = None

    def add_sort_field_by_field_name(self, field_name, field_type='string'):
        x = str(type(self.sort_object))
        print(x)
        if x == "<class 'list_of_lists_sorter.list_of_list_sorter'>":
            self.sort_object.has_header = self.has_header
            self.sort_object.add_sort_field_by_header_field_name(field_name, field_type)
        if x == "<class 'list_of_dicts_sorter.list_of_dicts_sorter'>":
            self.sort_object.add_sort_field_by_key_name(field_name, field_type)

    def sort_factory(self):
        print(type(self.list_of_xs[0]))
        if type(self.list_of_xs[0]) is list:
            self.sort_object = list_of_lists_sorter(self.list_of_xs)
        if type(self.list_of_xs[0]) is dict:
            print('dict sort factory')
            self.sort_object = list_of_dicts_sorter(self.list_of_xs)

    def sort(self):
        self.sort_object.list_of_dicts = self.list_of_xs
        self.sort_object.reverse_sort = self.reverse_sort
        self.sort_object.has_header = self.has_header
        return self.sort_object.sort()


surprise_me_sorter = list_of_xs_sorter([
    {'one': 1, 'two': 5},
    {'one': 1, 'two': 4}
])
surprise_me_sorter.sort_factory()
surprise_me_sorter.add_sort_field_by_field_name('two', 'string')
print(surprise_me_sorter.sort())

surprise_me_sorter = list_of_xs_sorter([
    ['one', 'two'],
    ['1', '5'],
    ['1', '4']
])
surprise_me_sorter.sort_factory()
surprise_me_sorter.has_header = True
surprise_me_sorter.add_sort_field_by_field_name('two', 'string')
print(surprise_me_sorter.sort())
