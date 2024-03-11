class Courses:
    def __init__(self, course_id, course_name, credits):
        self.course_id = course_id
        self.course_name = course_name
        self.credits = credits

    def __str__(self):
        return f" Course ID: {self.course_id}\n Course name:{self.course_name}\n Credits: {self.credits}"
