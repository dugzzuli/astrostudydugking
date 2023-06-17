from astropy.table import Table
from scipy.optimize import curve_fit
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

# 定义指数函数
def exp_func(x, a, b, c):
    return a * np.exp(-b * x) + c

# 进行指数函数拟合
popt, _ = curve_fit(exp_func, mag_sigclip, snr_sigclip)

# 绘制散点图和拟合曲线
plt.scatter(mag_sigclip, snr_sigclip, s=0.1, alpha=0.5)
plt.plot(mag_sigclip, exp_func(mag_sigclip, *popt), color='red')
plt.xlabel('MAG_AUTO')
plt.ylabel('SNR_WIN')
plt.title('SNR_WIN and MAG_AUTO Fit')
plt.gca().invert_xaxis()
plt.show()

# # 进行二次函数拟合
# fit_params = np.polyfit(mag_sigclip, snr_sigclip, 2)
# fit_func = np.poly2d(fit_params)

# # 绘制散点图和拟合曲线
# plt.scatter(mag_sigclip, snr_sigclip, s=0.1, alpha=0.5)
# plt.plot(mag_sigclip, fit_func(mag_sigclip), color='red')
# plt.xlabel('MAG_AUTO')
# plt.ylabel('SNR_WIN')
# plt.title('SNR_WIN and MAG_AUTO Fit')
# plt.gca().invert_xaxis()
# plt.show()

# plt.scatter(mag_sigclip,snr_sigclip,  s=0.1, alpha=0.5)
# plt.xlabel('SNR_WIN')
# plt.ylabel('MAG_AUTO')
# plt.title('SNR_WIN and MAG_AUTO Fit')
# plt.gca().invert_xaxis()
# plt.show()