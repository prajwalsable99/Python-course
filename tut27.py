#decorators

def deco(funct):
    def show():
        print("showing")
        funct()
        print("has shown")
    return show()


# @deco
def greet():
    print("heloo ,prajwal")


# deco(greet)



