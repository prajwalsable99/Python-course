# over riding 
class A:
    classvara="i am var_a of class A"
    def __init__(self):
        self.classvara="i am istance var in A" 

#------------------------------------------------------------------
class B(A):
    #pass
    classvara="i am var_b of class B"
    def __init__(self):
        # super().__init__()                     #this will call init of derive
        self.classvara="i am istance var in B"   
        # super().__init__()                       #this will call init of base

#---------------------------------------------------------------------


obb=B()
print(obb.classvara)  



'''order of preference      1.derive class constructor var
                            2.base class constructor var
                            3.derive class var
                            4.base class var

                            
                            '''