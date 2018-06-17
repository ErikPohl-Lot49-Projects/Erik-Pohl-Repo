from flask import Flask, request
from flask_restful import Resource, Api
from sqlalchemy import create_engine
from flask import jsonify
import json

db_connect = create_engine('sqlite:///faq.db')
app = Flask(__name__)
api = Api(app)


#refactor
#test cases
#multiple parameters to put
#delete


# https://stackoverflow.com/questions/24254945/internal-server-error-flask
# https://www.codementor.io/sagaragarwal94/building-a-basic-restful-api-in-python-58k02xsiq
#https://stackoverflow.com/questions/48095713/accepting-multiple-parameters-in-flask-restful-add-resource
# http://blog.luisrei.com/articles/flaskrest.html

class SortedQuestions(Resource):
    def get(self, sortby):
        conn = db_connect.connect()  # connect to database
        query = conn.execute("select q.*, sum(a.confirmationcount) question_value from questions q,"
                             "answers a where  q.question_id = a.question_id order by question_value desc")  # This line performs query and returns json result
        return {'descending list of questions': [i for i in query.cursor.fetchall()]
                }
    def post(self):
        pass
    def delete(self):
        pass

class AllQuestions(Resource):
        def get(self):
            conn = db_connect.connect()  # connect to database
            query = conn.execute("select q.*  from questions q;"
                                 )  # This line performs query and returns json result
            return {'allquestions': [i for i in query.cursor.fetchall()]
                    }
        def post(self):
            pass
        def delete(self):
            pass


class ConfirmedAnswers(Resource):
    def get(self, question_id):
        conn = db_connect.connect()  # connect to database
        query = conn.execute(
            "select q.question, a.answer, sum(a.confirmationcount) as answer_value from answers a, questions q where a.question_id = %d "
            "and q.question_id = a.question_id "
            "group by a.answer "
            "order by answer_value desc" % int(question_id)
        )
        return {'confirmed answers': [i for i in query.cursor.fetchall()]
                }

class Answer(Resource):
    def get(self, answer_id):
        conn = db_connect.connect()  # connect to database
        query = conn.execute(
            "select a.* from answers a where a.answer_id = %d "
             % int(answer_id)
        )
        return {'answer': [i for i in query.cursor.fetchall()]}
    def put(self, answer_id):
        conn = db_connect.connect()  # connect to database
        query = conn.execute(
            "select max(a.answer_id)+1 from answers a"
        )
        max_id = [i[0] for i in query.cursor.fetchall()][0]
        command = "insert into answers values(" + str(max_id) + ", 1, \'"+ answer_id + "\', 0,1,1);"
        query = conn.execute(
            command
        )
        return {int(max_id): answer_id}

class Question(Resource):
    def get(self, question_id):
        conn = db_connect.connect()  # connect to database
        query = conn.execute(
            "select q.* from questions q where q.question_id = %d "
             % int(question_id)
        )
        return {'question': [i for i in query.cursor.fetchall()]
                }
    def put(self, question_id):
        conn = db_connect.connect()  # connect to database
        query = conn.execute(
            "select max(q.question_id)+1 from questions q"
        )
        max_id = [i[0] for i in query.cursor.fetchall()][0]
        command = "insert into questions values(" + str(max_id) + ", \'"+ question_id + "\', 1,1);"
        query = conn.execute(
            command
        )
        return {int(max_id): question_id}



api.add_resource(SortedQuestions, '/sortedquestions/<sortby>')
api.add_resource(ConfirmedAnswers, '/confirmedanswers/<question_id>')
api.add_resource(Answer, '/answer/<answer_id>')
api.add_resource(Question, '/question/<question_id>')
api.add_resource(AllQuestions, '/allquestions/')


if __name__ == '__main__':
    app.run(port='5002')
