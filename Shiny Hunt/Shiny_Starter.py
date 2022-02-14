import keyboard
import time
import numpy as np
import cv2
import pyautogui
import telegram_send

# create functions that determin specific functions.
# nxbt controls needed Home = ], x Button = J, A button = L, up button =W
def Reset():
    #go back home
    keyboard.press('[')
    time.sleep(.05)
    keyboard.release('[')

    time.sleep(1)
    # check if home button was properly registered 
    image_difference = image_processing_reset()

    #Sometimes home button is not recognized on first push
    if image_difference>10000:
        keyboard.press('[')
        time.sleep(.1)
        keyboard.release('[')

    time.sleep(1)

    #close application
    keyboard.press('i')
    time.sleep(.1)
    keyboard.release('i')

    time.sleep(0.5)

    #confirm closing
    for i in range(0,5):
        time.sleep(.75)
        keyboard.press('l')
        time.sleep(.1)
        keyboard.release('l')

# function to start application
def start():
    #confirm starting game
    keyboard.press('l')
    time.sleep(.1)
    keyboard.release('l')

    time.sleep(.5)

    #confirm starting profile
    keyboard.press('l')
    time.sleep(.1)
    keyboard.release('l')

    time.sleep(25)

    # hardest part of the script repeat button inputs until pokemon select screen
    for i in range (0, 108):
        time.sleep(.2)
        keyboard.press('l')
        time.sleep(.1)
        keyboard.release('l')
        time.sleep(.2)

        keyboard.press('w')
        time.sleep(.1)
        keyboard.release('w')
     # should be at pokemon select screen

    time.sleep(2)
def Starter_select():
    ###
    #use this if selecting turtwig
    for i in range(0,2):
        time.sleep(.75)
        keyboard.press('l')
        time.sleep(.1)
        keyboard.release('l')

    time.sleep(.1)
    keyboard.press('l')
    time.sleep(.1)
    keyboard.release('l')
    ###
    #Use this if selecting Chimchar (d) or Piplup (a)
    
#     time.sleep(.75)
#     keyboard.press('l')
#     time.sleep(.1)
#     keyboard.release('l')
#     #change here for piplup or chimchar
#     time.sleep(.75)
#     keyboard.press('d')
#     time.sleep(.1)
#     keyboard.release('d')
#     
#     time.sleep(.75)
#     keyboard.press('l')
#     time.sleep(.1)
#     keyboard.release('l')

    ###
    time.sleep(1)
    image_difference = image_processing_select()

    #Sometimes home button is not recognized on first push
    if image_difference>100000:
        time.sleep(.1)
        keyboard.press('l')
        time.sleep(.1)
        keyboard.release('l')

    time.sleep(1.5)

    keyboard.press('w')
    time.sleep(.25)
    keyboard.release('w')

    time.sleep(0.1)

    keyboard.press('w')
    time.sleep(.25)
    keyboard.release('w')

    time.sleep(0.5)

    keyboard.press('l')
    time.sleep(.1)
    keyboard.release('l')

    time.sleep(0.5)

    keyboard.press('l')
    time.sleep(.1)
    keyboard.release('l')


#function to handle image capture
def image_processing():
    # take screenshot using pyautogui
    print("Checking...")
    image = pyautogui.screenshot()
    print("Done")
    # since the pyautogui takes as a
    # PIL(pillow) and in RGB we need to
    # convert it to numpy array and BGR
    # so we can write it to the disk

    image = cv2.cvtColor(np.array(image),
                         cv2.COLOR_RGB2BGR)
     #loads presaved foreground image of the battle button
    # writing it to the disk using opencv
    cv2.imwrite("screengrab.png", image)
    img_after = cv2.imread("screengrab.png")
    cv2.imwrite("screengrabsmaller.png", image[520:555, 1225:1350])
    d = cv2.absdiff(img_before[520:555, 1225:1350],img_after[520:555, 1225:1350])
    ret, thresh1 = cv2.threshold(d, 125, 255, cv2.THRESH_BINARY)
    cv2.imwrite("AbsDifference.png", thresh1)
    s =thresh1.sum()
    #print(s)
    return (s)

def image_processing_reset():
    # take screenshot using pyautogui
    img_before_reset = cv2.imread("Reset.png")
    image = pyautogui.screenshot()

    # since the pyautogui takes as a
    # PIL(pillow) and in RGB we need to
    # convert it to numpy array and BGR
    # so we can write it to the disk

    image = cv2.cvtColor(np.array(image),
                         cv2.COLOR_RGB2BGR)
     #loads presaved foreground image of the home screen
    # writing it to the disk using opencv
    cv2.imwrite("screengrabreset.png", image)
    img_after = cv2.imread("screengrabreset.png")
    cv2.imwrite("screengrabresetsmaller.png", image[520:555, 1225:1350])
    d = cv2.absdiff(img_before_reset[520:555, 1225:1350],img_after[520:555, 1225:1350])
    ret, thresh1 = cv2.threshold(d, 125, 255, cv2.THRESH_BINARY)
    cv2.imwrite("AbsDifferenceReset.png", thresh1)
    s =thresh1.sum()
    #print(s)
    return (s)

def image_processing_select():
    # take screenshot using pyautogui
    img_before_select = cv2.imread("Select.png")
    image = pyautogui.screenshot()

    # since the pyautogui takes as a
    # PIL(pillow) and in RGB we need to
    # convert it to numpy array and BGR
    # so we can write it to the disk

    image = cv2.cvtColor(np.array(image),
                         cv2.COLOR_RGB2BGR)
    #loads presaved foreground image of the pokemon select confirmation menu
    # writing it to the disk using opencv
    cv2.imwrite("screengrabselect.png", image)
    img_after = cv2.imread("screengrabselect.png")
    cv2.imwrite("screengrabselectsmaller.png", image[575:600, 1100:1275])
    d = cv2.absdiff(img_before_select[575:600, 1175:1225],img_after[575:600, 1175:1225])
    ret, thresh1 = cv2.threshold(d, 125, 255, cv2.THRESH_BINARY)
    cv2.imwrite("AbsDifferenceselect.png", thresh1)
    s =thresh1.sum()
    #print(s)
    return (s)

pyautogui.keyDown('alt')
pyautogui.press('tab')
pyautogui.keyUp('alt')

time.sleep(.2)

img_before = cv2.imread("screengrabOriginal.png")
time.sleep(2)
print('starting script')

# start script returning form home
Reset()
print('ENTERING Game')
# start script to try for shiny
start()
Starter_select()
#might need to vary this value depending on video delay
time.sleep(15.7)

image_difference = image_processing()

if image_difference < 50000:
    not_shiny =True
else:
    not_shiny = False
    print ('exiting script')

# this part will wait for an input to see if we redo the loop should use a while loop where one key press returns true and the other returns false and it waits indefinetely for keyboard press
while  not_shiny:
   #input = keyboard.read_key(suppress = True)
    #restart loop
    #if input== "x":
    #time.sleep(1)
    #print('repeating script')
    # start script returning form home
    Reset()

    # start script to try for shiny
    start()
    Starter_select()
    #might need to vary this value depending on video delay
    time.sleep(15.7)

    image_difference = image_processing()

    if image_difference < 50000:
        not_shiny =True
    else:
        print ('exiting script')
        not_shiny = False


#Send confirmation to telegram app to check if False positive or actual Shiny

telegram_send.send(messages=["Scripted Finished! Check if shiny."])
telegram_send.send(images =[open("screengrab.png","rb")] )
