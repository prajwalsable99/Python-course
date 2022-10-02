#single inheritance


class student:
    
    live="human"
    work="programmer"
    def __init__(self,name,age,work):
        self.name=name
        self.age=age
        self.work=work
    
    def show(self):
        return f" { self.name } is { self.work } with age { self.age }  is {self.live}"

    

class studentcollege(student):
    def __init__(self,name,age,work,college):
        self.name=name
        self.age=age
        self.work=work
        self.college=college
    def showcollege(self):
        return f" { self.name } is from {self.college} college"

    # def row(self):
    #     print(self.live)
        


prajwal=studentcollege('alex',34,"CEO","fergusson")
print(prajwal.showcollege())
print(prajwal.show())  