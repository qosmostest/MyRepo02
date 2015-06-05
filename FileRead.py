# work with files

#open file for read

f=open('c:/TEMP/workpy.txt','r')

# pieces reading

s1=f.read(5)
print s1

s2=f.read(19)
print s2

s2=f.read(25)
print s2

f.close()

