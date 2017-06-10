#Code used for finding RFEs and making the plots used in the Master Theisis of Kristian Reed


#superDARN rfe plotter        Kristian reed 09.08.2016
import matplotlib
matplotlib.use('Agg') # Must be before importing matplotlib.pyplot or pylab!
from davitpy import pydarn
import davitpy.pydarn.sdio
from davitpy.pydarn.plotting import *
from davitpy.utils import *

import os
import datetime as dt

import matplotlib.pyplot as plt
from matplotlib import *
from scipy import *
import pandas as pd

from sdread import *
from tools import *
from fanRfe import *
from mltplot import *
import time


##########IF EDIT pandasRFE run:
    
"""
rfe2=array(pandasRfe)
save(newpath+'newData.npy',rfe2)
"""


#Initializing
sTime = dt.datetime(2014, 12, 16, 0)        #Scanning start Time
eTime = dt.datetime(2015, 1, 15, 0)     #Scanning end time
radars=['lol']  #'inv','rkn'  , 'cly'            #Radars to scan

rfelist=array([['cly',dt.datetime(2014, 12, 20, 23, 44)],         #1
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
     ['rkn',dt.datetime(2014, 12, 11, 10, 19)],        #46
     ['lyr',dt.datetime(2016, 12, 1, 7, 53)],        #47
     ['lyr',dt.datetime(2016, 12, 4, 1, 44)],        #48
     ['lyr',dt.datetime(2016, 12, 4, 11, 10)],        #49
     ['lyr',dt.datetime(2016, 12, 16, 10, 31)],        #50
     ['lyr',dt.datetime(2016, 12, 17, 3, 29)],        #51
     ['lyr',dt.datetime(2016, 12, 17, 7, 22)],        #52
     ['lyr',dt.datetime(2016, 12, 17, 8, 06)],        #53
     ['lyr',dt.datetime(2016, 12, 20, 10, 59)],        #54
     ['lyr',dt.datetime(2016, 12, 22, 4, 16)],        #55
     ['lyr',dt.datetime(2016, 12, 24, 6, 25)],        #56
     ['lyr',dt.datetime(2016, 12, 25, 4, 43)],        #57
     ['lyr',dt.datetime(2016, 12, 29, 6, 13)]])        #58
      
#rfelist=array([['inv',dt.datetime(2014, 12, 1, 16, 8)],         #14       Missing
#    ['cly',dt.datetime(2014, 12, 3, 11, 12)],         #20      Missing
#    ['cly',dt.datetime(2014, 12, 6, 10, 8)],        #25        Missing
#    ['cly',dt.datetime(2015, 12, 10, 22, 10)]])         #44        Missing
#rfelist=array([['lyr',dt.datetime(2016, 12, 1, 7, 53)],        #47
#     ['lyr',dt.datetime(2016, 12, 4, 1, 44)],        #48
#     ['lyr',dt.datetime(2016, 12, 4, 11, 10)],        #49
#     ['lyr',dt.datetime(2016, 12, 16, 10, 31)],        #50
#     ['lyr',dt.datetime(2016, 12, 17, 3, 29)],        #51
#     ['lyr',dt.datetime(2016, 12, 17, 7, 22)],        #52
#     ['lyr',dt.datetime(2016, 12, 17, 8, 06)],        #53
#     ['lyr',dt.datetime(2016, 12, 20, 10, 59)],        #54
#     ['lyr',dt.datetime(2016, 12, 22, 4, 16)],        #55
#     ['lyr',dt.datetime(2016, 12, 24, 6, 25)],        #56
#     ['lyr',dt.datetime(2016, 12, 25, 4, 43)],        #57
#     ['lyr',dt.datetime(2016, 12, 29, 6, 13)]])        #58

               
LoadFile=True  #True for local RFE file
SaveScratch=False	#Save in /scratch folder
SaveXlsx=True     #Save as .xlsx spreadsheet
SaveNpy=True        #Save as .npy file
RFEplot=True        #Make RFE plot
fanPlot=False

timerS=time.clock()

#Make path for storage
if SaveScratch:
	newpath='/scratch/rfeFiles/'+datetime.datetime.now().strftime("%Y-%m-%d-%H.%M/")
else:
	newpath=os.getcwd()+'/files/'+datetime.datetime.now().strftime("%Y-%m-%d-%H.%M/")

if not os.path.exists(newpath):
	os.makedirs(newpath)

#Loading stored file
if LoadFile: rfe=load(os.getcwd()+'/files/'+'rfeMasterCorr.npy')#15dec2014.npy

#Loading data and finding RFE
if not LoadFile:
    rfe=array([[0,0,0,0,0,0,0,0,0]])
    #for rad in radars:         #Uncomment for normal run!
    for n in range(len(rfelist)):    #Comment out for normal run!
        save(newpath+'data.npy',rfe)          #Save for every radar in case it stops
        timerSTmp=time.clock()
        rfeTmp=array([[0,0,0,0,0,0,0,0,0]])
        
        #rfeTmp=sdread(rfeTmp,rad,sTime,eTime)      #Uncomment for normal run!
        event=rfelist[n]            #Comment out for normal run!
        rfeTmp=sdread(rfeTmp,event[0],event[1],event[1]+datetime.timedelta(minutes=1))   #Comment out for normal run!
        
        rfeTmp = delete(rfeTmp, 0, axis=0)
        rfe = append(rfe,rfeTmp,axis=0)
        timerETmp=time.clock()
        print 'Time used for '+str(radars)+': '+secondsToStr(timerETmp-timerSTmp)
    
    if len(rfe)>1:
        rfe = delete(rfe, 0, axis=0)
        
pandasRfe=pd.DataFrame(rfe,columns=['Site','Beam','Gate','Lon(MLT)','MLT','Lat(mag)','Lon(mag)','IMF','Time'])      
pandasRfe.index+=1
#Output result
print pandasRfe[['Time','Site','Beam','Gate','MLT', 'IMF']]
print 'Time used: '+secondsToStr(time.clock()-timerS)




#Creating map with RFE
if RFEplot:
    plt.figure(figsize=(9,9))
    #plt.title(str(radars)+' from '+sTime.strftime("%Y.%m.%d %H:%M")+' until '+ eTime.strftime("%H:%M UTC"),fontsize="x-large")
    width = 111e3*60
    m = plotUtils.mapObj(width=width, height=width, lat_0=90., lon_0=65, coords='mag')
    # Plotting some radars
    overlayRadar(m, fontSize=20, codes=['inv','rkn','cly','han','lyr'])#'lyr'
    # Plot radar fov
    overlayFov(m, codes=['inv','rkn','cly','han','lyr'], maxGate=70, beams=[])#0,6,11,12,13,15 'inv','rkn','cly'
    #Add RFE points
    for i in range(len(rfe)):
        #Coordinates in map projection
        x,y=m(rfe[i,6],rfe[i,5])
        #x,y=lon,lat
        if rfe[i,0]=='inv': m.scatter(x, y, s=3, linewidths=2, color='g', zorder=2)
        elif rfe[i,0]=='rkn': m.scatter(x, y, s=3, linewidths=2, color='r', zorder=2)
        elif rfe[i,0]=='cly': m.scatter(x, y, s=3, linewidths=2, color='b', zorder=2)
        elif rfe[i,0]=='lyr': m.scatter(x, y, s=3, linewidths=2, color='c', zorder=2)
        elif rfe[i,0]=='han': m.scatter(x, y, s=3, linewidths=2, color='m', zorder=2)
        else: continue
            
        #legend
    m.scatter(0,0, s=3, linewidths=2, color='g', zorder=2,label='INV')
    m.scatter(0,0, s=3, linewidths=2, color='r', zorder=2,label='RKN')
    m.scatter(0,0, s=3, linewidths=2, color='b', zorder=2,label='CLY')
    m.scatter(0,0, s=3, linewidths=2, color='c', zorder=2,label='LYR')
    m.scatter(0,0, s=3, linewidths=2, color='m', zorder=2,label='HAN')
    plt.legend()
    
    pylab.savefig(newpath+"rfepos.pdf",dpi=200)
    print 'Saved rfe plot'
    #plt.show()
    
    #Make MLT plot
    mlat=array(rfe[:,5],dtype=float)
    mlt=array(rfe[:,4],dtype=float)
    timeEvents=rfe[:,8]
    imf=rfe[:,7]
    #mltplot2 for special plot
    mltplot(newpath,timeEvents,imf,radars,mlat,mlt)


#Produce .npy file
if SaveNpy:
    save(newpath+'data.npy',rfe)
    print 'Saved .npy file'
    
#Produce .xlsx file
if SaveXlsx:
    pandasRfe.to_excel(newpath+str(sTime.strftime("%Y-%m-%d-%H%M.xlsx")))
    print 'Saved .xlsx file'


#plotFanRfe(lon,lat,newpath,imf,sTime, rad, interval=60, fileType='fitex', param='velocity',
#            filtered=False, scale=[], channel=None, coords='geo',
#            colors='lasse', gsct=False, fov=True, edgeColors='face',
#            lowGray=False, fill=True, velscl=1000., legend=True,
#            overlayPoes=False, poesparam='ted', poesMin=-3., poesMax=0.5,
#            poesLabel=r"Total Log Energy Flux [ergs cm$^{-2}$ s$^{-1}$]",
#            overlayBnd=False, show=True, png=False, pdf=False, dpi=500,
#            tFreqBands=[]):
if fanPlot and len(rfe)>1:    
    for i in range(len(rfe)):#len(rfe)
        #i=-5+n
        print '***Plot ',i,' out of ',len(rfe)-1,'   ',secondsToStr(time.clock()-timerS),'***'
        plotFanRfe(rfe[i,3],rfe[i,5],newpath,rfe[i,7],rfe[i,8],[rfe[i,0]], param='velocity',interval=60, fileType='fitex',
                                scale=[-500,500],coords='mlt',gsct=True,fill=True,overlayPoes=False,
                                show=False, png=True,pdf=False,dpi=200)
        print 'time used: '+ secondsToStr(time.clock()-timerS)
    print 'Saved fan plot figures'
    
timerE=time.clock()
print 'Total time used: '+secondsToStr(timerE-timerS)
    
    
