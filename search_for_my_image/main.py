import cv2
import time
import matplotlib.pyplot as plt
import numpy as np


video_path = 'output.avi'


cap = cv2.VideoCapture(video_path)


if not cap.isOpened():
    print("Ошибка при открытии видеофайла.")
    exit()

counter = 0
frams_c = 0

while True:
    ret, frame = cap.read()

    if not ret:
        print("Видео закончилось или произошла ошибка при чтении.")
        break

    height, width, _ = frame.shape
    middle_strip = frame[:, width // 2 :width // 2 + 1, :]

    sl = height//3-height//3//2

    w = middle_strip[sl:sl+1, :, :]
    b = middle_strip[sl*3:sl*3+1, :, :]
    r = middle_strip[sl*5:sl*5+1, :, :]


    if np.array_equal(w,[[[255, 255, 255]]]) and np.array_equal(b, [[[202,  70,  62]]]) and np.array_equal(r, [[[36, 26, 236]]]):
        counter += 1
        print(counter)
    frams_c += 1
    

    
    
    
# Освобождаем ресурсы
cap.release()
cv2.destroyAllWindows()

print(f"My picture appears {counter} times out of {frams_c}")
