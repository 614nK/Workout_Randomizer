# Write your code here :-)
# Python program to shuffle a deck of card

# importing modules
import argparse
import itertools, random
import os
#find_package(OpenCV)todoreview
import cv2 as cv

#CHANGED: Added tinker since it allows for some different dialog box options
import tkinter as tk
from tkinter import simpledialog

#CHANGED: Switched the input method from terminal parsing to popup window input requests
application_window = tk.Tk()
w1 = simpledialog.askstring("Input", "What is your first workout?", parent = application_window)
w2 = simpledialog.askstring("Input", "What is your second workout?", parent = application_window)
w3 = simpledialog.askstring("Input", "Third workout?", parent = application_window)
w4 = simpledialog.askstring("Input", "Fourth", parent = application_window)

# make a deck of cards
value = list(map(str,range(2,11)))
face = ['J','Q','K','A']
value.extend(face)
suit = ['S','H','D','C']
deck = list(itertools.product(value,suit))

# shuffle the cards
random.shuffle(deck)

dirpath = os.path.dirname(__file__)
print(dirpath)

for i in range(0,len(deck)):
    impath = dirpath+str('/PNG/')+deck[i][0]+deck[i][1]+str('.png')
    print(impath) 
    img = cv.imread(impath,1)

    # Window name in which image is displayed 
    window_name = 'Image'
  
    # font 
    font = cv.FONT_HERSHEY_SIMPLEX 
  
    # org 
    #CHANGED: updated origin point 
    org = (150, 80) 
  
    # fontScale
    #CHANGED: updated scale for ease of viewing 
    fontScale = 3
   
    # Blue color in BGR 
    #CHANGED: changed color to HEX value #28572a in BGR
    color = (122, 82, 40) 
  
    # Line thickness of 2 px
    #CHANGED: Altered again for ease of reading
    thickness = 5

    #CHANGED: changed the displayed name to match the input from the dialog windows or just blank for now. There could be a more compact way of making this but I just wanted something quick
    if impath.endswith("H.png"):
        if w1 == []:
            workout = ''
        else:
            workout = w1
    elif impath.endswith("D.png"):
        if w2 == []:
            workout = ''
        else:
            workout = w2
    elif impath.endswith("S.png"):
        if w3 == []:
            workout = ''
        else:
            workout = w3
    elif impath.endswith("C.png"):
        if w4 == []:
            workout = ''
        else:
            workout = w4
    # Using cv2.putText() method 
    image = cv.putText(img, workout, org, font,  
                   fontScale, color, thickness, cv.LINE_AA) 
   
    # Displaying the image 
    cv.imshow(window_name, img)
    cv.waitKey(0)

cv.destroyAllWindows()

# draw five cards
#print("You got:")
#for i in range(5):
#   print(deck[i][0], "of", deck[i][1])
