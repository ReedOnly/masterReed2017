#Code used for finding RFEs and making the plots used in the Master Theisis of Kristian Reed
#Written by Kristian Reed 10.06.2017
#Distribution of RFE's

from scipy import *
import matplotlib.mlab as mlab
import matplotlib.pyplot as plt
from scipy.stats import norm
from scipy.stats import rv_continuous, gamma

rfe=a=array([1,1,1,1,1,1,1,3,3,4,4,5,5,5,5,5,5,6,6,7,7,8,8,9,9,9,9,9,9,
             10,11,11,12,15,16,17,18,19,22,24,25,31,45,49,97,
             7,1,9,8,11,7,17,8,6,1,3,1,])


fig = plt.figure(figsize=(10,5))
ax = fig.add_subplot(111)

# the histogram of the data
n, bins, patches = ax.hist(rfe, bins=97, normed=0, facecolor='green', alpha=0.75)

#bincenters = 0.5*(bins[1:]+bins[:-1])
# add a 'best fit' line for the normal PDF
#y = mlab.normpdf(rfe)
#l = ax.plot(bincenters, y, 'r--', linewidth=1)

ax.set_title('Time duration of RFE')
ax.set_xlabel('Duration (minutes)')
ax.set_ylabel('Number of events')
plt.xlim(0,100)
plt.ylim(0,11)
ax.grid(True)



x = linspace(0, 50, 100)

#Gamma distribution
#fit_alpha, fit_loc, fit_beta=gamma.fit(rfe)
#p = gamma.pdf(x, a=2, loc=0, scale=3.8)
#ax.plot(x, p, 'r', linewidth=3)

plt.savefig('./RFEdist.pdf', dpi=400)