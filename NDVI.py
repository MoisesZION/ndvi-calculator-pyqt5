import sys
from PyQt5 import uic
from PyQt5.QtWidgets import QMessageBox

# Lee el archivo gráfico que se hizo en Qt Designer (NDVI.ui).
# uic.loadUiType() lee el file y crea dos clases ; en donde se tiene el setup de widgets y ventana
DialogUi, DialogType = uic.loadUiType("NDVI.ui")


class NDVI(DialogType, DialogUi):
    """Calculadora puntual de NDVI (Normalized Difference Vegetation Index).

    Hereda de DialogType (QDialog) y de DialogUi (la interfaz generada
    a partir de NDVI.ui), siguiendo la misma filosofía que ConvLongArc.
    """

    def __init__(self):
        """Constructor de la clase.

        1) Llama al constructor de la clase padre (QDialog).
        2) Construye la interfaz gráfica con setupUi(self), lo que crea
           todos los objetos definidos en NDVI.ui (txtRed, txtNir, etc.)
           como atributos de self.
        3) Conecta cada botón de la interfaz con su método correspondiente.
        """
        super().__init__()
        self.setupUi(self)

        self.btnCalcular.clicked.connect(self.btnCalcular_clicked)
        self.btnLimpiar.clicked.connect(self.btnLimpiar_clicked)
        self.btnSalir.clicked.connect(self.btnSalir_clicked)

    def btnCalcular_clicked(self):
        """Valida los datos ingresados, calcula el NDVI y muestra
        el resultado junto con su interpretación.

        Fórmula:
            NDVI = (NIR - RED) / (NIR + RED)
        """

        # --- 1. Verificar que los campos no estén vacíos -----------------
        strRed = self.txtRed.text().strip()
        strNir = self.txtNir.text().strip()

        if strRed == "":
            QMessageBox.warning(self, "Dato faltante",
                                 "Por favor, ingrese un valor RED.")
            return

        if strNir == "":
            QMessageBox.warning(self, "Dato faltante",
                                 "Por favor, ingrese un valor NIR.")
            return

        # --- 2. Verificar que los valores sean numéricos ------------------
        try:
            fltRed = float(strRed)
            fltNir = float(strNir)
        except ValueError:
            QMessageBox.warning(self, "Valor no numérico",
                                 "Los valores deben ser numéricos.")
            return

        # --- 3. Verificar que RED y NIR estén en el rango 0 - 255 --------
        if not (0 <= fltRed <= 255):
            QMessageBox.warning(self, "Valor fuera de rango",
                                 "El valor RED debe estar entre 0 y 255.")
            return

        if not (0 <= fltNir <= 255):
            QMessageBox.warning(self, "Valor fuera de rango",
                                 "El valor NIR debe estar entre 0 y 255.")
            return

        # --- 4. Evitar división entre cero --------------------------------
        if (fltNir + fltRed) == 0:
            QMessageBox.warning(self, "Cálculo no posible",
                                 "No es posible calcular el NDVI cuando "
                                 "RED y NIR son 0.")
            return

        # --- 5. Calcular el NDVI -------------------------------------------
        fltNdvi = (fltNir - fltRed) / (fltNir + fltRed)

        # --- 6. Mostrar el resultado con dos decimales ----------------------
        self.txtNdvi.setText(f"{fltNdvi:.2f}")

        # --- 7. Mostrar la interpretación del resultado ---------------------
        strInterpretacion = self.clasificarNdvi(fltNdvi)
        self.txtInterpretacion.setPlainText(strInterpretacion)

    def clasificarNdvi(self, fltNdvi):
        """Recibe un valor de NDVI (float) y devuelve el texto de
        interpretación correspondiente, según la tabla de clasificación:

            < 0          -> Agua, suelo desnudo, construcciones, etc.
            0.00 - 0.20  -> Vegetación escasa o muy débil.
            0.21 - 0.50  -> Vegetación moderada.
            0.51 - 0.80  -> Vegetación densa.
            0.81 - 1.00  -> Vegetación muy densa y vigorosa.
        """
        if fltNdvi < 0:
            return ("Agua, suelo desnudo, construcciones u otras "
                     "superficies no vegetadas.")
        elif 0.00 <= fltNdvi <= 0.20:
            return "Vegetación escasa o muy débil."
        elif 0.21 <= fltNdvi <= 0.50:
            return "Vegetación moderada."
        elif 0.51 <= fltNdvi <= 0.80:
            return "Vegetación densa."
        else:  # 0.81 - 1.00
            return "Vegetación muy densa y vigorosa."

    def btnLimpiar_clicked(self):
        """Limpia los campos de entrada y de resultado."""
        self.txtRed.clear()
        self.txtNir.clear()
        self.txtNdvi.clear()
        self.txtInterpretacion.clear()

    def btnSalir_clicked(self):
        """Cierra la aplicación."""
        sys.exit()