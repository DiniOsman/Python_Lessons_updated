

class Customer:
    def __init__(self, name, MembershipType):
         self.name = name
         self.MembershipType = MembershipType
         
        
C = Customer("Dini", "Gold")
print(C.name, C.MembershipType)     

str = "welocme my boy"

print(str.upper())   
print(type(str), str)
    