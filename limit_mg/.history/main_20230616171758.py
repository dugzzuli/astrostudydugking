from astropy.table import Table

# 打开星表FITS文件
stars_table = Table.read('mb_sc_tm15_u_20230602204159_239_sciimg_sexcat.fits',hdu=2)

stars_table[(stars_table["SNR_WIN"] > 4.5) & (stars_table["SNR_WIN"] < 5.5)]