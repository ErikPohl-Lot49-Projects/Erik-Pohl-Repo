import io
import logging
import pickle
import sys
from unittest import TestCase

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
    class MockResponse:
        def __init__(self, endpoint_return):
            # from http://docs.python-requests.org/en/master/api/#requests.Response
            # set to None in a less didactic manner
            # The apparent encoding, provided by the chardet library
            self.apparent_encoding = None
            # Content of the response, in bytes.
            self.content = None
            # A CookieJar of Cookies the server sent back.
            self.cookies = None
            # Elapsed time sending request and getting response
            self.elapsed = None
            # Encoding to decode with when accessing r.text.
            self.encoding = None
            # Case-insensitive Dictionary of Response Headers.
            self.headers = None
            # A list of Response objects from the history of the Request.
            self.history = None
            # True if this Response one of the permanent versions of redirect.
            self.is_permanent_redirect = None
            # True if this Response is a well-formed HTTP redirect that could have been processed automatically
            self.is_redirect = None
            # Returns the parsed header links of the response, if any.
            self.links = None
            # Returns a PreparedRequest for the next request in a redirect chain, if there is one.
            self.next = None
            # Returns True if status_code is less than 400, False if not.
            self.ok = None
            # Textual reason of responded HTTP Status, e.g. “Not Found” or “OK”.
            self.reason = None
            # The PreparedRequest object to which this is a response.
            self.request = None
            # Integer Code of responded HTTP Status, e.g. 404 or 200.
            self.status_code = None
            # Content of the response, in unicode.
            self.text = None
            # Final URL location of Response.
            self.url = None
            for key, value in endpoint_return.items():
                setattr(self, key, value)

    currentcase = TestCase.currentcase
    endpointdata = TestCase.endpointdatasource

    if kwargs:
        # how do we iterate through testcases?
        endpoint = endpointdata[currentcase]
        endpoint_return = endpoint[kwargs['url']]
        return MockResponse(endpoint_return)  # make the return code more flexible
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
