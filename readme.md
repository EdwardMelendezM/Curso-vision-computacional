# Instalaciones necesarias
1. Verificar nuestra version de python
```
python --version
```
2. Instalacion de numpy y open cv (Manejo de imagenes)
```
pip install opencv-python
pip install numpy
```
3. Instalacion de matplotlib (Graficos)
```
pip install matplotlib
```

4. Comprobar si se instalo correctamente
```
import matplotlib
import cv2
import numpy as np

print(np.__version__)
print(cv2.__version__)
print(matplotlib.__version__)
```

5. Desintalar un paquete
```
pip uninstall nombre_del_paquete
```