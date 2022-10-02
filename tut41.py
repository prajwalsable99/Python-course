
# property   setter deleter
class student:
    def __init__(self,fname,lname):
        self.fname=fname
        self.lname=lname
        # self.email= f"{self.fname}{self.lname}@gmail.com"

    def show(self):
        return f"name of student is {self.fname} {self.lname}"


    @property
    def showmail(self):
        return f"{self.fname}.{self.lname}@gmail.com"

    @showmail.setter
    def showmail(self,str):
        names=str.split("@")[0]
        self.fname=names.split(".")[0]
        self.lname=names.split(".")[1]
       

    @showmail.deleter
    def showmail(self):
        self.fname=None
        self.lname=None


A=student("prajwal","sable")
B=student("alex","hales")

# print(A.showmail())

print(A.showmail)

A.showmail="xyz.abc@gmail.com"
print(A.showmail)
print(A.fname)
print(A.lname)

