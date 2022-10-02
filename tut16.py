
# varg=10
# print(varg)
# #local and global variables
# def fun(x):
#     # varg=5 #if varg was not locally here it would have gone for global search
#     # a=6
#     global varg
#     varg=varg+11
#     print(varg)
#     print(x,"printed")

# fun(varg)
# print(varg)

#local acn be use outside fun
# print(a)  throw error as it is local in function
#also global var cannot be changed in fucnt for that u have to use global prefix



def prajwal():
    x=10
    def boy():
        global x
        x=20
    print("due to prajwal",x)
    boy()
    print("due to boy",x)
    
prajwal()
print(x)
#wont work as global as global
