#class(animal) and obj(class-instance i.e. dog)   

class student:
    
    live="human"
    work="programmer"
    name="xxxxxxxx"
    pass


#-------------------------------------------------
prajwal=student()
# its own quality
prajwal.name="prajwal"
prajwal.age=15
prajwal.subs=["maths","phy"]


yash=student()
#its own qulaity
yash.name="prajwal"
yash.age=17
yash.subs=["maths","sci"]



print(yash.work,prajwal.work)