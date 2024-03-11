from domains.student_management_system import StudentManagementSystem
from input import get_int_input, get_str_input, get_float_input
from output import display_message, display_student_info, display_course_info

system = StudentManagementSystem()
system.student_info()
system.courses_info()

while True:
    print("Select from 1 to 6: ")
    print("1. Input mark for student in the course: ")
    print("2. List student: ")
    print("3. List courses: ")
    print("4. Show student marks:")
    print("5. List students by GPA:")
    print("6. Exit")

    choice = get_int_input("Select a number: ")

    if choice == 1:
        system.input_mark()
    elif choice == 2:
        system.list_students()
    elif choice == 3:
        system.list_courses()
    elif choice == 4:
        system.showthemarkofstudent()
    elif choice == 5:
        system.list_students_by_gpa()
    elif choice == 6:
        print("Thanks for using this student management system")
        break
    else:
        print("Invalid choice")
