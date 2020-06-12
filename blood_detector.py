import cv2

PATH_TO_IMAGE = "blood-demo.jpg"

img = cv2.imread(PATH_TO_IMAGE)
hsv = cv2.cvtColor(img, cv2.COLOR_RGB2HSV)
# RGB
# BGR
lower_red = (0, 0, 150)
upper_red = (90, 90, 255)

mask = cv2.inRange(img, lower_red, upper_red)
print(hsv[60,91])

cv2.imshow("Image", mask)
cv2.waitKey()