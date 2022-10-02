
# set has no repeat items
s=set()   
print(type(s))

setfromlist=set([1,2,3,4,4,42,22,2,2])
print(setfromlist)
print(type(setfromlist))

s.add(1)
print(s)
s.add(2)
print(s)
s1=s.union({3,4})
print(s1)
s2=s1.intersection({3})
print(s2)

# it has also min,max,len 

a={1,2,3,4}
print(type(a))