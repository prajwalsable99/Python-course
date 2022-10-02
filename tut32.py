class student:
    
    live="human"
    work="programmer"
    def __init__(self,name,age,work):
        self.name=name
        self.age=age
        self.work=work
    
    def show(self):
        return f" { self.name } is { self.work } with age { self.age }  is {self.live}"

    

prajwal=student("prajwal",20,"developer")
print(prajwal.show())
