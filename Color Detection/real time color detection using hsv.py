import cv2
import  numpy as np

cap = cv2.VideoCapture(0)

while True:
    _, frame = cap.read()

    hsv_frame  = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)


    # mask for red color
    low_red = np.array([161, 155, 84])
    high_red = np.array([179, 255, 255])
    red_mask = cv2.inRange(hsv_frame, low_red, high_red) # only define the red color
    red = cv2.bitwise_and(frame, frame, mask= red_mask)

    # mask for blue color
    low_blue = np.array([94, 80, 2])
    high_blue = np.array([126, 255, 255])
    blue_mask = cv2.inRange(hsv_frame, low_blue, high_blue)  # only define the blue color
    blue = cv2.bitwise_and(frame, frame, mask=blue_mask)

    # mask for green color
    low_green = np.array([25, 52, 72])
    high_green = np.array([102, 255, 255])
    green_mask = cv2.inRange(hsv_frame, low_green, high_green)  # only define the green color
    green  = cv2.bitwise_and(frame, frame, mask = green_mask)


    # every color except white
    low = np.array([0, 42, 0])
    high = np.array([179, 255, 255])
    _mask = cv2.inRange(hsv_frame, low, high)  # only define the red colo
    mask2 = cv2.bitwise_and(frame, frame, mask=_mask)

    cv2.imshow("Frame", frame)
    cv2.imshow("Red mask ", red)
    cv2.imshow("Blue mask ", blue)
    cv2.imshow("Green mask ", green)

    cv2.imshow("All the colors without white ", mask2)
    key = cv2.waitKey(1)
    if key == 27:
        break


'''
hue > means the color

saturation > quantity of color

value > brightness of color
'''
