from astropy.table import Table
from scipy.optimize import curve_fit
import numpy as np
import matplotlib.pyplot as plt
from astropy.stats import sigma_clip

# 打开星表FITS文件
stars_table = Table.read('mb_sc_tm15_u_20230602204159_239_sciimg_sexcat.fits', hdu=2)

# 从stars_table中提取SNR_WIN和MAG_AUTO
snr = stars_table['SNR_WIN']
mag = stars_table['MAG_AUTO']

snr_sigclip = sigma_clip(snr)
mag_sigclip = sigma_clip(mag)

# 定义二次函数
def quadratic_func(x, a, b, c):
    return a*x**2 + b*x + c

# 进行二项式拟合
popt, pcov = curve_fit(quadratic_func, mag_sigclip, snr_sigclip)

# 绘制散点图和拟合曲线
plt.scatter(mag_sigclip, snr_sigclip, s=0.1, alpha=0.5)
plt.xlabel('MAG_AUTO')
plt.ylabel('SNR_WIN')
plt.title('SNR_WIN and MAG_AUTO Fit')
plt.gca().invert_xaxis()

# 绘制拟合曲线
# x = np.linspace(np.min(mag_sigclip), np.max(mag_sigclip), 1000)
y = quadratic_func(mag_sigclip, *popt)
plt.plot(x, y, '-r')

plt.show()