# just for comparisons, let's import the originals from astropy
import astropy.constants as c_astropy
import astropy.units as u_astropy

print "from astropy (before unitsiau2015 import) G =", c_astropy.G.value

from unitsiau2015 import u, c

# once unitsiau2015 is imported, the values within astropy have also changed
print "from astropy (after unitsiau2015 import) G =", c_astropy.G.value
print "from unitsiau2015 G =", c.G.value
