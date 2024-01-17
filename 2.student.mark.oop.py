class Person():
    def __init__(self, name, dob):
        self.name = name
        self.dob = dob
        
class Student(Person):
    def __init__(self, id, name, dob):
        super().__init__(name, dob)
        self.id = id
    
    def __str__(self):
        return f" ID: {self.id}\n Name: {self.name}\n DoB: {self.dob}"
           
        
class Courses():
    def __init__(self, course_id, course_name):
        self.course_id = course_id
        self.course_name = course_name
    
    def __str__(self):
        return f" Course ID: {self.course_id}\n Course name:{self.course_name}"
class StudentMangementSystem():
    def __init__(self):
        self.students = {}
        self.courses = {}
        self.marks = {}
    
    def student_info(self):
       numberOfstudent = int(input("Enter the number of student in the class: "))
       for i in range(numberOfstudent):
          id = input("Enter student id: ")
          name = input("Enter student name: ")
          dob = input("Enter date of birth of student: ")
          self.students[id] = Student(id, name, dob)
    
    def courses_info(self):
       numberOfcourses = int(input("Enter number of courses: "))
       for i in range(numberOfcourses):
          course_id = input("Enter course id: ")
          course_name = input("Enter courses name: ")
          self.courses[course_id] = Courses(course_id, course_name)
       
    def input_mark(self):
       course_id = input("Enter course id: ")
       if course_id not in self.courses:
          print("Invalid Course Id")
          return
       for id, student in self.students.items():
          mark = float(input(f"Enter mark for {student.name}: "))
          if id not in self.marks:
             self.marks[id] = {}       
          self.marks[id][course_id] = mark            
       
    def list_students(self):
        for student in self.students.values():
            print(student)

    def list_courses(self):
        for course in self.courses.values():
            print(course)

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
    
system = StudentMangementSystem()
system.student_info()
system.courses_info()

while True:
   print("Select from 1 to 5: ")
   print("1. Input mark for student in the course: ")
   print("2. List student: ")
   print("3. List courses: ")
   print("4. Show student marks:")
   print("5. Out")
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
      print("Thanks for using this student management system")
      break
   else:
      print("invalid choice")  
                
