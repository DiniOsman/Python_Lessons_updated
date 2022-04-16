class Empoloyee:
    def __init__(self, name, age, color, profession):
        self.name = name
        self.age = age
        self.color = color
        self.profession = profession
        
    def intorduce_yourself(self):
        pass
        #print("my name is: " + self.name)
emp1 = Empoloyee("DINI HASSAN", 30, "BLACK", "SOFTWARE ENGINEER")
#emp1.intorduce_yourself()
print(emp1.name, emp1.age, emp1.color)