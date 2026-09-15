import sys
from PyQt5 import QtWidgets
from NDVI import NDVI

app = QtWidgets.QApplication(sys.argv)
MyApp = NDVI()
MyApp.show()
sys.exit(app.exec_())