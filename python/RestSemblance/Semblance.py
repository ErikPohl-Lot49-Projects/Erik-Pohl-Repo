from unittest import TestCase
import logging, sys, pickle
from SemblanceExceptions import UnrecognizedURLTestCase

# TODO: bundle this up so it can be used easily
# TODO: https://medium.com/@yeraydiazdiaz/what-the-mock-cheatsheet-mocking-in-python-6a71db997832
# TODO: https://code-maven.com/mocking-input-and-output-for-python-testing
# TODO: https://stackoverflow.com/questions/33767627/python-write-unittest-for-console-print
# TODO: https://necromuralist.github.io/posts/201310mocking-print/index.src.html
# TODO: https://realpython.com/python-cli-testing/
# TODO: Semblance
# TODO:         Route faked JSON from endpoints to test cases
# TODO:         Route faked screen output to test cases, capture output of actual process for testing
# TODO:         Route faked DB / file?


def semblance_mocked_requests_get(*args, **kwargs):
    class MockResponse:
        def __init__(self, json_data, status_code):
            self.json_data = json_data
            self.status_code = status_code
            self.text = json_data
            self.reason = 'This is part of the requests.get return to explain the reason for the status'
            # note we might need fake all aspects of that requests get return

    print(args, kwargs)
    currentcase = TestCase.currentcase
    endpointdata = TestCase.endpointdatasource

    if kwargs:
        print("evaluating for the url passed to the mock")
        # how do we iterate through testcases?
        endpoint = endpointdata[currentcase]
        endpoint_return = endpoint[kwargs['url']]
        endpoint_json_return = endpoint_return['json_value']
        endpoint_ret_value = endpoint_return['return_value']
        return MockResponse(endpoint_json_return, endpoint_ret_value)  # make the return code more flexible
    else:
        logging.critical("Did not recognize the URL to be mocked: " + args[0])
        raise UnrecognizedURLTestCase

def inccurrentcase():
    TestCase.counter += 1
    TestCase.currentcase = 'TestCase' + str(TestCase.counter)
    try:
        TestCase.endpointdatasource[TestCase.currentcase]
    except:
        raise StopIteration


def LoadCases():
    TestCase.counter = 1
    TestCase.currentcase = 'TestCase' + str(TestCase.counter)
    # consider loading expected results so that it can be compared against outputs what are outputs?
    with open("TestCaseFile.pickle", "rb") as Test_Case_File_Handle:
        TestCase.endpointdatasource = pickle.loads(Test_Case_File_Handle.read())

class Semblance(TestCase):
    LoadCases()








