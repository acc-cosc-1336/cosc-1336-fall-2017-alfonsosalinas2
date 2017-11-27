from transcript import Transcript
from school_initializer import SchoolInitializer
from school_db import SchoolDB

class Gradebook:


    def __init__(self, school_db):
        self.school_db = school_db
        self.enrollments = school_db.enrollments
        self.students = school_db.school_initializer.students

    def main(self):
        keep_going = 'y'

        while keep_going == 'y':
            print("Available Enroll IDs: ")
            for enrollment in self.enrollments.values():
                print(enrollment.enroll_id)

            enroll_key = int(input("\nEnter enroll key: "))

            if enroll_key in self.enrollments:
                enroll = self.enrollments.get(enroll_key)

                grade = input("Enter grade: ")
                enroll.grade = grade

            else:
                print("Key doesn't exist")

            keep_going = input("Enter y to continue...")

        for enrollment in self.enrollments.values():
            enrollment.print_record()

        print("\nAvailable Student IDs: ")
        for student in self.students.values():
            print(student.student_id)

        ask_student = 'y'

        while ask_student == 'y':
            student_id = int(input("\nEnter student id: "))
            student = self.students[student_id]
            transcript = Transcript(self.enrollments)
            transcript.print_transcript(student)

            ask_student = input("\nEnter y to search for another student: ")

        ask_print_all = input("\nWould you like to print all student transcripts? (y/n): ")
        if ask_print_all == 'y':
            transcript.print_all_transcripts(self.students)

        ask_print_all = input("\nWould you like to save enrollments? (y/n): ")
        if ask_print_all == 'y':
            self.school_db.save_data()

school_db = SchoolDB(SchoolInitializer())
gradebook = Gradebook(school_db)
gradebook.main()
