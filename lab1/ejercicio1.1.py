#importar el modulo opencv
import cv2

#Leer una img-*
img = cv2.imread('img/lena.jpg')

#Mostrar img
cv2.imshow('Lena original',img)
cv2.waitKey(0)
cv2.destroyAllWindows()