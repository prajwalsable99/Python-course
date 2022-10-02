def display(x,y):
    return f"sum of {x} and {y} is {x+y}"

#print(display(3,4))
"""while importing this will be also imported to avoid so we use"""

print("imported=",__name__)
if __name__=='__main__':
     print(display(3,4))

