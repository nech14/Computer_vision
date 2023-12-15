import pyautogui
import time
import mss
import mss.tools
import matplotlib.pyplot as plt
import numpy as np
from skimage.measure import label
import cv2
import keyboard as kb


def jump():
    pyautogui.hotkey("up")

def refactorJump():
    kb.press("up")


def sit():
    pyautogui.keyDown("down")
    pyautogui.keyUp('down')


def refactorSit(t):
    kb.press('down')
    time.sleep(t)
    kb.release('down')




def get_screenshot(monitors, number_monitor):
    with mss.mss() as sct:
        monitor = {"top": 0, "left": 0, "width": monitors[number_monitor]['width'], "height": monitors[number_monitor]['height']}
        sct_img = sct.grab(monitor)

        return sct_img


def get_screenshot_box(t, l, w, h):
    with mss.mss() as sct:
        box = {"top": t, "left": l, "width": w, "height": h}
        sct_img = sct.grab(box)

        return sct_img

def save_screenshot(image, name, _format='png'):  
    mss.tools.to_png(image.rgb, image.size, output=f'{name}.{_format}')


dino = {}


monitors = mss.mss().monitors

image = np.array(get_screenshot(monitors, 0))
image_binary = image.mean(2)
image_binary[image_binary == 249] = 0
image_binary[image_binary > 0] = 1
image_label = label(image_binary)


image_label = image_binary.astype(np.uint8)

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


start_image = image_label[pt[1]:pt[1]+template_array.shape[0]-15, pt[0]+template_array.shape[1]+10:pt[0]+template_array.shape[0]*3]

print('gggg')


refactorJump()

start_time  = time.time()
coef = 0.033 #0.3
jump_time = 0.14
sit_time = 0.25
time_see = 0 #0.016

buf_n = 0
buf_time = [15,    30,   40,   65,  90, 110]
buf_coef = [0.038, 0.07,  0.19, 0.35,  0.48, 0.5]
buf_jump = [0.146, 0.14,  0.13, 0.118, 0.115, 0.097]
while True:
    tim = time.time() - start_time
    if buf_n < len(buf_time) and tim > buf_time[buf_n]:
        coef = buf_coef[buf_n]
        jump_time = buf_jump[buf_n]
        print("new time jump")
        buf_n += 1

    # if t >= 15:
    #     coef = 4.7
    #     jump_time = 0.2
    # elif t >= 20:
    #     coef = 4.7
    #     jump_time = 0.18


    t = pt[1]+5
    l = pt[0]+120
    h = int(template_array.shape[0]-40)
    w = int(template_array.shape[0] * coef)

    image = np.array(get_screenshot_box(t, l, w, h))
    image_binary = image.mean(2)

    image_binary[image_binary == 249] = 0
    image_binary[image_binary > 0] = 1

    start_image = image_binary.astype(np.uint8)


    if start_image.sum() > 4:
        #print('jump', start_image.sum(), t, coef)

        if start_image[start_image.shape[0]//2:, :].sum() > 0:

            time.sleep(time_see)

            refactorJump()
            time.sleep(jump_time)
            refactorSit(0.005)
        else:
            refactorSit(sit_time)

        # if tim > 45:
        #     plt.imshow(start_image)
        #     plt.show()
        #action.append(['j', 6])
    else:
        time.sleep(0.0001)



