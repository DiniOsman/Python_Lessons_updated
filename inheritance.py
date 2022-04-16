# implementing inheritance in python
# parent class
class father:
    
    def __init__(self):
        print("Bird is ready")

    def whoisThis(self):
        print("son")

    def swim(self):
        print("Swim faster")

# child class
class son(father):

    def __init__(self):
        # call super() function
        super().__init__()
        print("son is ready")

    def whoisThis(self):
        print("son")

    def run(self):
        print("Run faster")

peggy = son()
peggy.whoisThis()
peggy.swim()
peggy.run()
        