class Student:
    marks = 0
    def compute_marks(self, obtained_marks):
        marks = obtained_marks
        print("obtained marks: ", marks)
Student.print_marks = classmethod(Student.compute_marks)
Student.print_marks(88)        

class person:
    age = 25
    def print_age(cls):
        print("the age is: ", cls.age)
person.print_age = classmethod(person.print_age)
person.print_age()        