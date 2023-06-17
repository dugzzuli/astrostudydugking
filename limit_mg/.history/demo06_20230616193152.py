from astropy.table import Table
from scipy.optimize import curve_fit
import numpy as np
import matplotlib.pyplot as plt
from astropy.stats import sigma_clip

# 打开星表FITS文件
stars_table = Table.read('mb_sc_tm15_u_20230602204159_239_sciimg_sexcat.fits', hdu=2)

# 从stars_table中提取SNR_WIN和MAG_AUTO
snr = stars_table[(stars_table['SNT_WIN']!=None) &(stars_table['FLAGS']==0) & (stars_table['SNR_WIN']>0)]['SNR_WIN']
mag = stars_table[(stars_table['SNT_WIN']!=None) &(stars_table['FLAGS']==0) & (stars_table['SNR_WIN']>0)]['MAG_AUTO_S']

snr_sigclip = sigma_clip(snr,maxiters=5)
mag_sigclip = sigma_clip(mag,maxiters=5)


from astropy.modeling import models, fitting
quadratic_model = models.Exponential1D(amplitude=2.0, tau=0.1)

# 定义拟合器
fitter = fitting.LevMarLSQFitter()

# 拟合模型
fit_result = fitter(quadratic_model, snr_sigclip, mag_sigclip)


# 绘制散点图和拟合曲线
plt.scatter(snr_sigclip,mag_sigclip,  s=0.1, alpha=0.5)
plt.ylabel('MAG_AUTO')
plt.xlabel('SNR_WIN')
plt.title('SNR_WIN and MAG_AUTO Fit')

x=np.sort(snr_sigclip)
plt.plot(x, fit_result(x), color='r')

plt.show()

print(fit_result([5]))

