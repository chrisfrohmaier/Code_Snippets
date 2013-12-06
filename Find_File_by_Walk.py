import os
testing=[] #Establishing an array to find the files

for dirpath,dirnames,filenames in os.walk('refs'): #Traverses through a directory tree from 'refs' (refs is a folder in your CWD)
	for file in filenames:
		fileex=os.path.splitext(file)[-1] #Splits the file name, [-1] means it will look at the extension
		if fileex== '.fits': #wanted all .fits files 
			complete=os.path.join(dirpath,file) #joins the path and file name (path from 'refs')
			testing.append(complete)

prefix=testing[3].split('.')
print prefix
