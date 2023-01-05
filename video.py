import cv2
import numpy as np

# The following code is sloppy, unorganized, and was written while on pain medication for a serious injury.

'''
Plan:
1. Get frame from camera [x]
2. Get mask from frame [x]
3. Convert mask to ASCII [x]
     a. Convert to np array [x]
     b. For each pixel, find the closest pixel in pix (brightness) [x]
     c. Write that pixel to a new np array [x]
     d. Convert np array to frame [x]
     e. Display frame [x]
4. Display new frame [x]
'''

pix = "          .,-~:;=!*#$@"
# @#$*!=;:~-,.
# .,-~:;=!*#$@

normalize = 255/len(pix)
font = cv2.FONT_HERSHEY_SIMPLEX
font_size = 0.1

height, width = 700, 700
charx, chary = 120, 120

def get_mask(frame):  # returns a grayscale image of the specified resolution
    frame = cv2.resize(frame, (charx, chary))
    frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    return frame

def get_ascii(frame):  # returns the ascii version of the frame
    mask = get_mask(frame)

    to_display = np.zeros((height, width, 3), np.uint8)

    for x in range(charx):
        for y in range(chary):
            brightness = mask[x, y]
            index = int(brightness / normalize) - 1
            cv2.putText(to_display, pix[index], (int(
                y*(height/charx)), int(x*(height/chary))), font, font_size, (255, 255, 255), 1)

    return to_display

cap = cv2.VideoCapture(0)

if not cap.isOpened():
    print("Cannot open camera")
    exit()

while True:
    ret, frame = cap.read()

    if not ret:
        print("Can't receive frame.")
        break

    frame = get_ascii(frame)

    cv2.imshow('frame', frame)
    if cv2.waitKey(1) == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
