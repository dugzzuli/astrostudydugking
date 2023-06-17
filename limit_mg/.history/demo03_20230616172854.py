import numpy as np
import matplotlib.pyplot as plt
from astropy.stats import sigma_clip
from scipy.optimize import curve_fit

# Generate some sample data
np.random.seed(123)
snr = np.random.normal(size=100)
mag = 10 - 2.5 * np.log10(np.abs(snr)) + np.random.normal(scale=0.1, size=100)

# Apply sigma clipping
snr_sigclip = sigma_clip(snr)
mag_sigclip = sigma_clip(mag)

# Define a function to fit
def func(x, a, b):
    return a * np.log10(x) + b

# Fit the function to the clipped data using curve_fit
popt, pcov = curve_fit(func, snr_sigclip, mag_sigclip)

# Evaluate the fitted function at some new values (e.g. x=0.1,0.2,0.3,...,max(snr_sigclip))
x_new = np.linspace(0.1, max(snr_sigclip), 100)
y_fit = func(x_new, *popt)

# Plot the clipped data and fitted function
plt.figure(figsize=(8, 6))
plt.scatter(snr_sigclip, mag_sigclip, label='Clipped Data')
plt.plot(x_new, y_fit, 'r-', label='Fitted Function')
plt.legend()
plt.xlabel('SNR')
plt.ylabel('Magnitude')
plt.show()