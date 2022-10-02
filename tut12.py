#exception handling try and except
'''n1=int(input("no1 : "))  #error point
n2=int(input("\nno2 :"))
print("sum is",n1+n2)
'''
# if i put values like q and 5 error will come at line 2

#-------------------------------------------------------------------------
'''n1=(input("no1 : "))
n2=(input("\nno2 :"))
print("sum is",int(n1)+int(n2))   #erroe point


# if i put values like q and 5 error will come at line 11

print("i wil not be printed")  #due to error will not be excuted
'''
#--------------------------------------------------------------------

# so this can be handles by
n1=(input("no1 : "))
n2=(input("\nno2 :"))
try:
    print("sum is",int(n1)+int(n2))   #erroe point
except Exception as why :
    print( "why :",why)

print("this time i will be printed")

#if no eror=>try will work else exception handling
#----------------------------------------------------


