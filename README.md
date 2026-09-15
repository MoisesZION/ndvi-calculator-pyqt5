# NDVI Calculator (PyQt5)

Aplicación de escritorio en Python, construida con **PyQt5** y **Qt Designer**, para calcular el **NDVI (Normalized Difference Vegetation Index)** a partir de valores puntuales de reflectancia de las bandas RED e NIR de una imagen.

## ¿Qué hace?

A partir de dos valores de entrada (RED y NIR, en el rango 0–255), la aplicación calcula:

```
NDVI = (NIR - RED) / (NIR + RED)
```

y muestra tanto el resultado numérico (con dos decimales) como una interpretación en lenguaje sencillo de qué tipo de cobertura sugiere ese valor:

| Rango       | Interpretación                                                        |
| ----------- | ---------------------------------------------------------------------- |
| < 0         | Agua, suelo desnudo, construcciones u otras superficies no vegetadas   |
| 0.00 – 0.20 | Vegetación escasa o muy débil                                          |
| 0.21 – 0.50 | Vegetación moderada                                                    |
| 0.51 – 0.80 | Vegetación densa                                                       |
| 0.81 – 1.00 | Vegetación muy densa y vigorosa                                        |

La aplicación valida que los campos no estén vacíos, que los valores sean numéricos, que estén en el rango 0–255, y evita la división entre cero, mostrando siempre mensajes de error claros mediante `QMessageBox` (sin cerrar la app ni mostrar tracebacks).

## Estructura del proyecto

```
.
├── NDVI.py          # Lógica de la aplicación: clase NDVI, cálculo, validaciones
├── main_ndvi.py      # Módulo ejecutable: arranca la QApplication y muestra la ventana
├── NDVI.ui           # Interfaz gráfica construida en Qt Designer
└── README.md
```

## Requisitos

- Python 3.8 o superior
- PyQt5

## Instalación

```bash
git clone https://github.com/<tu-usuario>/ndvi-calculator-pyqt5.git
cd ndvi-calculator-pyqt5
pip install PyQt5
```

## Uso

Ejecuta el módulo principal desde la carpeta del proyecto (los tres archivos deben estar juntos, ya que `NDVI.py` carga `NDVI.ui` con una ruta relativa):

```bash
python main_ndvi.py
```

En Windows, si el comando `python` no está disponible, usa el lanzador:

```powershell
py main_ndvi.py
```

## Ejemplo

```
RED = 50
NIR = 150

NDVI = (150 - 50) / (150 + 50) = 0.50   → Vegetación moderada
```

## Objetos de la interfaz (Qt Designer)

Para mantener consistencia entre `NDVI.ui` y `NDVI.py`, se usan estos `objectName`:

| objectName           | Tipo de widget            |
| --------------------- | -------------------------- |
| `txtRed`              | QLineEdit                  |
| `txtNir`               | QLineEdit                  |
| `txtNdvi`              | QLineEdit (solo lectura)   |
| `txtInterpretacion`    | QTextEdit (solo lectura)   |
| `btnCalcular`          | QPushButton                |
| `btnLimpiar`           | QPushButton                |
| `btnSalir`             | QPushButton                |

## Licencia

Este proyecto se distribuye con fines académicos/educativos.
