'''Basic Tax Calculator

This application accepts two inputs including a price and a tax rate, it then outputs this to a results window.

Created: September 2016
Author: Edward Haigh
'''

import sys
from PyQt4 import QtCore, QtGui, uic
 
qtCreatorFile = "design.ui" # Enter file here.
 
Ui_MainWindow, QtBaseClass = uic.loadUiType(qtCreatorFile)
 
class MyApp(QtGui.QMainWindow, Ui_MainWindow):
    def __init__(self):
        QtGui.QMainWindow.__init__(self)
        Ui_MainWindow.__init__(self)
        self.setupUi(self)
        self.calculate.clicked.connect(self.CalculateTax)

    def CalculateTax(self):
        price = int(self.price.toPlainText())
        tax = int(self.tax.toPlainText())
        total_price = price + ((tax/100) * price)
        self.total.setText(str(total_price))
 
if __name__ == "__main__":
    app = QtGui.QApplication(sys.argv)
    window = MyApp()
    window.show()
    sys.exit(app.exec_())