# comprehnesions

'''l1=[]
for i in range(100):
    if i%7==0:
        l1.append(i)

print(l1)
'''

#mod

'''l2=[ i for i in range(100) if i%7==0]

print(l2)'''

#---------------------------------
# trad
di1={0:"item0",1:"item1",2:"item2"}
print(di1)
# mod
di2={i:f"item{i}"for i in range(10)}
print(di2)

#  key : value to  value :key

di3={v:k for k,v in di2.items()}
print(di3)