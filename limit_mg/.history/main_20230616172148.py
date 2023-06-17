import numpy as np
from astropy.stats import sigma_clip
import matplotlib.pyplot as plt

# 从stars_table中提取SNR_WIN和MAG_AUTO
snr = stars_table['SNR_WIN']
mag = stars_table['MAG_AUTO']

# 对SNR_WIN和MAG_AUTO进行sigma clipping处理
snr_sigclip=sigma_clip(snr)
mag_sigclip=sigma_clip(mag)

# 进行二次函数拟合
fit_params = np.polyfit(mag_sigclip, snr_sigclip, 2)
fit_func = np.poly1d(fit_params)

# 绘制散点图和拟合曲线
plt.scatter(mag_sigclip, snr_sigclip, s=0.1, alpha=0.5)
plt.plot(mag_sigclip, fit_func(mag_sigclip), color='red')
plt.xlabel('MAG_AUTO')
plt.ylabel('SNR_WIN')
plt.title('SNR_WIN and MAG_AUTO Fit')
plt.gca().invert_xaxis()
plt.show()
