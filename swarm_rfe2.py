#Code used for finding RFEs and making the plots used in the Master Theisis of Kristian Reed
#Written by Kristian Reed 10.06.2017

from scipy import *
from spacepy import pycdf
from matplotlib import pyplot as plt
import matplotlib.dates as mdates
import datetime as dt
 

cdfa = pycdf.CDF('./files/swarm/SW_OPER_FACATMS_2F_20141216T000000_20141216T235959_0205.DBL')
cdfac = pycdf.CDF('./files/swarm/SW_OPER_FAC_TMS_2F_20141216T000000_20141216T235959_0206.DBL')
cdfc = pycdf.CDF('./files/swarm/SW_OPER_FACCTMS_2F_20141216T000000_20141216T235959_0205.DBL')

cdf=cdfac

#Print different variables
print cdf

#Copy All
dataset = cdf.copy()

elements=cdf.keys()

#Import single variable

faca=cdfa['FAC'][...]
timea=cdfa['Timestamp'][...]
lona=cdfa['Longitude'][...]
lata=cdfa['Latitude'][...]

facc=cdfc['FAC'][...]
timec=cdfc['Timestamp'][...]
lonc=cdfc['Longitude'][...]
latc=cdfc['Latitude'][...]

facac=cdfac['FAC'][...]
timeac=cdfac['Timestamp'][...]
lonac=cdfac['Longitude'][...]
latac=cdfac['Latitude'][...]


formatter = mdates.DateFormatter('%H:%M:%S')
fig,ax=plt.subplots(figsize=(9,3))
ax=plt.subplot(1,1,1)
s1=ax.plot(timea,faca,label='SWARM A')
s2=ax.plot(timec,facc,label='SWARM C')
s3=ax.plot(timeac,facac,label='SWARM AC')
ax.set_xlim([dt.datetime(2014, 12, 16, 0,47), dt.datetime(2014, 12, 16, 0,49)])
ax.xaxis.set(major_formatter=formatter)
ax.set_ylim([-2, 2])
#ax.set_xlabel('Time [UTC]',fontsize=14)
ax.set_ylabel('Current [$uA m^{-2}$]',fontsize=14)
ax.legend(fontsize=10)

#ax2=ax.twinx()
#s4=ax2.plot(timea,lata,label='lat A')
#s5=ax2.plot(timec,latc,label='lat B')
#s6=ax2.plot(timeac,latac,label='lat AC')
#ax2.set_ylabel('GEO Latitude [deg]')
#ax2.set_xlim([dt.datetime(2014, 12, 16, 0,47), dt.datetime(2014, 12, 16, 0,49)])
#ax2.set_ylim([70, 85])
#ax2.legend()
ax.grid(True)

#ax.axvspan(xmin=dt.datetime(2014, 12, 13, 0,20,30), xmax=dt.datetime(2014, 12, 13, 0,21,30), color='0.9')
#ax.axvline(dt.datetime(2014, 12, 16, 0,41), color='k', linestyle='solid')
#######################################################
#a=2760
#b=2940
#ax3=plt.subplot(2,1,2)
#s1=ax3.plot(flipud(lata[a:b]),flipud(faca[a:b]),label='SWARM A')
#s2=ax3.plot(flipud(latc[a:b]),flipud(facc[a:b]),label='SWARM C')
#s3=ax3.plot(flipud(latac[a:b]),flipud(facac[a:b]),label='SWARM AC')
##ax3.set_xlim([dt.datetime(2014, 12, 16, 0,46), dt.datetime(2014, 12, 16, 0,49)])
##ax3.xaxis.set(major_formatter=formatter)
#ax3.set_xlim([84,72.6])
#ax3.set_ylim([-2, 2])
#ax3.set_xlabel('Latitude [degree]')
#ax3.set_ylabel('Current [$uA/m^2$]')
#ax3.legend()

#ax4=ax3.twinx()
#s4=ax4.plot(timea,lata,label='lat A')
#s5=ax4.plot(timec,latc,label='lat B')
#s6=ax4.plot(timeac,latac,label='lat AC')
#ax4.set_ylabel('GEO Latitude [deg]')
#ax4.set_xlim([dt.datetime(2014, 12, 16, 0,46), dt.datetime(2014, 12, 16, 0,49)])
#ax4.set_ylim([70, 85])
#ax2.legend()
#ax3.grid(True)

#fig.suptitle('SWARM Field aligned currents (FAC) 16.12.2014',fontsize=14)

fig.show()

plt.savefig('./2swarm.pdf', dpi=400)

