class grandfather:
    def show1(self):
        return ("i am grandfather")


class father(grandfather):                #multilevel inheritance  
    def show2(self):
        return ("i am father")

class son(father,):
    def show3(self):
        return ("i am son")


prajwal=son()  #i can access all functions from obj of son 

print(prajwal.show1())
print(prajwal.show2())
print(prajwal.show3())


