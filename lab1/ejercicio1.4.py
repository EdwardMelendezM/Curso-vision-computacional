import cv2
img = cv2.imread('img/marsrover.png')

puntoInicial = (90,60)
puntoFinal = (350,380)

color = (255,0,0)
grosor = 10


cv2.rectangle(img,puntoInicial,puntoFinal,color,grosor)
cv2.imwrite('reactangle.jpg',img)

cv2.imshow('img nuevo',img)
cv2.waitKey(0)