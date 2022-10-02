#operator overloading
#and dunder methods
class student:
    pay=8888

    def __init__(self,name,age,work):
        self.name=name
        self.age=age
        self.work=work
    
    def show(self):
        
        return f" { self.name } is { self.work } with age { self.age } "

    def __add__(self,other):  #one of method for more serach google @mapping operator to functions
        return self.age + other.age



prajwal=student("prajwal",20,"gamer")

yash=student("yash",24,"android_developer")

print("sum of age",prajwal+yash)