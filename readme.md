# Instalaciones necesarias
Antes de todas las instalaciones necesitamos que instales python y visual studio
```
https://www.python.org/downloads/
https://code.visualstudio.com/download
```
1. Verificar nuestra version de python
```
python --version  |  py --version
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

print("Version de numpy",np.__version__)
print("Version de openCv",cv2.__version__)
print("Version de matplotlib",matplotlib.__version__)
```

5. Desintalar una librerias
```
pip uninstall nombre_del_paquete
```


6. Listar todas las librerias instaladas
```
pip list
```

7. Guardar la lista de librerias
```
pip list > test/bibliotecas_instaladas.txt
```
