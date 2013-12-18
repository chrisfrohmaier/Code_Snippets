import numpy as np

a, b = 300, 200 #Where do you want your mask to be centered y,x
ny = 1000 #Y size
nx=1000 #X size
r = 40 #Radius of Mask

ym,xm = np.ogrid[-a:ny-a, -b:nx-b] #Some clever numpy stuff
mask = xm*xm + ym*ym <= r*r #Makes your circle

array = np.ones((ny, nx),dtype=bool) #your input array that will be masked
array[mask] = False #Changes all the parts of that array that need to be masked
#np.savetxt('Test2.txt',array,delimiter=' ') #Saves the array to a text file if you want
print array #Prints the array