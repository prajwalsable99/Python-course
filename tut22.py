# time  module
import time
'''
initial1=time.time()    #ref time at that instant

for  j in range(45):
    print("hi")

print("time rquired for the for loop is",time.time()-initial1)


initial2=time.time()
i=0
while(i<45):
    print("hi")
    i=i+1


print("time rquired for the while loop is",time.time()-initial2)'''


# how to get local time

'''time_now=time.asctime(time.localtime(time.time()))

print(time_now)


'''
#time delay
i=0
while(i<10):
    print(i)
    time.sleep(2)