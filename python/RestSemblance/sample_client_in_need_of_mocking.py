import requests


url_base = 'http://127.0.0.1:5002'
url_students = url_base + '/Students'
url_courses = url_base + '/Courses'


def output_response(status_code, text):
    '''
    output results of requests get
    :param status_code: status code
    :param text: text of request get
    :return: True
    '''
    print(status_code, text)
    print(
        "status_code, text -->",
        status_code,
        text
    )
    return True


def perform_request(api_url):
    '''
    This will be mocked
    :param api_url: url to retrieve API data from using requests get
    :return:
    '''
    r_get_response = requests.get(url=api_url)
    output_response(r_get_response.status_code, r_get_response.text)
    return True


def GetStudentAndCourse():
    '''
    API requests to get Student and Course data
    :return: True
    '''
    perform_request(url_students)
    perform_request(url_courses)
    return True

if __name__ == '__main__':
    GetStudentAndCourse()
