from student import Student
from enrollment import Enrollment

class Transcript:

    def __init__(self, enrollments, credit_points=0, grade_points=0):

        self.enrollments = enrollments
        self.credit_points = credit_points
        self.grade_points = grade_points

    def print_transcript(self, student):

        print("\nName: ", student.first_name + ' ' + student.last_name)
        print("Class\t\t\tCredit hours\t Credit Points\t Grades Points\t Grades")

        sum_credit_points = 0
        sum_grade_points = 0
        sum_credit_hours = 0

        for e in self.enrollments.values():

            credit_points = self.get_credit_points(e.grade)
            sum_credit_points += credit_points
            grade_points = credit_points * e.course.credit_hour
            sum_grade_points += grade_points
            sum_credit_hours += e.course.credit_hour

            if e.student.student_id == student.student_id:
                print(format(e.course.title, '20'), format(str(e.course.credit_hour), '18'),
                      format(str(credit_points), '14'), format(str(grade_points), '12'), e.grade)
                print("===" * 25)
                print(format(sum_credit_points, '22'), format(sum_grade_points, '34'))
                print("GPA: ", format((sum_grade_points / sum_credit_hours)*10, '.2f'))

    def print_all_transcripts(self, students):
        print("\nAll student transcripts: ")
        for student in students.values():
            self.print_transcript(student)

    def get_credit_points(self, letter_grade):

        credit_points = 0

        if letter_grade == 'A':
            credit_points = 4
        elif letter_grade == 'B':
            credit_points = 3
        elif letter_grade == 'C':
            credit_points = 2
        elif letter_grade == 'D':
            credit_points = 1

        return credit_points
