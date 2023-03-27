
from astropy.coordinates import SkyCoord
import astropy.units as u
from astropy.time import Time
import datetime,ephem
import numpy as np
#from astro import *
from astropy.table import *
from astropy.time import Time

def getsunalt(date=None):
        Site = ephem.Observer()
        Site.lon,Site.lat=  '100.03222222222','26.69777'
        Site.elevation=3000
        sun =  ephem.Sun()
        if date is None:
            Site.date=datetime.datetime.utcnow()
        else:
            Site.date=date
        sun.compute(Site)
        return sun.alt*180/np.pi
    
    
class Lijiang:
    '''
    为了简化,旧版本采用ephem计算
    '''
    Site=ephem.Observer()
    Site.lon,Site.lat= '100.03222222222','26.69777'
    Site.elevation=3000
    sun= ephem.Sun()
    moon=ephem.Moon()
    def __init__(self,ra,dec,time):
        self.Site.date=time
        self.sun.compute(self.Site)
        self.moon.compute(self.Site)
        self.ra=ra
        self.dec=dec
        self.obj=SkyCoord(ra=self.ra*u.deg,dec=self.dec*u.deg)
        self.ObserveObjectDB="GRB_ToO,f|M|A0,%i:%i:%.2f,%i:%i:%.2f,19.02,2000"%(self.obj.ra.hms.h,
                                                       self.obj.ra.hms.m,self.obj.ra.hms.s,
                                                       self.obj.dec.dms.d,abs(self.obj.dec.dms.m),
                                                                             abs(self.obj.dec.dms.s))
        self.ObserveObject = ephem.readdb(self.ObserveObjectDB)
        self.ObserveObject.compute(self.Site)
        #return self.ObserveObject.alt*180/np.pi,self.ObserveObject.az*180/np.pi
        self.ha=(self.Site.sidereal_time()-self.ra*np.pi/180)*u.rad.to(u.deg)
    def alt(self):
        return self.ObserveObject.alt*180/np.pi
    def azi(self):
        return self.ObserveObject.az*180/np.pi
    def siderealTime(self):
        return self.Site.sidereal_time()*180/np.pi
    def sunra(self):
        return self.sun.ra*180/np.pi
    def sundec(self):
        return self.sun.dec*180/np.pi
    def sunalt(self):
        return self.sun.alt*180/np.pi
    def sunazi(self):
        return self.sun.az*180/np.pi
    def moonra(self):
        return self.moon.ra*180/np.pi
    def moondec(self):
        return self.moon.dec*180/np.pi
    def moonalt(self):
        return self.moon.alt*180/np.pi
    def moonazi(self):
        return self.moon.az*180/np.pi
    def moonDistance(self):
        dis=self.obj.separation(SkyCoord(self.moonra()*u.deg,self.moondec()*u.deg)).deg
        #dis=ephem.separation((self.ObserveObject.alt,self.ObserveObject.az),
        #                         (self.moon.az, self.moon.alt))*180/np.pi
        return dis

    def moonPhase(self):

        return self.moon.moon_phase

    def airmass(self):
        ha=self.Site.sidereal_time()-self.ra*np.pi/180
        airmass=airmass_rad(ha,self.Site.lat,self.dec*np.pi/180)
        return airmass
    def hourangle(self):
        
        return self.ha
def airmass_rad(hour_angle,latitude,dec):
    """
    airmass at hour angle t
    """
    x = 1/(np.sin(latitude)*np.sin(dec)+np.cos(latitude)*np.cos(dec)*np.cos(hour_angle))  #t is hour angle
    delta_x = 0.00186*(x-1)+0.002875*((x-1)**2)+0.0008083*((x-1)**3)
    airmass = x - delta_x
    return float(airmass)
def airmass_deg(hour_angle,latitude,dec):
    return airmass_rad(hour_angle*np.pi/180,latitude*np.pi/180,dec*np.pi/180)
def convertHMSDMS(ra,dec):
    coor=SkyCoord(ra*u.deg,dec*u.deg)
    rahms='%02d:%02d:%05.2f'%(coor.ra.hms.h,coor.ra.hms.m,coor.ra.hms.s)
    decdms='%02d:%02d:%02d'%(coor.dec.dms.d,abs(coor.dec.dms.m),abs(coor.dec.dms.s))
    #print(rahms,decdms)
    return rahms,decdms