import io
import logging
import pickle
import sys
from unittest import TestCase
from types import SimpleNamespace

from SemblanceExceptions import UnrecognizedURLTestCase

# TODO: Semblance
# TODO:         Route faked DB / file?
# TODO:         mock function calls and such?
# TODO: check out references for inspiration for project growth
# TODO: allow changing file name
# TODO: consider liberating test cases from fixed nomenclature


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
        endpoint = endpointdata[currentcase]
        endpoint_return = endpoint[kwargs['url']]
        MockedResponse = SimpleNamespace()
        for key, value in endpoint_return.items():
            setattr(MockedResponse, key, value)
        return MockedResponse
    else:
        logging.critical(
            "Did not recognize the URL to be mocked: " + kwargs['url']
        )
        raise UnrecognizedURLTestCase
    return True


def inccurrentcase():
    '''
    Increment test cases using
    a standard nomenclature
    :return: True
    '''
    # do this far more gracefully
    TestCase.counter += 1
    TestCase.currentcase = 'TestCase' + str(TestCase.counter)
    try:
        TestCase.endpointdatasource[TestCase.currentcase]
    except:
        raise StopIteration
    return True


def startCaptureOutput():
    '''
    Start capturing stdout output
    :return: True
    '''
    TestCase.capturedOutput = io.StringIO()
    sys.stdout = TestCase.capturedOutput
    return True


def stopCapturedOutput():
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
