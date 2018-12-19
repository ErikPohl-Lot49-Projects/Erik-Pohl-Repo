# !/usr/bin/env python
# -*- coding: utf-8 -*-
'''
Created on Dec 14, 2018

@author: Erik Pohl
'''
from collections import Counter, OrderedDict
import sys
import re
# this is problematic, so I won't use it
# from ..version_compare import version_compare

class version_compare:

    def __init__(self):
        self._current_version = sys.version.split(' ')[0]

    def current_version_greater_than_or_equal_than(self,compare_version):
        def normalize(version_info):
            return [
                int(version_component)
                for version_component
                in re.sub(
                    r'(\.0+)*$', '', version_info).split(".")
            ]
        return normalize(self._current_version) >= normalize(compare_version)

class Countput(Counter):

    def return_topn_as_list_of_strings(
            self,
            *,
            n=None,
            delimiter=' ',
            prefix='',
            suffix='',
            header=None
    ):
        headless_horseman = [
            prefix + delimiter.join(
                [
                    str(
                        frequency_data
                    )
                    for frequency_data
                    in frequency_tuple
                ]
            ) + suffix
            for frequency_tuple
            in self.most_common(n)
        ]
        return [header] + headless_horseman if header else headless_horseman

    def formatted_topn_output(
            self,
            *,
            n=None,
            delimiter=' ',
            prefix='',
            suffix='',
            header=None
    ):
        if header:
            print(header)
        [
            print(
                prefix + delimiter.join(
                    [
                        str(
                            frequency_data
                        )
                        for frequency_data
                        in frequency_tuple
                    ]
                ) + suffix
            )
            for frequency_tuple
            in self.most_common(n)
        ]

    def return_as_dict(self):
        # do something different for versions of Python
        # where the dictionary is not automatically ordered

        VC = version_compare();
        # adding to an ordered dict takes 75% more time
        return_dictionary = {} if VC.current_version_greater_than_or_equal_than("3.7.1") else OrderedDict()
        return_dictionary.update(
            {
                frequency_tuple[0]: frequency_tuple[1]
                for frequency_tuple
                in self.most_common()
            }
        )
        return dict(return_dictionary)
