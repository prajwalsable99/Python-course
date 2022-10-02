# args and kwargs
#in args we can send a tuple of no args
'''def name(*args):
    print(args)   #tuple
    for i in args:  #acesssing member by member
        print(i)

li=['prajwal','yash','rohan','jay']

name(*li)
'''
#one more example

'''def show(name,*quality):
    print(f"{name} has quality ")
    for i in quality:  #acesssing member by member
        print(i)

    
show("prajwal","smart","hanndsome","good")
print("===============")
l1=['happy','smart','chill']
show("yash",*l1)'''

#  (normal,*args) is valid...........        (*args,normal) is invalid


#kwargs
def display(**kwargs):
    print("cast is :\n")
    for key,value in kwargs.items():
        print(f"{ key }  is {value}")

di={"prajwal":"hero","yash":"director","jay":"producer"}


display(**di)