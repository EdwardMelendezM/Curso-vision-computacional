import cv2
img = cv2.imread('img/marsrover.png')

(b,g,r) = img[0,0]
print("valores de r,g,b",format((b,g,r)))

img[0:100,0:50] = (255,255,255)

cv2.imshow('imagen modificada',img)
cv2.waitKey(0)