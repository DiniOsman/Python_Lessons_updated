class SoftwareEngineer:
    def __init__(self, name, age, level, salary):
        self.name = name
        self.age = age
        self.level = level
        self.salary = salary
    def code(self):
        print(f"{self.name} is writing code and his age is " f"{self.age}")
        
    def code_in_language(self, language):
        print(f"{self.name} is writing code in {language}...")    
        
    #def information(self):
        #information  = f"name = {self.name}, age = {self.age}, level = {self.level}"
        #return information     
    # __str__ is same as above method excep func calling are different
    def __str__(self):
        information  = f"name = {self.name}, age = {self.age}, level = {self.level}"
        return information 
        
    def  __eq__(self, other):
        return self.name == other.name and self.age == other.age
    
    def entry_salary(age):
        if age < 25:
            return 500
        if age > 25 and age == 30:
            return 700
        if age > 30 and age == 40:
            return 1200
        else:
            return 1500
                   
se1 = SoftwareEngineer("DINI", 30, "SENIOR", 7000)
se2 = SoftwareEngineer("ALI", 25, "JUNIOR", 5000)
se3 = SoftwareEngineer("ALI", 25, "JUNIOR", 5000)
se2.code()
se1.code()
se1.code_in_language("PYTHON")
se2.code_in_language("JAVA")   
print(se1)   
print(se2 == se1)  
print(SoftwareEngineer.entry_salary(24))