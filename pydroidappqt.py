import locale
import mylocale
import sys
from qtpy import QtWidgets, QtCore

app = QtWidgets.QApplication(sys.argv)
window = QtWidgets.QMainWindow()
label = QtWidgets.QLabel("Hello, world!\n\nThis example can also run with other Qt libraries like PyQt6, PyQt5 and PySide2 using QtPy library.")
label.setAlignment(QtCore.Qt.AlignCenter)
label.setWordWrap(True)
window.setCentralWidget(label)
window.show()
sys.exit(app.exec())
