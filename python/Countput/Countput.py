'''
Created on Dec 14, 2018

@author: Erik Pohl
'''
from collections import Counter, OrderedDict
import sys
import re


class Countput(Counter):

    def _version_greater_than_or_equal(self, version1, version2):
        def normalize(version_info):
            return [
                int(version_component)
                for version_component
                in re.sub(
                    r'(\.0+)*$', '', version_info).split(".")
            ]
        return normalize(version1) >= normalize(version2)

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
        if self._version_greater_than_or_equal(
                '.'.join(
                    (
                            str(
                                sys.version_info.major
                            ),
                            str(
                                sys.version_info.minor
                            ),
                            str(
                                sys.version_info.micro
                            )
                    )
                ),
                "3.7.1"
        ):
            return_dictionary = {}
        else:
            return_dictionary = OrderedDict()
        return_dictionary.update(
            {
                frequency_tuple[0]: frequency_tuple[1]
                for frequency_tuple
                in self.most_common()
            }
        )
        return dict(return_dictionary)
