import numpy as np
import cv2
import pyautogui

#Code to take screenshot images to save as foregroun and to isolate places to check
image = pyautogui.screenshot()

# since the pyautogui takes as a
# PIL(pillow) and in RGB we need to
# convert it to numpy array and BGR
# so we can write it to the disk
image = cv2.cvtColor(np.array(image),
                     cv2.COLOR_RGB2BGR)

# writing it to the disk using opencv
cv2.imwrite("Reset.png", image)
# testing different pixels range to check if correct part is isolated
cv2.imwrite("screengrabresetsmaller.png", image[520:555, 1225:1350])


