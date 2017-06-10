#Code used for finding RFEs and making the plots used in the Master Theisis of Kristian Reed
#Written by Kristian Reed 10.06.2017

#calculate clock angle!

import numpy as np
from matplotlib import pyplot as plt
from matplotlib import gridspec
from tools import *
import os

#New mlt plot to make different sizes depending on IMF value
def mltplot3(newpath,timeEvents,imf,radars,mlat,mlt):
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
        if imf[n][1]==0: continue
        by=imf[n][1]
        bz=imf[n][2]        #by=imf[n][2] for bz
        
        
       

#        if bz==str: continue
#        if bz>0:
        if isinstance(by, str) or isinstance(bz, str)== True:
            fig1.scatter(theta[n], r_rev[n], color='#777777', s=7)
            continue
        print 'By: '+str(by)+', Bz: '+str(bz)
        if bz>0: angle=arctan(abs(by/bz))*180/pi
        else: angle=180-arctan(abs(by/bz))*180/pi
        print angle 
        if 0 < angle < 45:
            fig1.scatter(theta[n], r_rev[n], color='r', s=20)
        elif 45 < angle < 135:
            fig1.scatter(theta[n], r_rev[n], color='#45dcf7', s=20)
        else: fig1.scatter(theta[n], r_rev[n], color='#f7df2c', s=20)
        
    fig1.scatter(0, 30, color='r', linewidth=0.1, label='${\\theta}$ < 45$\\degree$')
    fig1.scatter(0, 30, color='#45dcf7', linewidth=0.1, label='45$\\degree$ < $\\theta$ < 135$\\degree$')
    fig1.scatter(0, 30, color='#f7df2c', linewidth=0.1, label='$\\theta$ > 135$\\degree$')
    #fig1.scatter(0,30, color='y', marker='s', linewidth=0.1,label='Spread > 5 nT')
    fig1.scatter(0,30, color='#777777', linewidth=0.1,label='Sign change')
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
    fig1.axvline(2*np.pi*4/24, color='#b2b2b2', linestyle='solid',linewidth=2,zorder=4)
    fig1.axvline(2*np.pi*10/24, color='#b2b2b2', linestyle='solid',linewidth=2,zorder=4)
    fig1.axvline(2*np.pi*14/24, color='#b2b2b2', linestyle='solid',linewidth=2,zorder=4)
    fig1.axvline(2*np.pi*20/24, color='#b2b2b2', linestyle='solid',linewidth=2,zorder=4)
    
    fig2=plt.subplot(gs[1])
    for n in range(len(mlat)):
        if imf[n]==0: continue
        by=imf[n][1]
        if by=='pm': continue
        elif abs(by)>0.5: fig2.scatter(mlt[n],by, color='r', linewidth=0.1)
        else: continue #fig2.scatter(mlt[n],mlat[n], color='k', linewidth=0.1)
        
    for n in range(len(mlat)):
        if imf[n]==0: continue
        bz=imf[n][2]
        if bz=='pm': continue
        elif abs(bz)>0.5: fig2.scatter(mlt[n],bz, color='#45dcf7', linewidth=0.1)
        else: continue #fig2.scatter(mlt[n],mlat[n], color='k', linewidth=0.1)
     
    
    fig2.scatter(0, 30, color='r', linewidth=0.1, label='By')
    fig2.scatter(0, 30, color='#45dcf7', linewidth=0.1, label='Bz')
    fig2.legend(loc=1, borderaxespad=0.)
    plt.axis([0, 24, -8, 8])
    fig2.set_xticks([0,6,12,18,24])
    fig2.set_yticks([-8,-4,0,4,8])
    plt.xlabel('Magnetic local time')
    plt.ylabel('IMF [nT]')
    #plt.title('Polar MLT distribution')
    fig2.axvline(4, color='#b2b2b2', linestyle='solid',linewidth=1,zorder=4)
    fig2.axvline(10, color='#b2b2b2', linestyle='solid',linewidth=1,zorder=4)
    fig2.axvline(14, color='#b2b2b2', linestyle='solid',linewidth=1,zorder=4)
    fig2.axvline(20, color='#b2b2b2', linestyle='solid',linewidth=1,zorder=4)
    fig2.grid(True)
    
    plt.show()
    fig.savefig(newpath+"/MLTpolar.pdf",dpi=200)
    

#mlat=array(rfe[:,5],dtype=float)
#mlt=array(rfe[:,4],dtype=float)
#mltplot(mlat,mlt)

