# lists and its functions  
# sequential,mutable,can storer diff data typoes unlike arrau

'''students=['yash','shiv','harsh']
print(students)

items=['heelo',11,134.34,True]

print(items)
print(items[2])
'''
#accesing

#list methods

num=[22,34,5,1,37]
#num.sort()
#num.reverse()


print(num)

# slicing in lists is simmilar to that of strings [start:end:step]

# string functons 

# print(len(num),max(num),min(num))

num.append(99)   #will add 99 at last
print(num)

num.insert(0,777)  # (index,value )
print(num)
num.remove(777)  #remove via value
print(num)

num.pop(0)     #remove vvia index
print(num)

num[2]=10   #mutability
print(num)

# extend()  joins alist ,clear(),index() gives first index 