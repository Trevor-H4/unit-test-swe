import User
import pytest
import System

class Student(User.User):
    def __init__(self, name,users,courses):
        self.users = users
        self.all_courses = courses
        self.name = name
        self.courses = self.users[name]['courses']
        self.password = self.users[name]['password']

    def submit_assignment(self,course,assignment_name,submission,submission_date):
        due_date = self.all_courses['comp_sci']['assignments'][assignment_name]["due_date"]
        submission = {assignment_name: {
          "grade": 'N/A',
          "submission_date": submission_date,
          "submission": submission,
            "ontime": self.check_ontime(submission_date,due_date)
        }}
        self.users[self.name]['courses'][course].update(submission)
        self.update_user_db()

    def check_grades(self,course):
        name = self.name
        assignments = self.users[name]['courses'][course]
        grades = []
        for key in assignments:
            grades.append([key, assignments[key]['grade']])
        return grades

    def view_assignments(self,course):
        course = self.all_courses['comp_sci']['assignments']
        assignments = []
        for key in course:
            assignments.append([key,course[key]['due_date']])
        return assignments

    def check_ontime(self,submission_date,due_date):
        return True

def test_check_ontime(grading_system):
    username = ''
    password = ''
    grading_system.login(username,password)

def test_submit_assignment(grading_system):
    username = None
    password = None
    grading_system.login(username,password)

def test_check_grades(grading_system):
    username = ''
    password = ''
    grading_system.login(username,password)

def test_view_assignments(grading_system):
    username = None
    password = None
    grading_system.login(username,password)

@pytest.fixture
def grading_system():
    gradingSystem = System.System()
    gradingSystem.load_data()
    return gradingSystem

