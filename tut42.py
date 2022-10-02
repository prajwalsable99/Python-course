class student:
    def __init__(self,fname,lname):
        self.fname=fname
        self.lname=lname
        # self.email= f"{self.fname}{self.lname}@gmail.com"

    def show(self):
        return f"name of student is {self.fname} {self.lname}"


    
    def showmail(self):
        return f"{self.fname}.{self.lname}@gmail.com"

A=student("abc",123)
print(A.showmail())


#object intro spection 
print(dir(A))

import inspect
print(inspect.getmembers(A))
