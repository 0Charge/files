l=[]
i=0
while i<=4:
	a = input("enter a element:")
	l.append(a)
	print(l)
	i+=1
"""creating a file"""
e="new.txt"
a = open(e,"w")
for line in l:
	a.write(str(line)+"\n")
a.close()
""""appends a value to file"""
k=str(input("enter extra element:"))
c = open(e,"a")
c.write(k)
c.close()
"""reads file"""
c=open(e,"r")
b = c.read()
print(b)
c.close()
"""reads a single line first line"""
c=open(e,"r")
t=c.readline()
print("\n",t,end="")
c.close()
"""reads al lines in a single list form"""
i=open(e,"r")
j=i.readlines()
print('\n',j,end="")
i.close()