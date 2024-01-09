students = {}  
def student_info():
   numberOfstudent = int(input("Enter the number of student in the class: "))
   for i in range(numberOfstudent):
      id = input("Enter student id: ")
      name = input("Enter student name: ")
      dob = input("Enter date of birth of student: ")
      students[id] = {"Name": name, "DoB": dob}

courses = {}
def courses_info():
   numberOfcourses = int(input("Enter number of courses: "))
   for i in range(numberOfcourses):
      course_id = input("Enter course id: ")
      course_name = input("Enter courses name: ")
      courses[course_id] = {"Courses name": course_name}
      
marks = {}      
def input_mark():
   course_id = input("Enter course id: ")
   if course_id not in courses:
      print("Invalid Course Id")
      return
   for id in students:
      mark = float(input(f"Enter mark for {students[id]['Name']}: "))
      if id not in marks:
         marks[id] = {}       
      marks[id][course_id] = mark
      
def list_students():   
   for id in students:
      print(f"{id}: {students[id]['Name']}")
      
def list_courses():
   for course_id in courses:
      print(f"{course_id}: {courses[course_id]['Courses name']}")      

def showthemarkofstudent():
   course_id = input("Enter course id: ")
   if course_id not in courses:
      print("Invalid course Id")
      return   
   for id in students:
      if id in marks and course_id in marks[id]:
            print(f"{students[id]['Name']}: {marks[id][course_id]}")
      else:
            print(f"{students[id]['Name']}: invalid")

      
student_info()
courses_info()
while True:
   print("Select from 1 to 5: ")
   print("1. Input mark for student in the course: ")
   print("2. List student: ")
   print("3. List courses: ")
   print("4. Show student marks:")
   print("5. Out")
   choice = input("Select a number: ")
   if choice == '1':
      input_mark()
   elif choice == '2':
      list_students()
   elif choice == '3':
      list_courses()
   elif choice == '4':
      showthemarkofstudent()
   elif choice == '5':
      print("Thanks for using this student management system")
      break
   else:
      print("invalid choice")            
 
      
            
       

