
# class method
class student:
    pay=8888

    def __init__(self,name,age,work):
        self.name=name
        self.age=age
        self.work=work
    
    def show(self):
        
        return f" { self.name } is { self.work } with age { self.age } "

    @classmethod            #to cnage class var
    def change_pay(classabc,newpay):
        classabc.pay=newpay

    @staticmethod               #only for class and obj
    def greet(x):
        print(x)

'''
prajwal=student("prajwal",20,"developer")
print(prajwal.show())
'''

student.change_pay(5555)
print(student.pay)
x="heeeeeeeeeeeeeeelo"

student.greet(x)
