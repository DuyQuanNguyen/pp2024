from .person import Person

class Student(Person):
    def __init__(self, id, name, dob):
        super().__init__(name, dob)
        self.id = id

    def __str__(self):
        return f" ID: {self.id}\n Name: {self.name}\n DoB: {self.dob}"