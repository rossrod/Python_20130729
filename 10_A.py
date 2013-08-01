#! /usr/bin/env python3.3

import sys

from PySide.QtGui import (
    QApplication, QFrame, QRadioButton,
    QVBoxLayout
)

class MainWindow(QFrame):
    def __init__(self):
        super(MainWindow, self).__init__()
        buttonsLayout = QVBoxLayout()
        button = QRadioButton('button')
        buttonsLayout.addWidget(button)
        self.setLayout(buttonsLayout)
        self.show()

if __name__ == '__main__':
    application = QApplication(sys.argv)
    mainWindow = MainWindow()
    sys.exit(application.exec_())
