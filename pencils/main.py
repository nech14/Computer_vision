
import numpy as np
import cv2
import matplotlib.pyplot as plt
from skimage.measure import label, regionprops

for i in range(12):
    image = cv2.imread(f'images/{i+1}.jpg')

    image_gray = cv2.cvtColor(image, cv2.COLOR_RGB2GRAY)

    edges = cv2.Canny(image_gray, 30, 100)
    contours, _ = cv2.findContours(edges, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    clean_image = np.zeros_like(image_gray)
    cv2.drawContours(clean_image, contours, -1, (255, 255, 255), thickness=cv2.FILLED)
    kernel = np.ones((80, 80), np.uint8)
    dilated_image = cv2.dilate(clean_image, kernel, iterations=1)
    
    image_label = label(dilated_image)

    pencils=0
    regions = regionprops(image_label)
    for region in regions:
        r = image_label[region.bbox[0]:region.bbox[2], region.bbox[1]:region.bbox[3]]
        x = region.bbox[2] - region.bbox[0]
        y = region.bbox[3] - region.bbox[1]
        count_pixels = np.count_nonzero(image_label == region.label)
        if (15 >x/y > 10 or 0.05<x/y < 0.1 or (count_pixels/(x*y) > 0.06 and count_pixels/(x*y) < 0.3)):
            pencils += 1

    if pencils == 1:
        print(f"Image №{i+1} shows {pencils} pencil")
    else:
        print(f"Image №{i+1} shows {pencils} pencils")


    #plt.imshow(image)
    #plt.show()


