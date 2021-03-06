#Code used for finding RFEs and making the plots used in the Master Theisis of Kristian Reed
#Written by Kristian Reed 10.06.2017

import numpy as np
from matplotlib import pyplot as plt
from matplotlib import gridspec
from tools import *
import os


def mltplot(newpath,timeEvents,imf,radars,mlat,mlt):
    #http://stackoverflow.com/questions/36061537/polar-plots-with-magnetic-local-time0-23-as-the-azimuth-against-magnetic-latit
    # set up random data between 0 and 90
    
    print(len(mlt))
    fig = plt.figure(figsize=(8, 6)) 
    #st=fig.suptitle(str(radars)+' from '+sTime.strftime("%Y.%m.%d %H:%M")+' until '+ eTime.strftime("%H:%M UTC"),fontsize="x-large")
    gs = gridspec.GridSpec(2, 1, height_ratios=[3, 1]) 
    r = mlat#[np.random.random() * 90.0 for i in range(0,10)]
    
    # set up 24 hours matching the random data above
    #hours = np.linspace(0.0,24.0,len(r))
    # scaling the 24 hours to the full circle, 2pi
    theta = mlt / 24.0 * (2.0 * np.pi)
    
    # reverse your data, so that 90 becomes 0:
    r_rev = [(ri - 90.0) * -1.0 for ri in r]
    
    # set up your polar plot
    fig1 = plt.subplot(gs[0], projection='polar')
    fig1.set_theta_zero_location("S")
    
    for n in range(len(mlat)):
#        year=time[n].year
#        day=time[n].timetuple().tm_yday
#        hour=time[n].hour
#        minute=time[n].minute
#        imf=get_imf(year,day,hour,minute)
        if imf[n]==0: continue
        by=imf[n][2]        #by=imf[n][2] for bz 
        if by=='ls': fig1.scatter(theta[n], r_rev[n], color='c', marker='s', linewidth=0.1)
        elif by=='pm': fig1.scatter(theta[n], r_rev[n], color='y', marker='s', linewidth=0.1)
        elif by>0.5: fig1.scatter(theta[n], r_rev[n], color='r', linewidth=0.1)
        elif by<-0.5: fig1.scatter(theta[n], r_rev[n], color='b', linewidth=0.1)
        else: fig1.scatter(theta[n], r_rev[n], color='k', linewidth=0.1)
        
    fig1.scatter(0, 30, color='r', linewidth=0.1, label='Bz>0')
    fig1.scatter(0, 30, color='b', linewidth=0.1, label='Bz<0')
    #fig1.scatter(0,30, color='y', marker='s', linewidth=0.1,label='Spread > 5 nT')
    fig1.scatter(0,30, color='y', marker='s', linewidth=0.1,label='Sign change')
    fig1.legend(bbox_to_anchor=(1.05, 1), loc=2, borderaxespad=0.)
        
    
    # define your axis limits
    fig1.set_ylim([0.0, 20.0])
    
    # statically reverse your y-tick-labels
    # caution: this turns your labels into strings
    #          and decouples them from the data
    # 
    # the np.linspace gives you a distribution between 90 and 0 -
    # the number of increments are related to the number of ticks
    # however, you require one more label, because the center is 
    #     omitted.  
    fig1.set_yticklabels(['{:.0f}'.format(ylabel) \
                    for ylabel in np.linspace(90.0,70.0,len(fig1.get_yticklabels())+1)[1:]])
    
    
    # statically turn your x-tick-labels into fractions of 24
    # caution: this turns your labels into strings
    #          and decouples them from the data
    #
    # the number of ticks around the polar plot is used to derive
    #    the appropriate increment for the 24 hours
    fig1.set_xticklabels(['{:.0f}'.format(xlabel) \
                        for xlabel in np.arange(0,24,(24 / len(fig1.get_xticklabels())))])
    
    fig1.grid(True)
    
    fig2=plt.subplot(gs[1])
    for n in range(len(mlat)):
        if imf[n]==0: continue
        by=imf[n][2]
#        if by>0.5: plt.scatter(mlt[n],mlat[n],color='r', linewidth=0.1)
#        elif by<-0.5: plt.scatter(mlt[n],mlat[n],color='b', linewidth=0.1)
#        else: plt.scatter(mlt[n],mlat[n],color='k', linewidth=0.1)
        if by=='ls': fig2.scatter(mlt[n],mlat[n], color='c', marker='s', linewidth=0.1)
        elif by=='pm': fig2.scatter(mlt[n],mlat[n], color='y', marker='s', linewidth=0.1)
        elif by>0.5: fig2.scatter(mlt[n],mlat[n], color='r', linewidth=0.1)
        elif by<-0.5: fig2.scatter(mlt[n],mlat[n], color='b', linewidth=0.1)
        else: fig2.scatter(mlt[n],mlat[n], color='k', linewidth=0.1)
    plt.axis([0, 24, 70, 90])
    plt.xlabel('Magnetic local time')
    plt.ylabel('Magnetic latitude')
    plt.title('Polar MLT distribution')
    fig2.grid(True)
    
    plt.show()
    fig.savefig(newpath+"/MLTpolar.pdf",dpi=200)
    

#mlat=array(rfe[:,5],dtype=float)
#mlt=array(rfe[:,4],dtype=float)
#mltplot(mlat,mlt)

