import gzip
import os

from domains.student_management_system import StudentManagementSystem
from input import get_int_input, get_str_input, get_float_input
from output import display_message, display_student_info, display_course_info

if os.path.exists("students.dat"):
    compressed_file_path = "students.dat"
    decompressed_file_path = "students.txt"

    with gzip.open(compressed_file_path, "rt") as compressed_file:
        data = compressed_file.read()

    with open(decompressed_file_path, "w") as decompressed_file:
        decompressed_file.write(data)

else:
    system = StudentManagementSystem()
    system.student_info()
    system.courses_info()

# Main loop
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

        compression_method = input("Select a compression method (gzip, zip, etc.): ")

        if compression_method == "gzip":
            with open(decompressed_file_path, "r") as decompressed_file:
                data = decompressed_file.read()

            with gzip.open(compressed_file_path, "wt") as compressed_file:
                compressed_file.write(data)

        break
    else:
        print("Invalid choice")
