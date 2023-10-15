from astropy.coordinates import SkyCoord

# 14h26m33.29s	+56d34m57.42s
# 00:41:35	+41:10:26 05h19m32.4s	+53d46m16s
# 45:51.9	42:26:06
#

ra = '06:16:36.8'
dec = '+71:19:26'

# Parse the RA and DEC values
c = SkyCoord(ra, dec, unit=('hourangle', 'deg'))

# Print the RA and DEC values in decimal format
print(c.ra.degree)
print(c.dec.degree)