import locale
from mylocale.TR import tr
import sys
from qtpy import QtWidgets, QtCore

app = QtWidgets.QApplication(sys.argv)
window = QtWidgets.QMainWindow()
label = QtWidgets.QLabel("")
label.setAlignment(QtCore.Qt.AlignCenter)
label.setWordWrap(True)
window.setCentralWidget(label)
lang_label = QtWidgets.QLabel("")
lang_label.setAlignment(QtCore.Qt.AlignCenter)
lang_label.setWordWrap(True)
window.setCentralWidget(lang_label)
window.show()
sys.exit(app.exec())
