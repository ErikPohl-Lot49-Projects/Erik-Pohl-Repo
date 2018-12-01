import pickle

endpointdatasource = {'TestCase1':
    {
        'http://127.0.0.1:5002/Students':
            {
                'json_value': '[{"Student":1},{"hello": 1}]',
                'return_value': '200'
            },
        'http://127.0.0.1:5002/Courses':
            {
                'json_value': '[{"Course":1},{"hello": 1}]',
                'return_value': '200'
            }
    }
    ,
    'TestCase2':
        {
            'http://127.0.0.1:5002/Students':
                {
                    'json_value': '[{"Student":2},{"hello": 1}]',
                    'return_value': '200'
                },
            'http://127.0.0.1:5002/Courses':
                {
                    'json_value': '[{"Course":2},{"hello": 1}]',
                    'return_value': '200'
                }
        }
}

with open("TestCaseFile.pickle","wb") as TestCaseFileHandle:
    TestCaseFileHandle.write(pickle.dumps(endpointdatasource))