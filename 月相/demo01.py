import datetime

from astropy.coordinates import SkyCoord
import astropy.units as u
from loguru import logger

from astronomia import Lijiang

if __name__=="__main__":
    rahms="10:00:00"
    decdms="+70:00:00"

    sc=SkyCoord(rahms+' '+decdms,unit=(u.hourangle,u.deg))
    x=Lijiang(sc.ra.deg,sc.dec.deg,datetime.datetime.utcnow())
    logger.info(f"月距:{x.moonDistance()}")
    logger.info(f"月相:{x.moonPhase()}") #百分比