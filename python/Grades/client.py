import unittest
import json
import requests


url_base = 'http://127.0.0.1:5002'
url_students = url_base + '/Students'
url_courses = url_base + '/Courses'
url_grades = url_base + '/Grades'

class GradesTestCases(unittest.TestCase):
    def test_PutGetAndDeleteStudent(self):
        lname = 'Pohl'
        fname = 'Erik'
        expected_id = '1'
        created_by = 1
        creation_date = 1
        api_url = url_students+'/StudentLname/'+lname+'/StudentFname/'+fname
        r_put = requests.put(url=api_url)
        print(r_put.status_code, r_put.reason, r_put.text)
        api_url = url_students+'/'+expected_id
        r_get = requests.get(url=api_url)
        print(r_get.status_code, r_get.reason, r_get.text)
        print(r_get.text)
        api_url = url_students+'/'+expected_id
        r_delete = requests.delete(api_url)
        self.assertEqual(r_get.text,json.dumps({'student': [[int(expected_id), lname, fname, created_by, creation_date]]})+'\n')
        self.assertEqual(r_put.text,json.dumps({expected_id: fname+" "+lname})+'\n')
        self.assertEqual(r_delete.text, json.dumps({"deleted_student": expected_id})+'\n')

    def test_PutGetAndDeleteCourse(self):
        course_name = 'APIs'
        expected_id = '1'
        created_by = 1
        creation_date = 1
        prereq_id = 1
        api_url = url_courses+'/course_name/' + course_name +'/prereq_id/' +str(prereq_id)
        r_put = requests.put(url=api_url)
        print(r_put.status_code, r_put.reason, r_put.text)
        api_url = url_courses+'/'+expected_id
        r_get = requests.get(url=api_url)
        print(r_get.status_code, r_get.reason, r_get.text)
        api_url =  url_courses+'/'+expected_id
        r_delete = requests.delete(api_url)
        print(r_delete.status_code, r_delete.reason, r_delete.text)
        self.assertEqual(r_get.text,json.dumps({'course': [[int(expected_id), course_name, prereq_id, created_by, creation_date]]})+'\n')
        self.assertEqual(r_put.text,json.dumps({expected_id: course_name+" "+str(prereq_id)})+'\n')
        self.assertEqual(r_delete.text, json.dumps({"deleted_course": expected_id})+'\n')

    def test_putgetanddeletegrade(self):
        student_id = 1
        course_id = 1
        numeric_grade =90
        created_by = 1
        creation_date =1
        expected_id = '1'
        api_url = url_grades+'/student_id/1/course_id/1/numeric_grade/90'
        r_put = requests.put(url=api_url)
        print(r_put.status_code, r_put.reason, r_put.text)
        api_url = url_grades+'/1'
        r_get = requests.get(url=api_url)
        print(r_get.status_code, r_get.reason, r_get.text)
        api_url =  url_grades+'/1'
        r_delete = requests.delete(api_url)
        print(r_delete.status_code, r_delete.reason, r_delete.text)
        self.assertEqual(r_get.text,json.dumps({'grade': [[int(expected_id), student_id, course_id, numeric_grade, created_by, creation_date]]})+'\n')
        self.assertEqual(r_put.text,json.dumps({expected_id: str(student_id)+" "+str(course_id)+" "+str(numeric_grade)})+'\n')
        self.assertEqual(r_delete.text, json.dumps({"deleted_grade": expected_id})+'\n')


if __name__ == '__main__':
    unittest.main()
