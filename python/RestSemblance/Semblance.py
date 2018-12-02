import io
import logging
import pickle
import sys
from unittest import TestCase
from types import SimpleNamespace

from SemblanceExceptions import UnrecognizedURLTestCase

# TODO: https://medium.com/@yeraydiazdiaz/what-the-mock-cheatsheet-mocking-in-python-6a71db997832
# TODO: https://code-maven.com/mocking-input-and-output-for-python-testing
# TODO: https://stackoverflow.com/questions/33767627/python-write-unittest-for-console-print
# TODO: https://necromuralist.github.io/posts/201310mocking-print/index.src.html
# TODO: https://realpython.com/python-cli-testing/
# TODO: Semblance
# TODO:         Route faked DB / file?
# TODO:         mock function calls and such?


def semblance_mocked_requests_get(*args, **kwargs):
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
        logging.critical("Did not recognize the URL to be mocked: " + kwargs['url'])
        raise UnrecognizedURLTestCase


def inccurrentcase():
    # do this far more gracefully
    TestCase.counter += 1
    TestCase.currentcase = 'TestCase' + str(TestCase.counter)
    try:
        TestCase.endpointdatasource[TestCase.currentcase]
    except:
        raise StopIteration


def startCaptureOutput():
    TestCase.capturedOutput = io.StringIO()
    sys.stdout = TestCase.capturedOutput


def stopCapturedOutput():
    sys.stdout = sys.__stdout__
    return TestCase.capturedOutput.getvalue()


def LoadCases():
    TestCase.counter = 1
    TestCase.currentcase = 'TestCase' + str(TestCase.counter)
    # consider loading expected results so that it can be compared against outputs what are outputs?
    with open("TestCaseFile.pickle", "rb") as Test_Case_File_Handle:
        TestCase.endpointdatasource = pickle.loads(Test_Case_File_Handle.read())


class Semblance(TestCase):
    LoadCases()
