from astropy.table import Table

# 打开星表FITS文件
stars_table = Table.read('mb_sc_tm15_u_20230602204159_239_sciimg_sexcat.fits',hdu=2)

# stars_table[(stars_table["SNR_WIN"] > 4.5) & (stars_table["SNR_WIN"] < 5.5)]

import numpy as np
import matplotlib.pyplot as plt

# 从stars_table中提取SNR_WIN和MAG_AUTO
snr = stars_table['SNR_WIN']
mag = stars_table['MAG_AUTO']
from astropy.stats import sigma_clip
snr_sigclip=sigma_clip(snr)
mag_sigclip=sigma_clip(mag)




plt.scatter(mag_sigclip,snr_sigclip,  s=0.1, alpha=0.5)



plt.xlabel('SNR_WIN')
plt.ylabel('MAG_AUTO')
plt.title('SNR_WIN and MAG_AUTO Fit')
plt.gca().invert_xaxis()
plt.show()