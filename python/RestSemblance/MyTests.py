from Semblance import Semblance, semblance_mocked_requests_get, inccurrentcase
from unittest import mock
import logging, sys
from sample_client_in_need_of_mocking import GetStudentAndCourse


class MyTestCases(Semblance):
    # change location of get command
    @mock.patch('sample_client_in_need_of_mocking.requests.get', side_effect=semblance_mocked_requests_get)
    def testWithMockValidJSon(self,*args, **kwargs):
        try:
            while True:
                print("Incremented to ", Semblance.currentcase)
                x, y = GetStudentAndCourse()
                inccurrentcase()
        except:
            pass

    # set up logging for all cases
    logging.basicConfig(stream=sys.stderr, level=logging.INFO)
    logging.basicConfig(stream=sys.stdout, level=logging.DEBUG)
    logging.basicConfig(stream=sys.stdout, level=logging.CRITICAL)
