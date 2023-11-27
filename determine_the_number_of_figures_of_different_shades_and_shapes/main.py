
import numpy as np
import cv2
import matplotlib.pyplot as plt
from skimage.measure import label, regionprops


image = cv2.imread('balls_and_rects.png')
hsv = cv2.cvtColor(image, cv2.COLOR_RGB2HSV)

binary = image.mean(2) > 0

labeled = label(binary)

regions = regionprops(labeled)
colors = []
h = hsv[:, :, 0]

circles = 0
circles_colors = []
rectangles = 0
rectangles_colors = []

for region in regions:
    r = h[region.bbox[0]:region.bbox[2], region.bbox[1]:region.bbox[3]]
    if np.all(r[0][0] != [0, 0, 0]):
        rectangles += 1
        rectangles_colors.extend(np.unique(r[0]))
    else:
        circles += 1        
        circles_colors.extend(np.unique(r[0])[1:])
    colors.extend(np.unique(r[0]))

colors = np.unique(colors)[1:]

print(f"Count figures: {labeled.max()}")   
print(f"Total colors in the picture {len(np.unique(colors))}")
print(f"\nNumber of circles: {circles}")
print(f"The circles have {len(np.unique(circles_colors))} colors.")
print(f"Number of rectangles: {rectangles}")
print(f"The rectangles have {len(np.unique(rectangles_colors)[1:])} colors.")


#plt.imshow(hsv)
#plt.show()
