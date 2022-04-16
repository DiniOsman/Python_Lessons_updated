class class_1:
    def __init__(self, name, age, id, salary):
        self.name = name
        self.age = age
        self.id = id
        self.salary = salary
std1 = class_1("DINI", 30, 22, 1500)
std2 = class_1("MR", 35, 25, 2000)
print(std1.__dict__)
print(std2.__dict__)        