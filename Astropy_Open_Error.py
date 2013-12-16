from astropy.io import fits
try:
		hdulist_multi_sci=fits.open('/Users/cf5g09/Documents/PTF_Transform/Icecube/refs/ptf_2924/C01/cd.ptf_2924_01_R_first.weight.fits')
		#print '++++ multi_mask assign ', science_image
		
except IOError or Warning or UnboundLocalError:
	print 'Cant open Science'