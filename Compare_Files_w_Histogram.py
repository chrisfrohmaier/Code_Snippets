import matplotlib.pyplot as plt


f=open('Compare.cat') #Reading the first file to comapre
fin=f.readline()
mag_array=[]
while fin:
	if fin.startswith('#'):
		#h.write(fin)
		#print fin
		fin=f.readline()
		continue
	ln=fin.split()
	mag=float(ln[2])
	if mag<30.:
		mag_array.append(mag)
	fin=f.readline()
g=open('PTF201101274235_2_o_27866_00.w_Catalog.cat') #Reading the second file to compare
gin=g.readline()
mag_Peter_array=[]
while gin:
	if gin.startswith('#'):
		#h.write(fin)
		#print fin
		gin=g.readline()
		continue
	ln=gin.split()
	mag=float(ln[2])
	if mag<30.0:
		mag_Peter_array.append(mag)
	gin=g.readline()

#The steps below are all the Plotting stuff for the Histograms


b1=plt.hist(mag_array,bins=30,label='IPAC, Zpt=23.48993',histtype='stepfilled',alpha=0.5) #alpha makes things translucent
b2=plt.hist(mag_Peter_array,bins=30,label='Peter, Zpt=27.8',histtype='stepfilled',alpha=0.5)
plt.title("IPAC Name: PTF_201101274235_i_p_scie_t100949_u009819050_f02_p002964_c00 \n Peter\'s Name: PTF201101274235_2_o_27866_00.w")
plt.xlabel('Magnitude')
plt.ylabel('Number of Detections')
plt.legend(loc=2)
plt.savefig('First Compare.png')
plt.show()
plt.close()	