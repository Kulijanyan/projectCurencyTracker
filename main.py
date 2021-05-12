from PyQt5 import QtWidgets
from ui import Ui_CurrencyTracker
from api import rate_getter


class ElementFunctions(QtWidgets.QMainWindow):
    def __init__(self):
        super(ElementFunctions, self).__init__()
        self.ui = Ui_CurrencyTracker()
        self.ui.setupUi(self)
        self.ui.exchange_value1.setPlaceholderText("0")
        self.ui.exchange_value2.setPlaceholderText("0")
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

        self.ui.exchange_button.clicked.connect(lambda: exchanger())

        def exchanger():
            if self.ui.base_value_2.currentText() == "---" or self.ui.base_value_3.currentText() == "---":
                self.ui.curr_error.exec_()
                self.ui.base_value_2.setCurrentIndex(1)
                self.ui.base_value_3.setCurrentIndex(2)
            else:
                curr_1 = self.ui.base_value_2.currentText()
                curr_2 = self.ui.base_value_3.currentText()

                first_val = self.ui.exchange_value1.text()
                second_val = self.ui.exchange_value2.text()

                if self.ui.exchange_value2.isModified():
                    if second_val.isnumeric():
                        res = float(second_val) / (rates[curr_2] / rates[curr_1])
                        res = str(round(res, 2))
                        self.ui.exchange_value1.setText(res)
                        self.ui.exchange_value1.setModified(False)
                        self.ui.exchange_value2.setModified(False)
                    else:
                        self.ui.value_error.exec_()
                elif self.ui.exchange_value1.isModified():
                    if first_val.isnumeric():
                        res = float(first_val) * (rates[curr_2] / rates[curr_1])
                        res = str(round(res, 2))
                        self.ui.exchange_value2.setText(res)
                        self.ui.exchange_value2.setModified(False)
                    else:
                        self.ui.value_error.exec_()


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    CurrencyTracker = QtWidgets.QMainWindow()
    ui = ElementFunctions()
    ui.show()
    sys.exit(app.exec_())
