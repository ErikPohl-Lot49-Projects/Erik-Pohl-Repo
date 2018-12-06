# !/usr/bin/env python
# -*- coding: utf-8 -*-
import io
import logging
import pickle
import sys
from types import SimpleNamespace
from unittest import TestCase

from SemblanceExceptions import UnrecognizedURLTestCase

__author__ = "Erik Pohl"
__copyright__ = "None"
__credits__ = ["Erik Pohl"]
__license__ = "GPL"
__version__ = "1.0.0"
__maintainer__ = "Erik Pohl"
__email__ = "erik.pohl.444@gmail.com"
__status__ = "Beta"

# TODO: Monkey patching [for Semblance]
# TODO: either make this work or back out thelooping logic back into the calling
#  unittest and let it handle expected results and parameters
# TODO: set case counter to 10 to make it blow up and test custom exception
# TODO: Semblance
# TODO:         Route faked DB / file?
# TODO:         mock function calls and such?
# TODO: check out references for inspiration for project growth
# TODO: allow changing file name
# TODO: consider liberating test cases from fixed nomenclature
# TODO: remove looping through all test cases from test script and put it here
# TODO: we must put the expected results for each case in the dictionary this way

def semblance_mocked_requests_get(*args, **kwargs):
    '''
    Get the response data for the mocked endpoint
    :param args: positional arguments to the mock side-effect
    :param kwargs: keyword arguments to the mock side-effect
    :return: response or error
    '''
    currentcase = TestCase.currentcase
    endpointdata = TestCase.endpointdatasource
    if kwargs:
        try:
            endpoint = endpointdata[currentcase]['urls']
        except:
            logging.critical(
                "Did not recognize the URL to be mocked: " + kwargs['url']
            )
            raise UnrecognizedURLTestCase
        endpoint_return = endpoint[kwargs['url']]
        MockedResponse = SimpleNamespace()
        for key, value in endpoint_return.items():
            setattr(MockedResponse, key, value)
        return MockedResponse
    else:
        print("no args")
    return True


def inccurrentcase():
    '''
    Increment test cases using
    a standard nomenclature
    :return: True
    '''
    for test_case in TestCase.endpointdatasource:
        TestCase.currentcase = test_case
        yield test_case
    raise StopIteration

def startCaptureOutput():
    '''
    deprecated: use the redirect context manager instead
    :return:
    '''
    '''
    Start capturing stdout output
    :return: True
    '''
    TestCase.capturedOutput = io.StringIO()
    sys.stdout = TestCase.capturedOutput
    return True


def stopCapturedOutput():
    '''
    deprecated: use the redirect context manager instead
    :return:
    '''
    '''
    End capturing stdout output
    and return it
    :return: captured stdout output
    '''
    sys.stdout = sys.__stdout__
    return TestCase.capturedOutput.getvalue()


def LoadCases():
    '''
    Loads test cases from a pickled dictionary
    Set current test case to first test case
    TestCaseFile.pickle
    :return: True
    '''

    TestCase.counter = 1
    TestCase.currentcase = 'TestCase' + str(TestCase.counter)
    # consider loading expected results so that it can be compared
    # against outputs what are outputs?
    with open("TestCaseFile.pickle", "rb") as Test_Case_File_Handle:
        TestCase.endpointdatasource = pickle.loads(
            Test_Case_File_Handle.read()
        )
    return True


class Semblance(TestCase):
    LoadCases()

    def all_mock_all_rest_api_cases(self, foo):
        for l in inccurrentcase():
            endpointdata = TestCase.endpointdatasource[l]
            xargs = endpointdata['args']
            xkwargs = endpointdata['kwargs']
            actual_result = foo(*xargs, **xkwargs)
            self.assertEqual(actual_result, endpointdata['Expected_Output'])
        return True

