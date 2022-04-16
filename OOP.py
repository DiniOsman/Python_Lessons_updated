class C1():
    def setname(self, who):
        self.name = who
        
l1 = C1()
l2 = C1()
l1.setname('bob') # Sets I1.name to 'bob'
l2.setname('mel') # Sets I2.name to 'mel'
print(l1.name)
    
    