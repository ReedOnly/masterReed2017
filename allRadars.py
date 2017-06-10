#Code used for finding RFEs and making the plots used in the Master Theisis of Kristian Reed
#Written by Kristian Reed 10.06.2017

#All radar plot

import datetime as dt
import matplotlib.pyplot as plt
import davitpy.pydarn.plotting.plotMapGrd
from davitpy import pydarn
from davitpy.utils import *

fig = plt.figure(figsize=(9,9))
ax = fig.add_subplot(111)

sTime = dt.datetime(2014, 12, 16, 00, 38)
#sTime = dt.datetime(2014, 12, 04, 07, 56)
mObj = plotUtils.mapObj(boundinglat=65., lon_0=0, coords='mlt',datetime=sTime,gridLabels=True)
mapDatObj = davitpy.pydarn.plotting.plotMapGrd.MapConv(sTime, mObj, ax)
davitpy.pydarn.plotting.overlayFov(mObj, codes=['inv'], maxGate=70, beams=[])#,'rkn','cly','han','lyr'


#data = pydarn.sdio.radDataRead.radDataOpen(sTime, 'cly', eTime=sTime+dt.timedelta(seconds=60))
#scan = data.readScan()
#
#pydarn.plotting.fan.overlayFan(scan, mapDatObj, fig, 'velocity', coords='mag')
#
#
mapDatObj.overlayMapFitVel(pltColBar=True, 
        overlayRadNames=True, annotateTime=True, 
        colorBarLabelSize=15.,colMap=cm.hsv)

mapDatObj.overlayCnvCntrs()
#mapDatObj.overlayHMB()
plt.savefig('./2all.pdf', dpi=100)