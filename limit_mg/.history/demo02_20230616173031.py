import numpy as np
from astropy.stats import sigma_clip
import matplotlib.pyplot as plt

# Generate some sample data
np.random.seed(123)
snr = np.random.normal(size=100)
mag = 10 - 2.5 * np.log10(np.abs(snr)) + np.random.normal(scale=0.1, size=100)

# Apply sigma clipping
snr_sigclip = sigma_clip(snr)
mag_sigclip = sigma_clip(mag)

# Fit quadratic functions to the clipped data
p_snr = np.polyfit(snr_sigclip, mag_sigclip, 2)


# Evaluate the fitted functions at some new values (e.g. x=0,1,2,...,len(snr_sigclip))
x_new = np.arange(len(snr_sigclip))
y_snr_fit = p_snr[0] * snr_sigclip**2 + p_snr[1] * x_new + p_snr[2]

# Plot the clipped data and fitted functions
plt.figure(figsize=(8, 6))
plt.scatter(range(len(snr_sigclip)), snr_sigclip, label='Clipped SNR')
plt.scatter(range(len(mag_sigclip)), mag_sigclip, label='Clipped Mag')
plt.plot(x_new, y_snr_fit, 'r-', label='Fitted SNR')

plt.legend()
plt.xlabel('Index')
plt.ylabel('Value')
plt.show()