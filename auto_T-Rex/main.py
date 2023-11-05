import pyautogui
import time
import mss.tools
from screeninfo import get_monitors
import matplotlib.pyplot as plt
import numpy as np
from skimage.measure import label
from PIL import Image
import cv2


def jump():
    pyautogui.hotkey("up")


def sit():
    pyautogui.keyDown("down")
    pyautogui.keyUp('down')


def get_screenshot(monitors, number_monitor):
    with mss.mss() as sct:
        monitor = {"top": 0, "left": 0, "width": monitors[2]['width'], "height": monitors[2]['height']}
        sct_img = sct.grab(monitor)

        return sct_img


def save_screenshot(image, name, _format='png'):  
    mss.tools.to_png(image.rgb, image.size, output=f'{name}.{_format}')


dino = {}


monitors = mss.mss().monitors

image = np.array(get_screenshot(monitors, 2))
image_binary = image.mean(2)
image_binary[image_binary == 249] = 0
image_binary[image_binary > 0] = 1
#image_binary = image_binary[456:521, 1505:1565]
#image_binary[image_binary > 200] = 0
#image_binary[image_binary > 0] = 1
image_label = label(image_binary)
#image_label[image_label != 1] = 0

#np.savetxt('dino.txt', image_label, fmt='%d', delimiter=' ')

plt.imshow(image_binary)
plt.show()

image_label = image_binary.astype(np.uint8)
#template_array = np.loadtxt('dino.txt', dtype=np.uint8)

template_array = plt.imread('dino.png')
template_array = template_array.mean(2)

template_array[template_array > 0.8] = 0
template_array[template_array > 0] = 1
template_array = template_array.astype(np.uint8)
result = cv2.matchTemplate(image_label, template_array, cv2.TM_CCOEFF_NORMED)

# пороговое значение для нахождения совпадений
threshold = 0.7


locations = np.where(result >= threshold)


conturs = []
for pt in zip(*locations[::-1]):
    conturs.append(pt)

pt = conturs[0]
plt.imshow(image[pt[1]:pt[1] + template_array.shape[0], pt[0]:pt[0] + template_array.shape[1]])
plt.show()
