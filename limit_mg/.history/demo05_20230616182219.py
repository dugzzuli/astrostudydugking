from astropy.table import Table
from scipy.optimize import curve_fit
import numpy as np
import matplotlib.pyplot as plt
from astropy.stats import sigma_clip

# 打开星表FITS文件
stars_table = Table.read('mb_sc_tm15_u_20230602204159_239_sciimg_sexcat.fits', hdu=2)

# 从stars_table中提取SNR_WIN和MAG_AUTO
snr = stars_table['SNR_WIN'][('SNR_WIN'>11.5) & ('SNR_WIN'>11.5)]
mag = stars_table['MAG_AUTO_S']