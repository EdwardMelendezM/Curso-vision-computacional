import numpy as np

npArray = np.zeros((5,6),dtype=np.uint8)
npArray = np.ones((5,6),dtype=np.uint8)
print(npArray)

# b,g,r = cv2.split(img)
# imgNueva = cv2.merge(b,g,r)