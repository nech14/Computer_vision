
import numpy as np
import matplotlib.pyplot as plt
from skimage.measure import label, regionprops

x_buf = []
y_buf = []

for i in range(99):
    f = np.load(f"out/h_{i+1}.npy") 

    bin_f = label(f)

    regions = regionprops(bin_f)    
    sorted_regions = sorted(regions, key=lambda region: region.area)
    for region in sorted_regions:
        r = bin_f[region.bbox[0]:region.bbox[2], region.bbox[1]:region.bbox[3]]
        x = region.bbox[2] - region.bbox[0]
        y = region.bbox[3] - region.bbox[1]
        x_buf.append(region.bbox[1]+y//2)
        y_buf.append(region.bbox[0]+x//2)

plt.subplot(121)
plt.plot(x_buf, y_buf)
plt.subplot(122)
plt.plot(x_buf[::3], y_buf[::3])
plt.plot(x_buf[1::3], y_buf[1::3])
plt.plot(x_buf[2::3], y_buf[2::3])
plt.show()


