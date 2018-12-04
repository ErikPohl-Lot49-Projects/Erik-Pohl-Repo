# !/usr/bin/env python
# -*- coding: utf-8 -*-
from unittest import mock
import logging
import sys
from sample_client_in_need_of_mocking import GetStudentAndCourse
from Semblance import Semblance, semblance_mocked_requests_get, inccurrentcase
from Semblance import startCaptureOutput, stopCapturedOutput

__author__ = "Erik Pohl"
__copyright__ = "None"
__credits__ = ["Erik Pohl"]
__license__ = "GPL"
__version__ = "1.0.0"
__maintainer__ = "Erik Pohl"
__email__ = "erik.pohl.444@gmail.com"
__status__ = "Beta"

class MyTestCases(Semblance):
    '''
    Demo usage for Semblance
    '''
    @mock.patch('sample_client_in_need_of_mocking.requests.get',
                side_effect=semblance_mocked_requests_get)
    def testWithMockValidJSon(self, *args, **kwargs):
        '''
        test incrementing through test cases
        using mocked endpoints
        :param args: not needed
        :param kwargs: not needed
        :return: True
        '''
        for _ in inccurrentcase():
            GetStudentAndCourse()
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
