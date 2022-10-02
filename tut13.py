# file io basics

'''# r :read  (default)
# ,w:write
# ,a:apppend
# ,X:creates if not,if exist doest work'''


'''b-binary,
t-text(default),
+=read and write'''

#------------------------------apply
#i opened alreday created file
'''fp=open("file13a.txt","r")
content=fp.read()              #reda(n)  will read n char
print("text from :",content)
fp.close()
'''

'''fp=open("file13a.txt","rb")
content=fp.read()       
print( "binary form:", content)       
fp.close()'''

#also after reading fp moves to end

# fp.readline()  read one line
'''fp=open("file13a.txt","r")
content=fp.readline()
print(content)
content=fp.readline()             
print(content)
fp.close()

'''

#readlines() gives  list ofall lines
'''fp=open("file13a.txt","r")
content=fp.readlines()
print(content)

fp.close()
'''


