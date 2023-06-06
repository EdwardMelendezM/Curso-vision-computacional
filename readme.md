# Instalaciones necesarias
1. Verificar nuestra version de python
```
python --version
```
2. Instalacion de numpy y open cv (Manejo de imagenes)
```
pip install numpy
pip install opencv-python
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

5. Desintalar una librerias
```
pip uninstall nombre_del_paquete
```

6. Buscar paquete
```
pip search numpy
```
7. Listar todas las librerias instaladas
```
pip list
```