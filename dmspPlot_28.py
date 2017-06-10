#Code used for finding RFEs and making the plots used in the Master Theisis of Kristian Reed
#Written by Kristian Reed 10.06.2017

from __future__ import print_function, division

import datetime as dt

import numpy as np
import matplotlib.pyplot as plt
from scipy.io import netcdf
from matplotlib import patheffects as pe
import matplotlib as mpl

import basemag
import cvdm

from davitpy import utils
from davitpy import pydarn
from davitpy.utils import *

#from fanRfe import *
from tools import *

sz = cvdm.journal_sizes.agu(baseFontSize=7)
#plt.figure(figsize=(sz.maxwidth, sz.maxwidth), dpi=sz.dpi(sz.maxwidth*11/8.5))

fig=plt.figure()
ax = fig.add_subplot(111)
plt.subplots_adjust(bottom=0.1, left=0.02, top=0.95, right=0.92, wspace=0.01)

map_date_ = dt.datetime(2014, 12, 13, 0, 22)

#f ='./files/dmsp/rfe28_PS.APL_V0116S024CE0008_SC.U_DI.A_GP.F17-SSUSI_PA.APL-SDR-DISK_DD.20141213_SN.41821-00_DF.NC' #my file
f ='./files/dmsp/rfe28_PS.APL_V0116S024CB0005_SC.U_DI.A_GP.F18-SSUSI_PA.APL-SDR-DISK_DD.20141213_SN.26564-00_DF.NC' #my file
#f ='./files/dmsp/rfe28_PS.APL_V0116S024CB0005_SC.U_DI.A_GP.F18-SSUSI_PA.APL-SDR-DISK_DD.20141213_SN.26563-00_DF.NC' #my file

map_ = basemag.Basemag(datetime=map_date_, lon_0='mlt', lat_0=90,
                        width=5e6, height=5e6, resolution='l', ax=ax)


#map_ = utils.mapObj(boundinglat=65., lon_0=270, coords='mlt',datetime=map_date_)

#plt.figure(figsize=(9,9))


title = 'RFE:28 DMSP F18 and SuperDARN 13 Dec. 2014 01:43'

map_.drawcoastlines(linewidth=0.5, zorder=4, color='.7')
map_.fillcontinents(color='0.95')
map_.drawparallels(range(0, 90, 5), color='0.6', coords='mlt', lonlabel=0.5,
                   lonlabel_kwargs=dict(color='0.6', fontweight='bold',
                                        path_effects=[pe.withStroke(foreground='w', linewidth=sz.lw*4)]))
map_.drawmeridians(range(0, 24, 1), coords='mlt', color='0.6', latmax=85)

ax.set_title(title, loc='left', fontsize='medium')


# SSUSI
fh = netcdf.netcdf_file(f, mmap=False)

lats = fh.variables['PIERCEPOINT_DAY_LATITUDE'].data
lons = fh.variables['PIERCEPOINT_DAY_LONGITUDE'].data
alts = fh.variables['PIERCEPOINT_DAY_ALTITUDE'].data

sc_lat = fh.variables['DMSP_LATITUDE'].data.ravel()
sc_lon = fh.variables['DMSP_LONGITUDE'].data.ravel()
sc_alt = fh.variables['DMSP_ALTITUDE'].data.ravel()
sc_time = [dt.datetime(2014, 12, 13) + dt.timedelta(seconds=x) for x in fh.variables['DMSP_COORDS_TIME'].data.ravel()]

           

data1 = fh.variables['DISK_INTENSITY_DAY'].data[:, :, 2]
data2 = fh.variables['DISK_INTENSITY_DAY'].data[:, :, 3]
data3 = fh.variables['DISK_INTENSITY_DAY'].data[:, :, 4]

uselats = np.nanmin(lats, axis=0) > 60

N = 1
 #   for data in [data1, data2, data3]:
for data in [data2]:
    p = map_.pcolormesh(lons[:, uselats], lats[:, uselats], data[:, uselats], latlon=True, coords='geo', zorder=1.9,
                        vmin=0, vmax=1000,
                        ax=ax, alpha=1/N, cmap='Greens')
    p.set_rasterized(True)
    N += 1

#===================================================
#Satellite Trajectory
#===================================================  
#Add Time tag
for i, time in enumerate(sc_time):
    if time.minute % 5 == 0 and time.second == 0:
        x, y = map_(sc_lon[i], sc_lat[i], coords='geo')#, height=sc_alt[i])
        if map_.llcrnrx < x < map_.urcrnrx and map_.llcrnry < y < map_.urcrnry:
            map_.plot(x, y, marker='o', markersize=6, color='b', markeredgecolor='w', zorder=7, ax=ax)
            ax.text(x, y, 'DMSP '+'{:%H:%M}'.format(time), color='k', zorder=7, fontsize=3, fontweight='bold',
                          path_effects=[pe.withStroke(foreground='w', linewidth=2)])

#Add sircle for every minute            
for i, time in enumerate(sc_time):
    if time.second == 0:
        x, y = map_(sc_lon[i], sc_lat[i], coords='geo')#, height=sc_alt[i])
        if map_.llcrnrx < x < map_.urcrnrx and map_.llcrnry < y < map_.urcrnry:
            map_.plot(x, y, marker='o', markersize=3, color='b', markeredgecolor='w', zorder=7, ax=ax)

#Add satellite track
map_.plot(sc_lon, sc_lat, latlon=True, coords='geo', color='b',# height=sc_alt,
          zorder=6, ax=ax, path_effects=[pe.withStroke(foreground='w', linewidth=2)])


##Swarm-B
#latSwarm,lonSwarm,timeSwarm=satorbit('./files/orbits/28_SW-B.txt')
#map_.plot(lonSwarm, latSwarm, latlon=True, coords='geo', color='r',
#          zorder=6, ax=ax, path_effects=[pe.withStroke(foreground='w', linewidth=2)])
#
#for i, time in enumerate(timeSwarm):
#    if time.minute % 5 == 0 and time.second == 0:
#        x, y = map_(lonSwarm[i], latSwarm[i], coords='geo')#, height=sc_alt[i]
#        if map_.llcrnrx < x < map_.urcrnrx and map_.llcrnry < y < map_.urcrnry:
#            map_.plot(x, y, marker='o', markersize=6, color='r', markeredgecolor='w', zorder=7, ax=ax)
#            ax.text(x, y, 'SWARM B '+'{:%H:%M}'.format(time), color='k', zorder=7,fontsize=3, fontweight='bold',
#                          path_effects=[pe.withStroke(foreground='w', linewidth=2)])
#
##Add sircle for every minute            
#for i, time in enumerate(timeSwarm):
#    if time.second == 0:
#        x, y = map_(lonSwarm[i], latSwarm[i], coords='geo')#, height=sc_alt[i]
#        if map_.llcrnrx < x < map_.urcrnrx and map_.llcrnry < y < map_.urcrnry:
#            map_.plot(x, y, marker='o', markersize=3, color='r', markeredgecolor='w', zorder=7, ax=ax)
#            
#         

##Meteop-A
lat2,lon2,time2=satorbit('./files/orbits/28_Meteop-A.txt')
map_.plot(lon2, lat2, latlon=True, coords='geo', color='g',
          zorder=6, ax=ax, path_effects=[pe.withStroke(foreground='w', linewidth=2)])

for i, time in enumerate(time2):
    if time.minute % 5 == 0 and time.second == 0:
        x, y = map_(lon2[i], lat2[i], coords='geo')#, height=sc_alt[i]
        if map_.llcrnrx < x < map_.urcrnrx and map_.llcrnry < y < map_.urcrnry:
            map_.plot(x, y, marker='o', markersize=6, color='g', markeredgecolor='w', zorder=7, ax=ax)
            ax.text(x, y, 'Meteop-A '+'{:%H:%M}'.format(time), color='k', zorder=7, fontsize=3, fontweight='bold',
                          path_effects=[pe.withStroke(foreground='w', linewidth=2)])

#Add sircle for every minute
for i, time in enumerate(time2):
    if time.second == 0:
        x, y = map_(lon2[i], lat2[i], coords='geo')#, height=sc_alt[i]
        if map_.llcrnrx < x < map_.urcrnrx and map_.llcrnry < y < map_.urcrnry:
            map_.plot(x, y, marker='o', markersize=3, color='g', markeredgecolor='w', zorder=7, ax=ax)
#===================================================
#Add SuperDARN Scan
#================================================cly===
sTime=dt.datetime(2014, 12, 13, 1, 43)
data = pydarn.sdio.radDataRead.radDataOpen(sTime, 'inv', eTime=sTime+dt.timedelta(seconds=60))
scan = data.readScan(firstBeam=0,useEvery=1,showBeams=True)
#fov = pydarn.radar.radFov.fov(site='inv',ngates=scan[0].prm.nrang,coords='mag')
#pydarn.plotting.overlayFov(map_, codes=['inv'], maxGate=70, beams=[])

ax2 = fig.add_subplot(111)
intensities,pcoll=pydarn.plotting.fan.overlayFan(scan, map_, fig, 'velocity', coords='mag', gsct=False, site=None,
               fov=None, gs_flg=[], fill=True, velscl=500., dist=500.,cmap='seismic',
               norm=plt.Normalize(vmin=-500, vmax=500), alpha=0.9)
    
#Colorbars
cvdm.cbar_below(ax, mappable=p, topOffset=0.01, height=0.015, rasterize=True, ticks=[0, 250, 500, 750, 1000], label='Radiance [R]')



cvdm.cbar_right(ax2, use_ColorbarBase=True, cmap='seismic', norm=plt.Normalize(vmin=-500, vmax=500),
                ticks=[-500, -250, 0, 250, 500], label='Velocity [m/s]')

plt.savefig('./28dmspInv43.pdf', dpi=200)