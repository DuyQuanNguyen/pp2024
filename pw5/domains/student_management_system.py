import math
from .student import Student  
from .courses import Courses

class StudentManagementSystem:
    def __init__(self):
        self.students = {}          # dictionary to store students
        self.courses = {}           # dictionary to store courses
        self.marks = {}             # dictionary to store marks
        self.student_gpa = {}       # dictionary to store student gpa

    # function to input student information
    def student_info(self):
        numberOfstudents = int(input("Enter the number of students in the class: "))
        for i in range(numberOfstudents):
            id = input("Enter student id: ")
            name = input("Enter student name: ")
            dob = input("Enter date of birth of student: ")
            self.students[id] = Student(id, name, dob)

    # write student information to students.txt
        with open("students.txt", "w") as file:
            for student in self.students.values():
                file.write(f"{student.id},{student.name},{student.dob}\n")

    # function to input course information
    def courses_info(self):
        numberOfcourses = int(input("Enter number of courses: "))
        for i in range(numberOfcourses):
            course_id = input("Enter course id: ")
            course_name = input("Enter course name: ")
            credits = int(input("Enter credits for the course: "))
            self.courses[course_id] = Courses(course_id, course_name, credits)

    # write course information to courses.txt
        with open("courses.txt", "w") as file:
            for course in self.courses.values():
                file.write(f"{course.course_id},{course.course_name},{course.credits}\n")

    # function to input mark
    def input_mark(self):
        course_id = input("Enter course id: ")
        if course_id not in self.courses:
            print("Invalid Course Id")
            return

        for id, student in self.students.items():
            mark = float(input(f"Enter mark for {student.name}: "))
            mark = math.floor(mark * 10) / 10

        if id not in self.marks:
            self.marks[id] = {}
            self.marks[id][course_id] = mark

    # Write marks information to marks.txt
        with open("marks.txt", "w") as file:
            for student_id, marks in self.marks.items():
                for course_id, mark in marks.items():
                    file.write(f"{student_id},{course_id},{mark}\n")
                    
    # function to calculate gpa
    def calculate_gpa(self, student_id):
        if student_id not in self.marks:
            print("No marks found for the student.")
            return None
        total_credits = 0
        weighted_sum = 0
        for course_id, mark in self.marks[student_id].items():
            if course_id in self.courses:
                credits = self.courses[course_id].credits
                total_credits += credits
                weighted_sum += mark * credits
        if total_credits == 0:
            print("No credits found for the student.")
            return None
        gpa = weighted_sum / total_credits
        return gpa

    # function to list students by gpa
    def list_students_by_gpa(self):
        for student_id, student in self.students.items():
            gpa = self.calculate_gpa(student_id)
            if gpa is not None:
                self.student_gpa[student] = gpa
        sorted_students = sorted(self.student_gpa.items(), key=lambda x: x[1], reverse=True)
        for student, gpa in sorted_students:
            print(f"{student}\n GPA: {gpa:.2f}\n")

    # function to list students
    def list_students(self):
        for student in self.students.values():
            print(student)

    # function to list courses
    def list_courses(self):
        for course in self.courses.values():
            print(course)

    # function to show student's mark
    def showthemarkofstudent(self):
        course_id = input("Enter course id: ")
        if course_id not in self.courses:
            print("Invalid course Id")
            return
        for id, student in self.students.items():
            if id in self.marks and course_id in self.marks[id]:
                print(f" {student.name}: {self.marks[id][course_id]}")
            else:
                print(f" {student.name}: invalid")
