# Write your code here :-)
# Python program to shuffle a deck of card
# Editing simply to see if anything changes from the remote branch

# importing modules
import numpy as np
import argparse
import itertools, random
import os
#find_package(OpenCV)todoreview
import cv2 as cv

# construct the argument parse and parse the command line arguments from user
#CHANGED: adding parsing capability
ap = argparse.ArgumentParser()
ap.add_argument("-wh", "--workout_hearts", required=False, help="Workout that will appear when a heart is drawn")
ap.add_argument("-wd", "--workout_diamonds", required=False, help="Workout that will appear when a diamond is drawn")
ap.add_argument("-ws", "--workout_spades", required=False, help="Workout that will appear when a spade is drawn")
ap.add_argument("-wc", "--workout_clubs", required=False, help="Workout that will appear when a club is drawn")
args = vars(ap.parse_args())
#print(args)
#print(type(args["workout_hearts"]))


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

#CHANGED: Adjusted the indexing to start at 0 since Python and not Matlab
for i in range(0,len(deck)):
    #CHANGED: In order to call from the Workout Randomizer directory
    #CHANGED: Had to add '/' in front of 'PNG' to call the image
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
   
    #CHAED: Determine what workout should be printed
    #TODO: Determining if workouts have been entered
    test = None in args.values()
    if test == True:
        workout = str(i+1)
    else:
        if impath.endswith("H.png"):
            workout = args["workout_hearts"]
        elif impath.endswith("D.png"):
            workout = args["workout_diamonds"]
        elif impath.endswith("S.png"):
            workout = args["workout_spades"]
        elif impath.endswith("C.png"):
            workout = args["workout_clubs"]
    #CHANGED: altered text to be printed as "workout"
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
