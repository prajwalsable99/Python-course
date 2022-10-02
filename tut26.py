#map,filter and reduce
'''#normal way to update items by1
lis=['1','2','3']

for i in range(len(lis)):
    lis[i]=int(lis[i])+1

print(lis)'''

'''
li=["2","4","6"]

li=list(map(int,li))                                 #map===           list(map(fun,onwhichlist))

print(li)

li=list(map(lambda x: x*x,li))

print(li)'''

#---------------------------------------------------------------------------------------

#filter

'''
oldlist=[1,2,3,4,5,6,7,8,9]

def showgrt5(x):
    return x>5

newlist=list(filter(showgrt5,oldlist))

print(oldlist)
print(newlist)'''
#-----------------------------------------------------------------------------------------------
#reduce imported from functools

from functools import reduce

lista=[1,2,3,4,5]
'''num=0
for i in lista:
    num=num+i

print(num)'''

#reduce
sum=reduce(lambda x,y: x+y,lista)

print(sum)