import sys
from PyQt5 import QtWidgets
#import p2


class loginWindow(QtWidgets.QWidget):

    def __init__(self):
        super().__init__()
        self.init_window()

    def init_window(self):
        self.loginButton = QtWidgets.QPushButton('Login')
        self.usernameLine = QtWidgets.QLineEdit()
        self.passwordLine = QtWidgets.QLineEdit()
        self.usernameLabel = QtWidgets.QLabel('Username')
        self.passwordLabel = QtWidgets.QLabel('Password')

        password_box = QtWidgets.QHBoxLayout()
        password_box.addWidget(self.passwordLabel)
        password_box.addWidget(self.passwordLine)

        user_box = QtWidgets.QHBoxLayout()
        user_box.addWidget(self.usernameLabel)
        user_box.addWidget(self.usernameLine)

        bottom_box = QtWidgets.QHBoxLayout()
        bottom_box.addWidget(self.loginButton)

        v_box = QtWidgets.QVBoxLayout()
        v_box.addLayout(user_box)
        v_box.addLayout(password_box)
        v_box.addLayout(bottom_box)

        self.setLayout(v_box)
        self.setWindowTitle('Login')
        self.clicked = False
        self.username = ''
        self.password = ''

        self.loginButton.clicked.connect(self.btn_clk)

    
    def btn_clk(self):

        sender = self.sender()
        if sender.text() == 'Login':
            if(self.username != '' and self.password != ''):
                self.username = self.usernameLine.text()
                self.password = self.passwordLine.text()
                self.clicked = True

    def clicked(self):
        return self.clicked            

    def getUser(self):
        return self.username;

    def getPassword(self):
        return self.password;

    def resetForm(self):
        self.clicked = False
        #self.usernameLine.clear()
        #self.passwordLine.clear()

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
        self.resize(250,175)
        self.setWindowTitle('Template Builder')

        self.generateButton.clicked.connect(self.btn_clk)

    def btn_clk(self):
        sender = self.sender()
        if (sender.text() == 'Generate' and self.customerLine.text() != ''):
            self.newLogin = loginWindow()
            self.newLogin.show()
            if (self.newLogin.clicked()):
                #x = Builder(self.getBarcode(),self.getCustomer(),self.loginWindow.getUser(),self.loginWindow.getPassword())
                #x.start()
                #print(self.loginWindow.getUser(),self.loginWindow.getPassword())
                print('clicked')
                #self.loginWindow.close()
                self.loginWindow.resetForm()
                #self.loginWindow.close()
            self.customerLine.clear()
            self.barcodeLine.clear()

    def getBarcode(self):

        return self.barcodeLine.text()

    def getCustomer(self):

        return self.customerLine.text()
            
            

def main():
    app = QtWidgets.QApplication(sys.argv)
    main = Window()
    main.show()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()
        

