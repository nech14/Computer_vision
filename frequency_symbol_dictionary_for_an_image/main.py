import matplotlib.pyplot as plt
import numpy as np
from skimage.measure import label, regionprops


def filling_factor(region):
    return region.image.mean()


def recognize(region):
    if filling_factor(region) == 1:
        return '-'
    else:
        match(region.euler_number):
            case -1: #B or 8
                #if ''.join(map(str, [1.,1.])) in ''.join(map(str, region.image.mean(0))):
                #    return 'B'
                if 1 in region.image.mean(0)[:2]:
                    return 'B'
                return '8'
            
            case 0: #A || 0 || P || D
                buf_region_image = region.image.copy()
                
                if 1 in region.image.mean(0)[:2]:
                    buf_region_image[-1, :] = 1
                    buf_region_image[:, -len(buf_region_image[0])//2:] = 1
                    buf_labeled = label(buf_region_image)
                    buf_regions = regionprops(buf_labeled)
                    euler = buf_regions[0].euler_number
                    if euler == 0:
                        return 'D'
                    elif euler == -1:
                        return 'P'
                
                buf_region_image[-1, :] = 1
                buf_labeled = label(buf_region_image)
                buf_regions = regionprops(buf_labeled)
                if 1 in region.image.mean(1):
                    return '*'
                if buf_regions[0].euler_number == -1:
                    return 'A'
                
                return '0'
            
            case 1: #1 || W || X || * || /
                if ''.join(map(str, [1.,1.])) in ''.join(map(str, region.image.mean(0))):
                    return '1'
                #if 1 in region.image.mean(0):
                    #return '1'
                buf_region_image = region.image.copy()
                buf_region_image[[0,-1], :] = 1
                buf_labeled = label(buf_region_image)
                buf_regions = regionprops(buf_labeled)
                euler = buf_regions[0].euler_number
                if euler == -1:
                    return 'X'
                elif euler == -2:
                    return 'W'
                elif region.eccentricity > 0.5:
                    return '/'
                return '*'
            
            case _:
                return '?'



image = plt.imread("symbols.png")

image_binary = image.mean(2)
image_binary[image_binary>0] = 1

image_bl = label(image_binary)

regions = regionprops(image_bl)

#96 - W
#77 - 0
#48 - B
#17 - -
#14 - 8
#8 - P
#6 - A
#4 - 1
#3 - *
#2 - /
#1 = X
#0 - D


symbols = {}
for region in regions:
    symbol = recognize(region)
    if symbol not in symbols:
        symbols[symbol] = 0
    symbols[symbol] += 1

    
print(f'count: {image_bl.max()}')
print(symbols)
print(f'coverage: {(image_bl.max()-symbols.get("?", 0))/image_bl.max()}')
