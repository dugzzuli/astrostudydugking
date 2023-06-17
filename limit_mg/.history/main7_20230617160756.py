import numpy as np
from astropy.table import Table
from scipy.optimize import curve_fit
import matplotlib.pyplot as plt
from astropy.stats import sigma_clip
# 读取fits文件数据
tab_hdu = Table.read('mb_sc_tm15_u_20230602204159_239_sciimg_sexcat.fits', hdu=2)

tab_hdu = tab_hdu[np.argsort(tab_hdu['SNR_WIN'])]

# 获取SNR_WIN和MAG_AUTO_S列的值
# snr_win = tab_hdu[(tab_hdu['SNR_WIN']>0) & (tab_hdu['SNR_WIN']<500)]['SNR_WIN']
# mag_auto_s = tab_hdu[(tab_hdu['SNR_WIN']>0) & (tab_hdu['SNR_WIN']<500)]['MAG_AUTO_S']

tab_hdu=tab_hdu[(tab_hdu['SNR_WIN']>0) & (tab_hdu['FLAGS']==0) & (tab_hdu['SNR_WIN']!=np.nan)]

# 获取SNR_WIN和MAG_AUTO_S列的值
snr_win = sigma_clip(snr_win)
mag_auto_s = sigma_clip(mag_auto_s)

plt.scatter(snr_win, mag_auto_s, s=1)

import numpy as np
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import PolynomialFeatures


# 将数据转换成输入格式
snr_win = snr_win.reshape(-1, 1)
mag_auto_s = mag_auto_s.reshape(-1, 1)

# 定义多项式特征转换器
poly = PolynomialFeatures(degree=5)

# 转换输入数据
X_poly = poly.fit_transform(snr_win)

# 定义线性回归模型
model = LinearRegression()

# 训练模型
model.fit(X_poly, mag_auto_s)


x_new = np.sort(snr_win)
plt.plot(x_new, model.predict(poly.fit_transform(x_new)), 'r')

plt.xlabel('SNR_WIN')
plt.ylabel('MAG_AUTO_S')
plt.show()


plt.savefig("2.png")

# 输出拟合结果
print(model.predict(poly.fit_transform([[5]])))