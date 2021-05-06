from 클래스만들기.사람모듈 import *

class Student(Person):

    def study(self):
        print('놀거면 공부해라!!!')

class Worker(Person):

    company = None

    def __init__(self, company):
        self.company = company

    def work(self):
        print('놀거면 일해라!!!')

if __name__ == '__main__':
    student = Student()
    student.name = "김길동"
    student.age = 20
    print(student)
    student.study()

    worker = Worker("mega")
    worker.name = "송길동"
    worker.age = 20
    print(worker)
    worker.work()
