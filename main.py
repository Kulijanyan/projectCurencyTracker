from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow
import sys


def application():
    app = QApplication(sys.argv)
    window = QMainWindow()

    window.setWindowTitle("Currency Tracker")
    window.setGeometry(200, 200, 800, 600)

    title_text = QtWidgets.QLabel(window)
    title_text.setText("Currency Tracker (v 0.1)")
    title_text.move(100, 100)
    title_text.adjustSize()

    window.show()
    sys.exit(app.exec_())


if __name__ == "__main__":
    application()
