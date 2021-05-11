from PyQt5 import QtWidgets
from ui import Ui_CurrencyTracker
from api import rate_getter


class ElementFunctions(QtWidgets.QMainWindow):
    def __init__(self):
        super(ElementFunctions, self).__init__()
        self.ui = Ui_CurrencyTracker()
        self.ui.setupUi(self)
        self.functions()

    def functions(self):
        rates = rate_getter()
        self.ui.base_value.currentIndexChanged.connect(lambda: base_value_rates(self.ui.base_value.currentText()))

        def base_value_rates(value):
            if value == "EUR":
                self.ui.eur_valuetxt.setText(str(round(rates["EUR"], 2)))
                self.ui.usd_valuetxt.setText(str(round(rates["USD"], 2)))
                self.ui.rub_valuetxt.setText(str(round(rates["RUB"], 2)))
                self.ui.amd_valuetxt.setText(str(round(rates["AMD"], 2)))
            elif value == "USD":
                self.ui.eur_valuetxt.setText(str(round(1 / rates["USD"], 2)))
                self.ui.usd_valuetxt.setText(str(1))
                self.ui.rub_valuetxt.setText(str(round(rates["RUB"] / rates["USD"], 2)))
                self.ui.amd_valuetxt.setText(str(round(rates["AMD"] / rates["USD"], 2)))
            elif value == "RUB":
                self.ui.eur_valuetxt.setText(str(round(rates["EUR"] / rates["RUB"], 4)))
                self.ui.usd_valuetxt.setText(str(round(rates["USD"] / rates["RUB"], 4)))
                self.ui.rub_valuetxt.setText(str(1))
                self.ui.amd_valuetxt.setText(str(round(rates["AMD"] / rates["RUB"], 2)))

        # def exchanger():
        #     print(self.ui.exchange_value1.toPlainText())
        #
        # exchanger()


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    CurrencyTracker = QtWidgets.QMainWindow()
    ui = ElementFunctions()
    ui.show()
    sys.exit(app.exec_())
