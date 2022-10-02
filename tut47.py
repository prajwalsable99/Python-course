
fp=open("file14.txt","r")
try:
    fp=open("asd.txt","r")


except Exception as e:
    print(e)

else:
    print("it will work if and only,if except is not executed")

finally:
    print("ok,so i will be executed every time")
    
    fp.close()
print('no woory')