from student import Student
from course import Course

class Enrollment:
    def __init__(self, enroll_id, student, course): #, grade):
        self.enroll_id = enroll_id
        self.course = course
        self.student = student
        #self.grade = grade

    def __init__(self, enroll_id, student, course, grade):
        self.enroll_id = enroll_id
        self.course = course
        self.student = student
        self.grade = grade

    def display(self):
        print("=============================\n")
        print("Enroll ID: ", self.enroll_id)
        print("Course: ", self.course.title, self.course.course_id)
        print("Credit Hours: ", self.course.credit_hour)
        print("Student ID: ", self.student.student_id)
        print("Name: ", self.student.first_name, self.student.last_name, "\n")
        print("Grade: ", self.grade)

    def setGrade(self, grade):
        self.grade = grade