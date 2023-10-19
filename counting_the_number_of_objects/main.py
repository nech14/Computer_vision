import numpy as np
import matplotlib.pyplot as plt
from scipy.ndimage import binary_dilation, binary_erosion, binary_opening, binary_closing
from skimage.measure import label

object0 = np.array([[0,0,0,0,0,0],
                    [0,0,0,0,0,0],
                    [1,1,1,1,1,1],
                    [1,1,1,1,1,1],
                    [1,1,1,1,1,1],
                    [1,1,1,1,1,1]])


object1 = np.array([[0,0,0,0,0,0],
                    [0,0,0,0,0,0],
                    [1,1,0,0,1,1],
                    [1,1,0,0,1,1],
                    [1,1,1,1,1,1],
                    [1,1,1,1,1,1]])


object2 = np.array([[0,0,0,0,0,0],
                    [0,0,0,0,0,0],
                    [1,1,1,1,1,1],
                    [1,1,1,1,1,1],
                    [1,1,0,0,1,1],
                    [1,1,0,0,1,1]])


object3 = np.array([[0,0,1,1,1,1],
                    [0,0,1,1,1,1],
                    [0,0,0,0,1,1],
                    [0,0,0,0,1,1],
                    [0,0,1,1,1,1],
                    [0,0,1,1,1,1]])


object4 = np.array([[0,0,1,1,1,1],
                    [0,0,1,1,1,1],
                    [0,0,1,1,0,0],
                    [0,0,1,1,0,0],
                    [0,0,1,1,1,1],
                    [0,0,1,1,1,1]])




objects = [object0, object1, object2, object3, object4]
object_symbols = ['▭','⊔','⊓','⊐','⊏']
img = np.load("ps.npy")
img = label(img)

print(f"Total number of objects: {np.max(img)}")

count = 0
c = 0
for i in range(len(objects)):
    count = np.max(label(binary_erosion(img, objects[i])))
    if i == 0:
        c = count
    elif i == 1 or i == 2:
        count -= c
    print(object_symbols[i] + ': ' + f"{count}")

#plt.imshow(img)


#plt.show()
