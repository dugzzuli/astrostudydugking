import numpy as np
from astropy.table import Table
from scipy.optimize import curve_fit
import matplotlib.pyplot as plt
from astropy.stats import sigma_clip
import numpy as np
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import PolynomialFeatures


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
snr_win = stars_table['SNR_WIN']
mag_auto_s = stars_table['MAG_AUTO_S']

plt.scatter(snr_win, mag_auto_s, s=1)




# 将数据转换成输入格式
snr_win = snr_win.reshape(-1, 1)
mag_auto_s = mag_auto_s.reshape(-1, 1)

# 定义多项式特征转换器
poly = PolynomialFeatures(degree=2)

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