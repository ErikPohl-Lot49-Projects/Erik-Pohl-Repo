from flask import Flask
from flask_restful import Resource, Api
from sqlalchemy import create_engine


db_connect = create_engine('sqlite:///grades.db')
app = Flask(__name__)
api = Api(app)

class Students(Resource):
    def get(self, student_id):
        conn = db_connect.connect()  # connect to database
        query = conn.execute(
            "select s.* from students s where s.student_id = %d;"
            % int(student_id)
        )
        return {'student': [i for i in query.cursor.fetchall()]}
    def delete(self,student_id):
        conn = db_connect.connect()  # connect to database
        query = conn.execute(
            "delete from students where student_id = %d"
            % int(student_id)
        )
        return {"deleted_student": student_id}

class AddStudent(Resource):
    def put(self, student_fname, student_lname):
        conn = db_connect.connect()  # connect to database
        query = conn.execute(
            "select max(s.student_id)+1 from students s"
        )
        max_id = [i[0] for i in query.cursor.fetchall()][0]
        if max_id is None:
            max_id = 1
        command = "insert into students values(" + str(max_id) + ", \'" + student_lname + "\', \'" + student_fname + "\', 1,1);"
        query = conn.execute(
            command
        )
        return {int(max_id): student_fname + " " + student_lname}

class Courses(Resource):
    def get(self, course_id):
        conn = db_connect.connect()  # connect to database
        query = conn.execute(
            "select c.* from courses c where c.course_id = %d;"
            % int(course_id)
        )
        return {'course': [i for i in query.cursor.fetchall()]
                }
    def delete(self,course_id):
        conn = db_connect.connect()  # connect to database
        query = conn.execute(
            "delete from courses where course_id = %d"
            % int(course_id)
        )
        return {"deleted_course": course_id}

class AddCourse(Resource):
    def put(self,course_name, prereq_id):
        conn = db_connect.connect()  # connect to database
        query = conn.execute(
            "select max(c.course_id)+1 from courses c"
        )
        max_id = [i[0] for i in query.cursor.fetchall()][0]
        if max_id is None:
            max_id = 1
        command = "insert into courses values(" + str(max_id) + ", \'" + course_name + "\', " + prereq_id + ", 1,1);"
        query = conn.execute(
            command
        )
        return {int(max_id): course_name + " " + str(prereq_id)}

class Grades(Resource):
    def get(self, grade_id):
        conn = db_connect.connect()  # connect to database
        query = conn.execute(
            "select g.* from grades g where g.grade_id = %d;"
            % int(grade_id)
        )
        return {'grade': [i for i in query.cursor.fetchall()]}
    def delete(self,grade_id):
        conn = db_connect.connect()  # connect to database
        query = conn.execute(
            "delete from grades where grade_id = %d"
            % int(grade_id)
        )
        return {"deleted_grade": grade_id}

class AddGrade(Resource):
    def put(self,student_id, course_id, numeric_grade):
        conn = db_connect.connect()  # connect to database
        query = conn.execute(
            "select max(g.grade_id)+1 from grades g"
        )
        max_id = [i[0] for i in query.cursor.fetchall()][0]
        if max_id is None:
            max_id = 1
        command = "insert into grades values(" + str(max_id) + ", " + str(student_id) + ", " + str(course_id) + ", " + str(numeric_grade) +",1,1);"
        query = conn.execute(
            command
        )
        return {int(max_id): str(student_id) + " " +course_id + " "+ str(numeric_grade)}

api.add_resource(Students, '/Students/<student_id>')
api.add_resource(AddStudent, '/Students/StudentLname/<student_lname>/StudentFname/<student_fname>')

api.add_resource(Courses, '/Courses/<course_id>')
api.add_resource(AddCourse, '/Courses/course_name/<course_name>/prereq_id/<prereq_id>/')

api.add_resource(Grades, '/Grades/<grade_id>')
api.add_resource(AddGrade, '/Grades/student_id/<student_id>/course_id/<course_id>/numeric_grade/<numeric_grade>')

if __name__ == '__main__':
    app.run(port='5002')