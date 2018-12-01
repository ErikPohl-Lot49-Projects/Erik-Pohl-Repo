import json
import requests


url_base = 'http://127.0.0.1:5002'
url_students = url_base + '/Students'
url_courses = url_base + '/Courses'

def GetStudentAndCourse():
    api_url = url_students
    r_get_student = requests.get(url=api_url)
    print(r_get_student.status_code, r_get_student.reason, r_get_student.text)
    print(r_get_student.text)
    api_url = url_courses
    r_get_course = requests.get(url=api_url)
    print(r_get_course.status_code, r_get_course.reason, r_get_course.text)
    return r_get_student.text, r_get_course.text


if __name__ == '__main__':
    GetStudentAndCourse()
