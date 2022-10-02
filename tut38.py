#diamond problem



""" 
                      A
            __________|__________
            |                   |
            B                   C
            |___________________|
                      |
                      D

"""

class A:
    def show(self):
        print("hello  i am A")

class B(A):
    def show(self):
        print("hello  i am B")
class C(A):
    def show(self):
        print("hello  i am C")
class D(B,C):
    pass
    # def show(self):
    #     print("hello  i am D")



obj=D()
obj.show()
