#functions in pythons

#built-in
'''a=6
b=10
c= sum((a,b))   #built in function use ctrl and click tosee  builtins.py
print(c)'''


#user defined

#no arg
'''def show():
    print("hello i am in function")

show()'''
#with arg and return value to store in var
'''def add(a,b):
    return a+b

sum =add(2,4)
print(sum)


'''
#doc-string

def display():
    """this is explaining what func does"""
    return("hello i am displayed")



print(display.__doc__)