# tuple sequential but immnutable

tup1=(1,2,3)
print(tup1)

# tup1[1]=11  #give error
# print(tup1)


# dictionary in py have {key:value} non sequential 

a={}
print(type(a))
a={1:"one",2:"two","prajwal":"hero"}
print(a)

# accesing  value by key 
print(a[2])

a["boy"]="girl"
print(a)
a["boy"]="man"
print(a)

del a["boy"]

print("a=",a)


# create copy of di    

b=a.copy()
print("b=",b)

a.update({"big":"small"})

print(a)

print(a.keys())  #gives keys

print(a.items()) # give slist of tuple of key:value pairs