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

# 定义指数函数
def exponential_func(x, a, b, c):
    return a * np.exp(-b * x) + c

# 进行指数式拟合
popt, pcov = curve_fit(exponential_func, snr_sigclip, mag_sigclip)

# 绘制散点图和拟合曲线
plt.scatter(snr_sigclip,mag_sigclip,  s=0.1, alpha=0.5)
plt.ylabel('MAG_AUTO')
plt.xlabel('SNR_WIN')
plt.title('SNR_WIN and MAG_AUTO Fit')
plt.gca().invert_xaxis()

# 绘制拟合曲线
x = np.linspace(np.min(snr_sigclip), np.max(snr_sigclip), len(snr_sigclip))
y = exponential_func(x, *popt)
plt.plot(x, y, '-r')

plt.show()

