from PyQt6.QtWidgets import QApplication, QWidget, QVBoxLayout, QLineEdit, QPushButton, QMessageBox
from client.messageServer import sendCommand

class MyWindow(QWidget):
    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):
        self.setWindowTitle('Text Box Example')
        self.setGeometry(100, 100, 300, 200)

        layout = QVBoxLayout()

        self.textbox = QLineEdit(self)
        layout.addWidget(self.textbox)

        self.button = QPushButton('Get Text', self)
        self.button.clicked.connect(self.on_button_click)
        layout.addWidget(self.button)

        self.setLayout(layout)

    def on_button_click(self):
        text = self.textbox.text()
        if text is not '':
            print("sending mesage...")
            startServer = sendCommand('10.110.220.71', 65432)
            startServer.sendMsg(text)