import sys
import p2.py
from PyQt5 import QtWidgets


class Window(QtWidgets.QWidget):

    def __init__(self):
        super().__init__()
        self.init_ui()

    def init_ui(self):
        self.generateButton = QtWidgets.QPushButton('Generate')
        self.customerLine = QtWidgets.QLineEdit(maxLength=10)
        self.barcodeLine = QtWidgets.QLineEdit()
        self.customerLabel = QtWidgets.QLabel('Customer')
        self.barcodeLabel = QtWidgets.QLabel('Barcode')

        barcode_box = QtWidgets.QHBoxLayout()
        barcode_box.addWidget(self.customerLabel)
        barcode_box.addWidget(self.customerLine)

        customer_box = QtWidgets.QHBoxLayout()
        customer_box.addWidget(self.barcodeLabel)
        customer_box.addWidget(self.barcodeLine)

        bottom_box = QtWidgets.QHBoxLayout()
        bottom_box.addWidget(self.generateButton)

        v_box = QtWidgets.QVBoxLayout()
        v_box.addLayout(barcode_box)
        v_box.addLayout(customer_box)
        v_box.addLayout(bottom_box)

        self.setLayout(v_box)
        self.setWindowTitle('Template builder')

        self.generateButton.clicked.connect(self.btn_clk)

        self.show()

    def btn_clk(self):
        sender = self.sender()
        if sender.text() == 'Generate':
            print('success')
            self.customerLine.clear()
            self.barcodeLine.clear()
        
            

app = QtWidgets.QApplication(sys.argv)

a_window = Window()
sys.exit(app.exec_())
        

