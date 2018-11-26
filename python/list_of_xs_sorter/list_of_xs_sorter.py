# !/usr/bin/env python
# -*- coding: utf-8 -*-
from list_of_dicts_sorter import list_of_dicts_sorter
from list_of_lists_sorter import list_of_lists_sorter
from list_of_string_lists_sorter import list_of_string_lists_sorter

__author__ = "Erik Pohl"
__copyright__ = "None"
__credits__ = ["Erik Pohl"]
__license__ = "GPL"
__version__ = "1.0.0"
__maintainer__ = "Erik Pohl"
__email__ = "erik.pohl.444@gmail.com"
__status__ = "Beta"

# TODO use a design pattern to simplify this


class list_of_xs_sorter:

    def __init__(self, list_of_xs):
        self.list_of_xs = list_of_xs
        self.reverse_sort = False
        self.string_list_delimiter = ' '  # current assumption is
        # space delimiter -- this is not cool
        self.has_header = False
        self.sort_object = None
        self.class_of_xs_sorter = "<class '{z}.{z}'>".format(
            z="list_of_{xs}_sorter"
        )
        self.class_losl_sorter = self.class_of_xs_sorter.format(
            xs="string_lists"
        )
        self.class_lol_sorter = self.class_of_xs_sorter.format(
            xs="lists"
        )
        self.class_lod_sorter = self.class_of_xs_sorter.format(
            xs="dicts"
        )

    def add_sort_field_by_field_name(self, field_name, field_type='string'):
        list_of_what_sorter = str(type(self.sort_object))
        if list_of_what_sorter in (
                self.class_lol_sorter,
                self.class_losl_sorter
        ):
            self.sort_object.has_header = self.has_header
            self.sort_object.add_sort_field_by_header_field_name(
                field_name,
                field_type
            )
        if list_of_what_sorter == self.class_lod_sorter:
            self.sort_object.add_sort_field_by_key_name(field_name, field_type)

    def sort_factory(self):
        if type(self.list_of_xs[0]) is list:
            self.sort_object = list_of_lists_sorter(self.list_of_xs)
        if type(self.list_of_xs[0]) is dict:
            self.sort_object = list_of_dicts_sorter(self.list_of_xs)
        if type(self.list_of_xs[0]) is str:
            self.sort_object = list_of_string_lists_sorter(
                self.list_of_xs,
                self.string_list_delimiter
            )

    def sort(self):
        self.sort_object.reverse_sort = self.reverse_sort
        self.sort_object.has_header = self.has_header
        list_of_what_sorter = str(type(self.sort_object))
        if list_of_what_sorter == self.class_losl_sorter:
            self.sort_object.string_list_delimiter = self.string_list_delimiter
        return self.sort_object.sort()
