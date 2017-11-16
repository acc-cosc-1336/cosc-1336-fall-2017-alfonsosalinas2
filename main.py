from gradebook import Gradebook


grade_book = Gradebook()

choice = 'Y'
while (choice == 'Y'):
    enroll_invalid = True
    while enroll_invalid:
        enroll_id = input("\nEnter enrollment ID: ")
        if enroll_id.isdigit():
            enroll_id = int(enroll_id)
            enroll_invalid = False

    grade_invalid = True
    while grade_invalid:
        grade = input("Enter a grade: ")
        if grade.isalpha():
            grade = grade.upper()
            grade_invalid = False

    e = grade_book.enrollments[enroll_id]
    #e.display()
    e.setGrade(grade)
    print("Updated Grade:")
    e.display()
    choice = input("\nDo you want to make another change? (Y/N) ")
    while not(choice == 'Y' or choice == 'N'):
        choice = input("Please enter Y or N: ")


#print gradebook
for e in grade_book.enrollments.values():
    e.display()


