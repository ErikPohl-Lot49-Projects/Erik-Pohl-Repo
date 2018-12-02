from unittest import mock
import logging
import sys
from sample_client_in_need_of_mocking import GetStudentAndCourse
from Semblance import Semblance, semblance_mocked_requests_get, inccurrentcase
from Semblance import startCaptureOutput, stopCapturedOutput


class MyTestCases(Semblance):
    '''
    Demo usage for Semblance
    '''
    @mock.patch('sample_client_in_need_of_mocking.requests.get',
                side_effect=semblance_mocked_requests_get)
    def testWithMockValidJSon(self, *args, **kwargs):
        '''
        test incremeneting through test cases
        using mocked endpoints
        :param args: not needed
        :param kwargs: not needed
        :return: True
        '''
        try:
            while True:
                print("Incremented to ", Semblance.currentcase)
                GetStudentAndCourse()
                inccurrentcase()
        except:
            pass
        return True

    def test_capture_stdout(self, *args, **kwargs):
        '''
        tests capturing stdout output using Semblance
        :param args: not needed
        :param kwargs: not needed
        :return: captured output
        '''
        startCaptureOutput()
        print("hello")
        capout = stopCapturedOutput()
        print("captured -->", capout)
        self.assertEqual("hello\n", capout)

    # set up logging for all cases
    logging.basicConfig(stream=sys.stderr, level=logging.INFO)
    logging.basicConfig(stream=sys.stdout, level=logging.DEBUG)
    logging.basicConfig(stream=sys.stdout, level=logging.CRITICAL)
