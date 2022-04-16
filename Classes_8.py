class Person:
    species = "human"
    def __init__(self, name, age, GradYear):
        self.name = name
        self.age = age
        self.GradYear = GradYear
                
dini = Person("DINI", 30, 2014)
sharm = Person("SHARM", 25, 2020)

print("Dini is a {}".format(dini.__class__.species))
print("sharm is a {}".format(sharm.__class__.species))

print("{} is {} years old and {} is his graduation is : ".format(dini.name, dini.age, dini.GradYear))
print("{} is {} years old and {} is his graduation is: ".format(sharm.name, sharm.age, sharm.GradYear))