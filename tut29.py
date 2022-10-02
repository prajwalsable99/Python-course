class student:
    
    live="human"
    work="programmer"
    
    def show(self):
        return f" {self.live} { self.name } is { self.work } with age { self.age } learning { self.subs}"


#-------------------------------------------------
prajwal=student()
# its own quality
prajwal.name="prajwal"
prajwal.age=15
prajwal.subs=["maths","phy"]


yash=student()
#its own qulaity
yash.name="yash"
yash.age=17
yash.subs=["maths","sci"]

print(prajwal.show())
print(yash.show())