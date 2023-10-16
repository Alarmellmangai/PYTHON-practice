class resume:
    def __init__(self,firstname,lastname):
        self.f_n=firstname
        self.l_n=lastname

    def fullname(self):
        return f"hi {self.f_n} {self.l_n}"
class student(resume):
    pass

x=student("john","bundy")
print(x.fullname())