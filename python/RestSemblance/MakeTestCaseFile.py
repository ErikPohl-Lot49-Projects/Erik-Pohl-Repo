# !/usr/bin/env python
# -*- coding: utf-8 -*-
import pickle

__author__ = "Erik Pohl"
__copyright__ = "None"
__credits__ = ["Erik Pohl"]
__license__ = "GPL"
__version__ = "1.0.0"
__maintainer__ = "Erik Pohl"
__email__ = "erik.pohl.444@gmail.com"
__status__ = "Beta"

# TODO: endpointdatasource ideally would come from a front-end application geared
# towards prompting non-technical folks
# to construct test cases for each API endpoint

endpointdatasource = {'TestCase1': {
    'urls': {
        'http://127.0.0.1:5002/Students': {
                'text': '[{"Student":1},{"hello": 1}]',
                'status_code': '200'
            },
        'http://127.0.0.1:5002/Courses': {
                'text': '[{"Course":1},{"hello": 1}]',
                'status_code': '200'
            }
    },
    'args': [1,2],
    'kwargs': {'c':3},
    'Expected_Output': True
    },
    'TestCase2': {
            'urls': {
            'http://127.0.0.1:5002/Students': {
                    'text': '[{"Student":2},{"hello": 1}]',
                    'status_code': '200'
                },
            'http://127.0.0.1:5002/Courses': {
                    'text': '[{"Course":2},{"hello": 1}]',
                    'status_code': '200'
                }
            },
    'args': [1,2],
    'kwargs': {'c':3},
    'Expected_Output': True

        }
}

# pickle it!

with open("TestCaseFile.pickle", "wb") as TestCaseFileHandle:
    TestCaseFileHandle.write(
        pickle.dumps(
            endpointdatasource
        )
    )
