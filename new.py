from PyQt5.QtWidgets import QApplication, QMainWindow, QAction, QToolBar
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import QSize
from sys import argv


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.GUI()

    def GUI(self):
        self.setWindowTitle("test")
        #self.setFixedSize(640, 480)

        self.toolbar = QToolBar("hello")
        self.toolbar.setFixedSize(640, 64)
        self.addToolBar(self.toolbar)
        self.toolbar.setMovable(False)
        self.toolbar.setIconSize(QSize(64, 64))

        self.newtool = QAction(QIcon("github.png"), "button", self)
        self.toolbar.addAction(self.newtool)

        # self.setStyleSheet(
        #    """
        #    QMainWindow {
        #        background: #eee;
        #    }


#
#    QToolBar {
#        background: #eee;
#        padding: 0px;
#        border: 0px;
#    }
#
#    QToolBar::item {
#        background: #59f;   # It don't work
#        padding: 10px;   # It don't work
#    }
#
#    """
# )


if __name__ == "__main__":
    app = QApplication(argv)
    window = MainWindow()
    window.show()
    app.exec_()
