#tell()  gives pointer current position      seek()  shiftes fp position
fp=open("file15.txt","rt")
print(fp.tell())

con=fp.readline()
print(con)

print(fp.tell())

con=fp.readline()
print(con)

print(fp.tell())
fp.close()


seek(n)            //n th position
