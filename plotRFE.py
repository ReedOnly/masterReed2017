#Code used for finding RFEs and making the plots used in the Master Theisis of Kristian Reed
#Written by Kristian Reed 10.06.2017


import datetime as dt
import os
import matplotlib.pyplot as plt
from davitpy import pydarn
import davitpy.pydarn.sdio
from davitpy.pydarn.plotting import *
from davitpy.utils import *

from fanRfe import *
from tools import *

import davitpy.pydarn.plotting.plotMapGrd
import matplotlib.cm as cm

newpath=os.getcwd()+'/files/'+'rfeWidth/'
if not os.path.exists(newpath):
	os.makedirs(newpath)
 
 
 
"""
    World radar day 2014
     ['cly',dt.datetime(2014, 12, 20, 23, 44),a,b],         #1
     ['inv',dt.datetime(2014, 12, 16, 00, 38),a,b],       #2
     ['inv',dt.datetime(2014, 12, 16, 21, 20),a,b],         #3
    
    World radar day 2015
     ['rkn',dt.datetime(2015, 12, 10, 18, 39),a,b],         #4
     ['rkn',dt.datetime(2015, 12, 11, 13, 57),a,b],         #5
     ['rkn',dt.datetime(2015, 12, 12, 13, 36),a,b],         #6
     ['rkn',dt.datetime(2015, 12, 12, 17, 32),a,b],         #7
     ['rkn',dt.datetime(2015, 12, 13, 14, 57),a,b]          #8
     
     ['inv',dt.datetime(2015, 12, 9, 23, 03),a,b],          #9
     
     ['inv',dt.datetime(2014, 12, 15, 0, 41),a,b],         #10
     ['inv',dt.datetime(2014, 12, 18, 21, 43),a,b],         #11
     ['inv',dt.datetime(2014, 12, 20, 19, 34),a,b],         #12
     ['rkn',dt.datetime(2014, 12, 15, 0, 29),a,b],         #13
     ['inv',dt.datetime(2014, 12, 1, 16, 8),a,b],         #14
     ['rkn',dt.datetime(2014, 12, 15, 1, 11),a,b],         #15
     ['rkn',dt.datetime(2014, 12, 17, 15, 0),a,b],         #16
     ['rkn',dt.datetime(2014, 12, 17, 16, 0),a,b],         #17
     ['rkn',dt.datetime(2014, 12, 18, 14, 05),a,b],         #18
     ['rkn',dt.datetime(2014, 12, 20, 17, 26),a,b],         #19
     ['cly',dt.datetime(2014, 12, 3, 11, 12),a,b],         #20
     ['cly',dt.datetime(2014, 12, 3, 12, 32),a,b],         #21
     ['cly',dt.datetime(2014, 12, 3, 21, 32),a,b],         #22
     ['cly',dt.datetime(2014, 12, 4, 7, 45),a,b],         #23
     ['cly',dt.datetime(2014, 12, 4, 10, 35),a,b],         #24
     ['cly',dt.datetime(2014, 12, 6, 10, 8),a,b],        #25
     ['cly',dt.datetime(2014, 12, 8, 22, 03),a,b],        #26
     ['cly',dt.datetime(2014, 12, 11, 21, 54),a,b],         #27
     ['cly',dt.datetime(2014, 12, 13, 1, 42),a,b],         #28
     ['cly',dt.datetime(2014, 12, 14, 14, 6),a,b],         #29
     ['cly',dt.datetime(2014, 12, 14, 14, 58),a,b],         #30
     ['cly',dt.datetime(2014, 12, 17, 21, 11),a,b],         #31
     ['cly',dt.datetime(2014, 12, 19, 23, 23),a,b],        #32
     ['han',dt.datetime(2014, 12, 14, 5, 57),a,b],        #33
     
     ['inv',dt.datetime(2014, 12, 1, 11, 46),a,b],         #34
     ['inv',dt.datetime(2014, 12, 1, 12, 19),a,b],         #35
     ['inv',dt.datetime(2014, 12, 1, 15, 47),a,b],         #36
     ['inv',dt.datetime(2014, 12, 3, 11, 21),a,b],         #37
     ['inv',dt.datetime(2014, 12, 3, 15, 31),a,b],         #38
     ['inv',dt.datetime(2014, 12, 3, 15, 50),a,b],         #39
     ['inv',dt.datetime(2014, 12, 4, 7, 14),a,b],         #40
     ['inv',dt.datetime(2014, 12, 4, 7, 56),a,b],         #41
     ['inv',dt.datetime(2014, 12, 4, 18, 46),a,b],         #42
     ['inv',dt.datetime(2014, 12, 8, 14, 07),a,b],         #43
     ['cly',dt.datetime(2015, 12, 10, 22, 10),a,b],         #44
     ['rkn',dt.datetime(2014, 12, 10, 11, 03),a,b],        #45
     ['rkn',dt.datetime(2014, 12, 11, 10, 19),a,b],        #46
     
     
     
     
"""
 
 
 
 
 
 
 
a=0
b=1

rfe=[['cly',dt.datetime(2014, 12, 20, 23, 44),a,b],         #1
     ['inv',dt.datetime(2014, 12, 16, 00, 38),a,b],       #2
     ['inv',dt.datetime(2014, 12, 16, 21, 20),a,b],         #3
     ['rkn',dt.datetime(2015, 12, 10, 18, 39),a,b],         #4
     ['rkn',dt.datetime(2015, 12, 11, 13, 57),a,b],         #5
     ['rkn',dt.datetime(2015, 12, 12, 13, 36),a,b],         #6
     ['rkn',dt.datetime(2015, 12, 12, 17, 32),a,b],         #7
     ['rkn',dt.datetime(2015, 12, 13, 14, 57),a,b],          #8
     ['inv',dt.datetime(2015, 12, 9, 23, 03),a,b],          #9
     ['inv',dt.datetime(2014, 12, 15, 0, 41),a,b],         #10
     ['inv',dt.datetime(2014, 12, 18, 21, 43),a,b],         #11
     ['inv',dt.datetime(2014, 12, 20, 19, 34),a,b],         #12
     ['rkn',dt.datetime(2014, 12, 15, 0, 29),a,b],         #13
     ['inv',dt.datetime(2014, 12, 1, 16, 8),a,b],         #14
     ['rkn',dt.datetime(2014, 12, 15, 1, 11),a,b],         #15
     ['rkn',dt.datetime(2014, 12, 17, 15, 0),a,b],         #16
     ['rkn',dt.datetime(2014, 12, 17, 16, 0),a,b],         #17
     ['rkn',dt.datetime(2014, 12, 18, 14, 05),a,b],         #18
     ['rkn',dt.datetime(2014, 12, 20, 17, 26),a,b],         #19
     ['cly',dt.datetime(2014, 12, 3, 11, 12),a,b],         #20
     ['cly',dt.datetime(2014, 12, 3, 12, 32),a,b],         #21
     ['cly',dt.datetime(2014, 12, 3, 21, 32),a,b],         #22
     ['cly',dt.datetime(2014, 12, 4, 7, 45),a,b],         #23
     ['cly',dt.datetime(2014, 12, 4, 10, 35),a,b],         #24
     ['cly',dt.datetime(2014, 12, 6, 10, 8),a,b],        #25
     ['cly',dt.datetime(2014, 12, 8, 22, 03),a,b],        #26
     ['cly',dt.datetime(2014, 12, 11, 21, 54),a,b],         #27
     ['cly',dt.datetime(2014, 12, 13, 1, 42),a,b],         #28
     ['cly',dt.datetime(2014, 12, 14, 14, 6),a,b],         #29
     ['cly',dt.datetime(2014, 12, 14, 14, 58),a,b],         #30
     ['cly',dt.datetime(2014, 12, 17, 21, 11),a,b],         #31
     ['cly',dt.datetime(2014, 12, 19, 23, 23),a,b],        #32
     ['han',dt.datetime(2014, 12, 14, 5, 57),a,b],        #33
     ['inv',dt.datetime(2014, 12, 1, 11, 46),a,b],         #34
     ['inv',dt.datetime(2014, 12, 1, 12, 19),a,b],         #35
     ['inv',dt.datetime(2014, 12, 1, 15, 47),a,b],         #36
     ['inv',dt.datetime(2014, 12, 3, 11, 21),a,b],         #37
     ['inv',dt.datetime(2014, 12, 3, 15, 31),a,b],         #38
     ['inv',dt.datetime(2014, 12, 3, 15, 50),a,b],         #39
     ['inv',dt.datetime(2014, 12, 4, 7, 14),a,b],         #40
     ['inv',dt.datetime(2014, 12, 4, 7, 56),a,b],         #41
     ['inv',dt.datetime(2014, 12, 4, 18, 46),a,b],         #42
     ['inv',dt.datetime(2014, 12, 8, 14, 07),a,b],         #43
     ['cly',dt.datetime(2015, 12, 10, 22, 10),a,b],         #44
     ['rkn',dt.datetime(2014, 12, 10, 11, 03),a,b],        #45
     ['rkn',dt.datetime(2014, 12, 11, 10, 19),a,b],       #46
     ['lyr',dt.datetime(2016, 12, 1, 7, 53),a,b],        #47
     ['lyr',dt.datetime(2016, 12, 4, 1, 44),a,b],        #48
     ['lyr',dt.datetime(2016, 12, 4, 11, 10),a,b],        #49
     ['lyr',dt.datetime(2016, 12, 16, 10, 31),a,b],        #50
     ['lyr',dt.datetime(2016, 12, 17, 3, 29),a,b],        #51
     ['lyr',dt.datetime(2016, 12, 17, 7, 22),a,b],        #52
     ['lyr',dt.datetime(2016, 12, 17, 8, 06),a,b],        #53
     ['lyr',dt.datetime(2016, 12, 20, 10, 59),a,b],        #54
     ['lyr',dt.datetime(2016, 12, 22, 4, 16),a,b],        #55
     ['lyr',dt.datetime(2016, 12, 24, 6, 25),a,b],        #56
     ['lyr',dt.datetime(2016, 12, 25, 4, 43),a,b],        #57
     ['lyr',dt.datetime(2016, 12, 29, 6, 13),a,b]]        #58
      
#rfe=[['inv',dt.datetime(2014, 12, 4, 7, 10),2,20]]
for n in range(len(rfe)):
    element=rfe[n]      
    sTimeRfe = element[1]
    rad=[element[0]]
    for t in range(-element[2],element[3]):
        sTime= sTimeRfe + dt.timedelta(minutes=t)
        
        year=sTime.year
        day=sTime.timetuple().tm_yday
        hour=sTime.hour
        minute=sTime.minute
        imf=get_imf(sTime)
        
            
#       pydarn.plotting.fan.plotFan(sTime,rad, param='velocity',interval=60, fileType='fitex',
#                                scale=[-500,500],coords='mlt',gsct=False,fill=True,
#                                show=False, png=True,pdf=False,dpi=200)
        
        print sTime
        plotFanRfe(0,0,newpath,imf,sTime,rad, param='width',interval=60, fileType='fitex',
                    filtered=False, scale=[-500,500], channel=None, coords='mlt',
                    colors='lasse', gsct=True, fov=True, edgeColors='face',
                    lowGray=False, fill=True, velscl=1000., legend=True,
                    overlayPoes=False, poesparam='ted', poesMin=-3., poesMax=0.5,
                    poesLabel=r"Total Log Energy Flux [ergs cm$^{-2}$ s$^{-1}$]",
                    overlayBnd=False, show=False, png=True, pdf=False, dpi=200,
                    tFreqBands=[])



#fig = plt.figure(figsize=(10,10))
#ax = fig.add_subplot(111)
#mObj = plotUtils.mapObj(boundinglat=50.,gridLabels=True, coords='mlt',dateTime=sTime)
#mapDatObj = davitpy.pydarn.plotting.plotMapGrd.MapConv(sTime, mObj, ax)
##mapDatObj.overlayMapFitVel()
#mapDatObj.overlayCnvCntrs()




#a=raw_input("Press Enter to continue...")






#fig.savefig(os.getcwd()+"/convection_los.png",dpi=400)