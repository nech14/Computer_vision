import cv2
import time
import matplotlib.pyplot as plt
import numpy as np

# Путь к видеофайлу
video_path = 'output.avi'

# Открываем видеофайл
cap = cv2.VideoCapture(video_path)

# Проверка успешности открытия файла
if not cap.isOpened():
    print("Ошибка при открытии видеофайла.")
    exit()

counter = 0
frams_c = 0
# Покадрово считываем видео
while True:
    # Считываем кадр
    ret, frame = cap.read()

    # Проверка на конец видео
    if not ret:
        print("Видео закончилось или произошла ошибка при чтении.")
        break

    # Обработка кадра (ваш код обработки)

    # Вывод кадра
    height, width, _ = frame.shape
    middle_strip = frame[:, width // 2 :width // 2 + 1, :]

    sl = height//3-height//3//2

    w = middle_strip[sl:sl+1, :, :]
    b = middle_strip[sl*3:sl*3+1, :, :]
    r = middle_strip[sl*5:sl*5+1, :, :]
    
    #print(middle_strip.shape, sl)
    #print(w)
    #print(b)
    #print(r)

    if np.array_equal(w,[[[255, 255, 255]]]) and np.array_equal(b, [[[202,  70,  62]]]) and np.array_equal(r, [[[36, 26, 236]]]):
        counter += 1
        print(counter)
        #6time.sleep(0.3)
        #plt.imshow(frame)
        #plt.show()
    frams_c += 1
    
    #cv2.imshow('Video', frame)
    #cv2.imshow('shape', middle_strip)

    # Выход из цикла при нажатии клавиши 'q'
    #if cv2.waitKey(25) & 0xFF == ord('q'):
    #    break
    
    
    
# Освобождаем ресурсы
cap.release()
cv2.destroyAllWindows()

print(f"My picture appears {counter} times out of {frams_c}")
