#enumerate  and join inlist

l1=["joe","alex","jos","chris","johnny"]
'''i=0
for item in l1:
    if i%2==0:
        print("odd items are",item)
    i=i+1
'''

'''
for index,item in enumerate(l1):
    if index%2==0:
        print("odd items are",item)


'''
#-----------------------------------------------------------------------------
l1=["apple","cat","ball","dog","egg"]
for i in l1:
    print(i,end=" ,")

#join function
print("\n")
print(" and ".join(l1))
