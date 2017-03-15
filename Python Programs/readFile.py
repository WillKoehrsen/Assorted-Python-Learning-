fid = open('exampleFile.txt','r')
readMe = fid.read()
print(readMe)
readLines = open('exampleFile.txt','r').readlines()

print(readLines)
fid.close()
print(type(fid))
#print(type(readMe))