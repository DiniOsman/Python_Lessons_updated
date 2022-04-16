class student:
    def check_pass_fail(self):
        if self.marks >= 40:
            return True
        else:
            return False
st1 = student()
st1.name = "DINI"
st1.marks = 85
print(st1.check_pass_fail())        