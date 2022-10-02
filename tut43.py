# generators in python

"""

Iterable-  __iter__() or __getitem__()

Iterator-   __next__()

Itertaion-

"""
def gen(n):

    for i in range (n):

         yield i

x=gen(6)

print(x.__next__())
print(x.__next__())
print(x.__next__())
print(x.__next__())
print(x.__next__())