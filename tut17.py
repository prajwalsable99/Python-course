#recurssions
'''
def show(str1):
    show(str1)
    print("hello ",str1)

show("prajwal")'''  
# function will kept caliing itself

#iterative 
'''def factorial(n):
    """" gives factorial"""
    fac=1
    for i in range(1,n+1,1):
        fac=fac*i
    return fac

print(factorial(5))

'''

#iterative
'''def facto(n):
    if n==1:
        return 1
    else:
        return n*facto(n-1)

print(facto(6))'''

#lets find nth num o ffibo  fibonnaci 0 1 1 2 3 5 8 13 21


def fibo(n):
    if n==1:
        return 0
    elif n==2:
        return 1
    else:
        return fibo(n-1)+fibo(n-2)

print(fibo(6))