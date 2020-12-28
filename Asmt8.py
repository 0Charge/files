j=[1,2,"a"]#creating a file to pre exist
e=open("one","w")
for line in j:
	e.write(str(line)+"\n")
e.close()
g=[4,5,"h"]#creting another file to pre exist
y=open("two","w")
for line in g:
	y.write(str(line)+"\n")
y.close()	
listOfFiles=["one","two"]
print("list of existing files:",listOfFiles)
a=str(input("enter  a file name:"))#enter a file name
if a in listOfFiles: #if file name already exists
	i=str(input("press r to read \n press a to append \n press w to empty and rewrite file \n press t to replace a line:\n"))
	if i=="r": #option to read it
		c=open(a,"r")
		C=c.read()
		print(C)
		c.close()
	elif i=="a": #option to append
		k=str(input("enter text to add:"))
		c=open(a,"a")
		c.write(k)
		c.close()
		c=open(a,"r")
		C=c.read()
		print(C)
	elif i=="w": #option to write
		m=int(input("enter number of elements tobe written:"))
		l=[]
		f=0
		while f<=m-1:
			q=input("enter element:")
			l.append(q)
			print(l)
			f+=1
		
		c=open(a,"w")
		for line in l:
			c.write(str(line)+"\n")
		c.close()
		c=open(a,"r")
		C=c.read()
		print(C)
		c.close()
	elif i=="t": #option to replace a line
			c=open(a,"r")
			C=c.read()
			print(C)
			c.close()
			x=int(input("select line to be replaced:"))
			z=str(input("enter the text to replace:"))
			c=open(a,"r+")
			J=c.readlines()
			J[x-1]=z+"\n"
			c.close()
			c=open(a,"w")
			for line in J:
				c.write(str(line))
			c.close()
			c=open(a,"r")
			C=c.read()
			print(C)
			c.close()
else:#if file name dont exist
					s=[]
					S=int(input("enter number of lines in file:"))#enter max num of lines 
					n=0
					while n<S:
						N=input("enter text to line:")
						s.append(N)#appending elements entered
						n+=1
					E=open(a,"w")#writing a file
					for line in s:
						E.write(str(line)+"\n")
					E.close()
					c=open(a,"r")#reading to print
					C=c.read()
					print(C)
					c.close()
					
"""import os used to deal with existing files on pc"""
							
					
			
		
		