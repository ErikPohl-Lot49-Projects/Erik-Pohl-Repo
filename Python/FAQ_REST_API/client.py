import json
import requests

import socket
#socket.getaddrinfo('localhost', 8080)

answer_id = "hello"
max_id = 2
command = "insert into answers values(" + str(max_id) + ", 1, \'"+ answer_id + "\', 0,1,1);"

api_url = 'http://127.0.0.1:5002/sortedquestions/1'
r = requests.get(url=api_url)
print(r.status_code, r.reason, r.text)

api_url = 'http://127.0.0.1:5002/answer/hello'
r = requests.put(url=api_url)
print(r.status_code, r.reason, r.text)

api_url = 'http://127.0.0.1:5002/question/example_question1'
r = requests.put(url=api_url)
print(r.status_code, r.reason, r.text)

api_url = 'http://127.0.0.1:5002/confirmedanswers/1'
r = requests.get(url=api_url)
print(r.status_code, r.reason, r.text)

api_url = 'http://127.0.0.1:5002/allquestions/'
r = requests.get(url=api_url)
print(r.status_code, r.reason, r.text)

api_url = 'http://127.0.0.1:5002/question/This%20question%20has%20spaces%20in%20it!'
r = requests.put(url=api_url)
print(r.status_code, r.reason, r.text)

api_url = 'http://127.0.0.1:5002/allquestions/'
r = requests.get(url=api_url)
print(r.status_code, r.reason, r.text)

