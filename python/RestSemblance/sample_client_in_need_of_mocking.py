import requests


url_base = 'http://127.0.0.1:5002'
url_students = url_base + '/Students'
url_courses = url_base + '/Courses'


def output_response(status_code, text):
    print(status_code, text)
    print(
        "status_code, text -->",
        status_code,
        text
    )


def perform_request(api_url):
    r_get_response = requests.get(url=api_url)
    output_response(r_get_response.status_code, r_get_response.text)


def GetStudentAndCourse():
    perform_request(url_students)
    perform_request(url_courses)

if __name__ == '__main__':
    GetStudentAndCourse()
