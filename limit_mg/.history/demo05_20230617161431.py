from astropy.table import Table
from scipy.optimize import curve_fit
import numpy as np
import matplotlib.pyplot as plt
from astropy.stats import sigma_clip

# 打开星表FITS文件
stars_table = Table.read('mb_sc_tm15_u_20230602204159_239_sciimg_sexcat.fits', hdu=2)

# 从stars_table中提取SNR_WIN和MAG_AUTO
stars_table.sort("SNR_WIN")

# 从stars_table中提取SNR_WIN
snr = stars_table['SNR_WIN']
# 对SNR_WIN进行3sigma clipping处理并获取掩码
sigclip_mask = sigma_clip(snr, sigma=3, maxiters=1).mask
# stars_table=stars_table[(stars_table['FLAGS']==0) & (stars_table['SNR_WIN']>0) & ~sigclip_mask & (stars_table['SNR_WIN']<800)]
stars_table=stars_table[(stars_table['FLAGS']==0) & (stars_table['SNR_WIN']>0) & ~sigclip_mask & (stars_table['SNR_WIN']<800)]
snr_sigclip = stars_table['SNR_WIN']
mag_sigclip = stars_table['MAG_AUTO_S']



def magsnr(snr,a0,a1,a2,a3,a4):
    return a0+(a1*snr**a2)+a3*snr


# 定义指数函数
def exponential_func(x, a, b, c):
    return a * np.exp(-b * x) + c

# 进行指数式拟合
popt, pcov = curve_fit(magsnr, snr_sigclip, mag_sigclip,maxfev=10000)

# 绘制散点图和拟合曲线
plt.scatter(snr_sigclip,mag_sigclip,  s=0.1, alpha=0.5)
plt.ylabel('MAG_AUTO')
plt.xlabel('SNR_WIN')
plt.title('SNR_WIN and MAG_AUTO Fit')


# 绘制拟合曲线
x = np.sort(snr_sigclip)
y = magsnr(x, *popt)
plt.plot(x, y, '-r')

plt.show()

print(magsnr(5, *popt))

