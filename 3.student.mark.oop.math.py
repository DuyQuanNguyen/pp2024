import math
import numpy as np
#define a class Person
class Person():
    def __init__(self, name, dob):
        self.name = name
        self.dob = dob

#define a class Student inherits from class Person
class Student(Person):
    def __init__(self, id, name, dob):
        super().__init__(name, dob)
        self.id = id

    def __str__(self):
        return f" ID: {self.id}\n Name: {self.name}\n DoB: {self.dob}"

#define a class Courses
class Courses():
    def __init__(self, course_id, course_name, credits):
        self.course_id = course_id
        self.course_name = course_name
        self.credits = credits

    def __str__(self):
        return f" Course ID: {self.course_id}\n Course name:{self.course_name}\n Credits: {self.credits}"

#define a main class for student management system
class StudentManagementSystem():
    def __init__(self):
        self.students = {}          #dictonary to store students
        self.courses = {}           #dictonary to store courses
        self.marks = {}             #dictonary to store marks
        self.student_gpa = {}       #dictonary to store studentgpa

#fuction to input student information
    def student_info(self):
        numberOfstudents = int(input("Enter the number of students in the class: "))
        for i in range(numberOfstudents):
            id = input("Enter student id: ")
            name = input("Enter student name: ")
            dob = input("Enter date of birth of student: ")
            self.students[id] = Student(id, name, dob)

#fuction to iput course information
    def courses_info(self):
        numberOfcourses = int(input("Enter number of courses: "))
        for i in range(numberOfcourses):
            course_id = input("Enter course id: ")
            course_name = input("Enter course name: ")
            credits = int(input("Enter credits for the course: "))
            self.courses[course_id] = Courses(course_id, course_name, credits)

#fuction to input mark
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

#fuction to calculate gpa
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

#funtion to list students by gpa
    def list_students_by_gpa(self):
        for student_id, student in self.students.items():
            gpa = self.calculate_gpa(student_id)
            if gpa is not None:
                self.student_gpa[student] = gpa
        sorted_students = sorted(self.student_gpa.items(), key=lambda x: x[1], reverse=True)
        for student, gpa in sorted_students:
            print(f"{student}\n GPA: {gpa:.2f}\n")

#fuction to list students
    def list_students(self):
        for student in self.students.values():
            print(student)

#fuction to list courses
    def list_courses(self):
        for course in self.courses.values():
            print(course)

#function to show student's mark
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

#create an instance of the StudentManagementSystem
system = StudentManagementSystem()
system.student_info()
system.courses_info()

#main 
while True:
    print("Select from 1 to 6: ")
    print("1. Input mark for student in the course: ")
    print("2. List student: ")
    print("3. List courses: ")
    print("4. Show student marks:")
    print("5. List students by GPA:")
    print("6. Exit")
    choice = input("Select a number: ")
    if choice == '1':
        system.input_mark()
    elif choice == '2':
        system.list_students()
    elif choice == '3':
        system.list_courses()
    elif choice == '4':
        system.showthemarkofstudent()
    elif choice == '5':
        system.list_students_by_gpa()
    elif choice == '6':
        print("Thanks for using this student management system")
        break
    else:
        print("Invalid choice")
