import pickle

endpointdatasource = {'TestCase1':
    {
        'http://127.0.0.1:5002/Students':
            {
                'text': '[{"Student":1},{"hello": 1}]',
                'status_code': '200'
            },
        'http://127.0.0.1:5002/Courses':
            {
                'text': '[{"Course":1},{"hello": 1}]',
                'status_code': '200'
            }
    }
    ,
    'TestCase2':
        {
            'http://127.0.0.1:5002/Students':
                {
                    'text': '[{"Student":2},{"hello": 1}]',
                    'status_code': '200'
                },
            'http://127.0.0.1:5002/Courses':
                {
                    'text': '[{"Course":2},{"hello": 1}]',
                    'status_code': '200'
                }
        }
}

with open("TestCaseFile.pickle","wb") as TestCaseFileHandle:
    TestCaseFileHandle.write(pickle.dumps(endpointdatasource))
