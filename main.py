import sys
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import QIcon
from currency_converter import CurrencyConverter
from ui import Ui_MainWindow
class CurrencyConv(QtWidgets.QMainWindow):
    def __init__(self):
        super(CurrencyConv, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.init_UI()


    def init_UI(self):
        self.setWindowTitle('Конвертатор Валют')
        self.setWindowIcon(QIcon('exchanging.png'))

        self.ui.lineEdit.setPlaceholderText('%Из валюты%')
        self.ui.lineEdit_2.setPlaceholderText('%Внесенная сумма%')
        self.ui.lineEdit_3.setPlaceholderText('%В валюту%')
        self.ui.lineEdit_4.setPlaceholderText('%Получаемая сумма%')
        self.ui.pushButton.clicked.connect(self.converter)

    def converter(self):
        c = CurrencyConverter()
        input_currency = self.ui.lineEdit.text()
        input_amount = int(self.ui.lineEdit_2.text())
        output_currency = self.ui.lineEdit_3.text()

        output_amount = round(c.convert(input_amount, '%s' % (input_currency), '%s' % (output_currency)), 2)

        self.ui.lineEdit_4.setText(str(output_amount))



app = QtWidgets.QApplication([])
application = CurrencyConv()
application.show()

sys.exit(app.exec())