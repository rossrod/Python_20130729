#! /usr/bin/env python3.3

import sys

from PySide.QtGui import (
    QApplication,
    QFrame, QRadioButton, QLineEdit,
    QVBoxLayout, QHBoxLayout
)

class MainWindow(QFrame):
    def __init__(self):
        super(MainWindow, self).__init__()
        buttonsLayout = QVBoxLayout()
        celsiusButton = QRadioButton('Celsius')
        fahrenheitButton = QRadioButton('Fahrenheit')
        buttonsLayout.addWidget(celsiusButton)
        buttonsLayout.addWidget(fahrenheitButton)
        dataEntry = QLineEdit()
        applicationLayout = QHBoxLayout()
        applicationLayout.addLayout(buttonsLayout)
        applicationLayout.addWidget(dataEntry)
        self.setLayout(applicationLayout)
        self.setWindowTitle('Temperature Converter')
        self.show()

if __name__ == '__main__':
    application = QApplication(sys.argv)
    mainWindow = MainWindow()
    sys.exit(application.exec_())
