#Code used for finding RFEs and making the plots used in the Master Theisis of Kristian Reed
#Written by Kristian Reed 10.06.2017

# -*- coding: utf-8 -*-

from __future__ import print_function, division, absolute_import
import datetime as dt
import matplotlib.pyplot as plt
import matplotlib as mpl
import cvdm
import nompy
from scipy import *

sz = cvdm.journal_sizes.agu(baseFontSize=7)

rfelist=array([['cly',dt.datetime(2014, 12, 20, 23, 40)],         #1
     ['inv',dt.datetime(2014, 12, 16, 00, 38)],         #2
     ['inv',dt.datetime(2014, 12, 16, 21, 20)],         #3
     ['rkn',dt.datetime(2015, 12, 10, 18, 39)],         #4
     ['rkn',dt.datetime(2015, 12, 11, 13, 57)],         #5
     ['rkn',dt.datetime(2015, 12, 12, 13, 36)],         #6
     ['rkn',dt.datetime(2015, 12, 12, 17, 32)],         #7
     ['rkn',dt.datetime(2015, 12, 13, 14, 57)],         #8
     ['inv',dt.datetime(2015, 12, 9, 23, 03)],         #9
     ['inv',dt.datetime(2014, 12, 15, 0, 41)],         #10
     ['inv',dt.datetime(2014, 12, 18, 21, 43)],         #11
     ['inv',dt.datetime(2014, 12, 20, 19, 34)],         #12
     ['rkn',dt.datetime(2014, 12, 15, 0, 29)],         #13
     ['inv',dt.datetime(2014, 12, 1, 16, 8)],         #14       Missing
     ['rkn',dt.datetime(2014, 12, 15, 1, 11)],         #15
     ['rkn',dt.datetime(2014, 12, 17, 15, 0)],         #16
     ['rkn',dt.datetime(2014, 12, 17, 16, 0)],         #17
     ['rkn',dt.datetime(2014, 12, 18, 14, 05)],         #18
     ['rkn',dt.datetime(2014, 12, 20, 17, 26)],         #19
     ['cly',dt.datetime(2014, 12, 3, 11, 12)],         #20      Missing
     ['cly',dt.datetime(2014, 12, 3, 12, 32)],         #21
     ['cly',dt.datetime(2014, 12, 3, 21, 32)],         #22
     ['cly',dt.datetime(2014, 12, 4, 7, 45)],         #23
     ['cly',dt.datetime(2014, 12, 4, 10, 35)],         #24
     ['cly',dt.datetime(2014, 12, 6, 10, 8)],        #25        Missing
     ['cly',dt.datetime(2014, 12, 8, 22, 03)],        #26
     ['cly',dt.datetime(2014, 12, 11, 21, 54)],         #27
     ['cly',dt.datetime(2014, 12, 13, 1, 42)],         #28
     ['cly',dt.datetime(2014, 12, 14, 14, 6)],         #29
     ['cly',dt.datetime(2014, 12, 14, 14, 58)],         #30
     ['cly',dt.datetime(2014, 12, 17, 21, 11)],         #31
     ['cly',dt.datetime(2014, 12, 19, 23, 23)],        #32
     ['han',dt.datetime(2014, 12, 14, 5, 57)],        #33
     ['inv',dt.datetime(2014, 12, 1, 11, 46)],         #34
     ['inv',dt.datetime(2014, 12, 1, 12, 19)],         #35
     ['inv',dt.datetime(2014, 12, 1, 15, 47)],         #36
     ['inv',dt.datetime(2014, 12, 3, 11, 21)],         #37
     ['inv',dt.datetime(2014, 12, 3, 15, 31)],         #38
     ['inv',dt.datetime(2014, 12, 3, 15, 50)],         #39
     ['inv',dt.datetime(2014, 12, 4, 7, 14)],         #40
     ['inv',dt.datetime(2014, 12, 4, 7, 56)],         #41
     ['inv',dt.datetime(2014, 12, 4, 18, 46)],         #42
     ['inv',dt.datetime(2014, 12, 8, 14, 07)],         #43
     ['cly',dt.datetime(2015, 12, 10, 22, 10)],         #44         Missing
     ['rkn',dt.datetime(2014, 12, 10, 11, 03)],        #45
     ['rkn',dt.datetime(2014, 12, 11, 10, 19)]])


#rfelist=array([[2,'inv',dt.datetime(2014, 12, 16, 00, 14),49],         #2
#     [13,'rkn',dt.datetime(2014, 12, 15, 0, 19),24],         #13
#     #[14,'inv',dt.datetime(2014, 12, 1, 16, 07),15],         #14       Missing
#     [28,'cly',dt.datetime(2014, 12, 13, 0, 18),97],         #28
#     [40,'inv',dt.datetime(2014, 12, 4, 7, 10),22],
#     #[41,'inv',dt.datetime(2014, 12, 4, 7, 50),7],         #41
#     [42,'inv',dt.datetime(2014, 12, 4, 18, 39),11]])         #42])

rfelist=array([[42,'inv',dt.datetime(2014, 12, 4, 18, 39),11]])


for n in range(len(rfelist)):
    event=rfelist[n][2]
    START = event - dt.timedelta(minutes=60)
    END = event + dt.timedelta(minutes=30)
    duration=rfelist[n][3]
    rfenr=rfelist[n][0]
    
    #==============================================================================
    ### Figure setup
    #==============================================================================
    
    fig = plt.figure(figsize=(sz.textwidth, sz.textwidth*0.8), dpi=sz.dpi(sz.textwidth*1.5))
    
    ax1 = plt.subplot(4, 1, 1)
    ax2 = plt.subplot(4, 1, 2, sharex=ax1)
    ax3 = plt.subplot(4, 1, 3, sharex=ax1)
    ax4 = plt.subplot(4, 1, 4, sharex=ax1)
    
    plt.subplots_adjust(top=0.97, bottom=0.08, left=0.12, right=0.96, hspace=0.2)
    
    ax1.set_xlim(START, END)
    for ax in [ax1,ax2,ax3]:
        plt.setp(ax.get_xticklabels(), visible=False)
    
    #==============================================================================
    ### Get data
    #==============================================================================
    
    #p = nompy.get_params(START, END, [14, 17, 18, 22, 25, 37], res='5min')
    p1 = nompy.get_params(START, END, [14, 17, 18, 22, 25, 37], res='min')
    
    #==============================================================================
    ### Plot data
    #==============================================================================
    
    #--- Bx, By, Bz
    
    # FIXME: 5min or 1min (p2)?
    #ax1.plot(p1.index, p1['Bx'], label='Bx',color='#D95F02')
    ax1.plot(p1.index, p1['By GSM'], label='By', color='#1B9E77')
    ax1.plot(p1.index, p1['Bz GSM'], label='Bz', color='#D95F02')
    ax1.hlines(0, START, END, linestyle='solid')
    leg = ax1.legend(ncol=3, frameon=False, loc='upper right', bbox_to_anchor=(0.4, 1))
    for legobj in leg.legendHandles:
        legobj.set_linewidth(sz.lw*2)
    ax1.set_ylim(-8, 10)
    ax1.set_ylabel('IMF [nT]')
    ax1.set_title('OMNI solar wind data for '+START.strftime('%d.%m.%Y   %H:%M')+' - '+END.strftime('%H:%M')+' UT')
    ax1.set_yticks([-8, -4, 0, 4, 8])
    ax1.grid(True)
    cvdm.pull_outer_ticklabels(ax1, 'y', 'lower')
    ax1.text(0.03, 0.9, '(a)', ha='left', va='top', transform=ax1.transAxes, fontweight='bold')
    
    #--- Vx
    
    ax2.plot(p1.index, p1['Vx'],color='#1B9E77')
    ax2.set_ylim(-700, -200)
    ax2.set_ylabel('Vx [km/s]')
    ax2.set_yticks([-700,-600, -500, -400, -300, -200])
    ax2.grid(True)
    cvdm.pull_outer_ticklabels(ax2, 'y', 'both')
    ax2.text(0.03, 0.9, '(b)', ha='left', va='top', transform=ax2.transAxes, fontweight='bold')
    
    #--- IMF clock angle
    theta=zeros(len(p1))
    by=array(p1['By GSM'])
    bz=array(p1['Bz GSM'])
    for t in range(len(p1)):
        if by[t] or bz[t]==nan: theta[t]=nan
        if bz[t]>0:
            theta[t]=arctan(abs(by[t]/bz[t]))*180/pi
        else:
            theta[t]=180-arctan(abs(by[t]/bz[t]))*180/pi
        
    ax3.plot(p1.index, theta,color='#D95F02')
    ax3.set_ylim(0,180)
    ax3.set_ylabel('Clock angle [deg]')
    ax3.set_yticks([0,45,90,135,180])
    ax3.grid(True)
    cvdm.pull_outer_ticklabels(ax3, 'y', 'both')
    ax3.text(0.03, 0.9, '(c)', ha='left', va='top', transform=ax3.transAxes, fontweight='bold')
    ax3.set_ylim(ax.get_ylim()[::-1])
    
    #--- Density
    ax4.plot(p1.index, p1['Dens'],color='#1B9E77')
    ax4.set_ylim(0, 10)
    ax4.set_ylabel('Density [cm$\mathdefault{^{-3}}$]')
    ax4.set_xlabel('UT (time-shifted to bow shock)')
    ax4.set_yticks([0, 5,10])
    ax4.grid(True)
    cvdm.pull_outer_ticklabels(ax4, 'y', 'upper')
    ax4.text(0.03, 0.9, '(d)', ha='left', va='top', transform=ax4.transAxes, fontweight='bold')
    
    
    #--- format time axis
    ax4.xaxis.set_major_locator(mpl.dates.MinuteLocator(byminute=[0,10,20,30,40,50]))
    ax4.xaxis.set_minor_locator(mpl.dates.MinuteLocator(byminute=[5,15,25,35,45,55]))
    ax4.xaxis.set_major_formatter(mpl.dates.DateFormatter('%H:%M'))
    
    #---- Make shaded area
    for ax in [ax1, ax2, ax3, ax4]:
        plt.axes(ax)
        plt.axvspan(xmin=event - dt.timedelta(minutes=6), xmax=event + dt.timedelta(minutes=duration-6), color='0.9')
        plt.axvline(event, color='k', linestyle='solid')
        
    #--- adjust ticklabels
    for ax in [ax1, ax2]:
        ax.yaxis.set_label_coords(-0.1, 0.5)
    plt.tight_layout()
    plt.savefig('./files/OmniPlot_new2/'+str(rfenr)+'omni.pdf', dpi=200,bbox_inches='tight')
