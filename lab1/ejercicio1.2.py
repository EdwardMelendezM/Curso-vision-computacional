import cv2
img = cv2.imread('img/marsrover.png')

print("Dimensiones, ",img.ndim)
print("Canales, ", format(img.shape[2]))
print("Propiedaes, ", img.shape)
print("Tamaño de la imagen",img.size)