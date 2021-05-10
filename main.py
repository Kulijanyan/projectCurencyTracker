from PyQt5 import QtWidgets
from ui import Ui_CurrencyTracker


class ElementFunctions(Ui_CurrencyTracker):
    def text_writer(self):
        self.usd_valuetxt.setText("ABOBA")


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    CurrencyTracker = QtWidgets.QMainWindow()
    ui = Ui_CurrencyTracker()
    ui.setupUi(CurrencyTracker)
    functions = ElementFunctions()
    functions.text_writer()
    CurrencyTracker.show()
    sys.exit(app.exec_())