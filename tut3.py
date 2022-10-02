#string functions

var="this is string as its type is"
print(var,type(var))
  #slicing

print(var[3])   # will print s ,index starst from 0

print(var[0:4])   #will print 0,1,2,3 th indicses items <4

print(len(var))  #will give no of char

print(var[0:29:2])  #3rd arg is step

print(var[::-1])  #pallindrome


print(var.isalnum)   #true if no spaces
print(var.isdigit)  #true if all digits  lly wheave decimal,alpha etc  ,capitalize ,lower ,upper ,insert5,replace,

#u can use string methoods doc o f official python
print(var.endswith("is"))
print(var.count('t'))
print(var.find('str'))