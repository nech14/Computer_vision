
import cv2
import time
import numpy as np

capture = cv2.VideoCapture(0)
capture.set(cv2.CAP_PROP_AUTO_EXPOSURE, -1)
capture.set(cv2.CAP_PROP_EXPOSURE, 0)

cv2.namedWindow("Camera")
cv2.namedWindow("Debug")



def detect_shape(contour):
    # Аппроксимация контура
    epsilon = 0.04 * cv2.arcLength(contour, True)
    approx = cv2.approxPolyDP(contour, epsilon, True)

    # Определение формы (квадрат или круг)
    shape = "Circle" if len(approx) > 4 else "Square"

    return shape


#frame = cv2.imread('im.jpg')
 

#cv2.drawContours(frame, contours, -1, (0, 255, 0), 2)


while True:

    frame = cv2.imread('1.png')
    denoised = cv2.fastNlMeansDenoisingColored(frame, None, 10, 10, 7, 21)

    frame = cv2.GaussianBlur(denoised, (21, 21), 0)
    hsv = cv2.cvtColor(denoised, cv2.COLOR_BGR2HSV)[:, :, 1]


    _, thresholded = cv2.threshold(hsv, 75, 245, cv2.THRESH_BINARY)


    contours, _ = cv2.findContours(thresholded, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)



    for contour in contours:
        shape = detect_shape(contour)
        cv2.drawContours(frame, [contour], 0, (0, 255, 0), 2)
        cv2.putText(frame, shape, (contour[0][0][0], contour[0][0][1]), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 0, 0), 2)
       
    
    cv2.imshow("Camera", thresholded)
    cv2.imshow("Debug", frame)
    
    if cv2.waitKey(1) == ord('q'):
        break

capture.release()
cv2.destroyAllWindows()

