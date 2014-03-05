'''
This file demonstrates how to do a Gaussian Kernal Density Estimation

BE CAREFUL!!!! FOR LOTS OF DATA POINTS THIS IS A VERY SLOW PROCESS, PERHAPS TRY A HEXBIN FIRST
'''
import pylab, subprocess
from scipy.stats import kde
import numpy as np
import math
from matplotlib import ticker
from matplotlib import cm as cm

data=[BS_av_colour,BS_av_V]
k=kde.gaussian_kde(data)
nbins=200 #PLAY WITH THIS, NOT TOO HIGH OR IT WILL TAKE FOREVER

xaxis=[]#An array containing all you x-axis values
yaxis=[]#An array containing all your yaxis values


xi, yi = np.mgrid[min(xaxis):max(xaxis):nbins*1j, min(yaxis):max(yaxis):nbins*1j]
zi = k(np.vstack([xi.flatten(), yi.flatten()]))

colors = [('white')] + [(cm.jet(i)) for i in xrange(1,256)] #This creates a color range based on the 'jet' colour scheme, but a value of zero is assigned 'white' this is so that if it is over plotted on your scatter diagram then it blends
new_map = matplotlib.colors.LinearSegmentedColormap.from_list('new_map', colors, N=256) #the new map created above

pylab.pcolormesh(xi, yi, zi.reshape(xi.shape), cmap=new_map) #Change cmap for idfferent color schemes

pylab.show() #or pylab.savefig()