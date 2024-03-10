import sys
from PyQt6.QtWidgets import QApplication, QWidget, QPushButton, QHBoxLayout, QLabel, QVBoxLayout, QLineEdit
from PyQt6.QtCore import QTimer
from PyQt6.QtGui import QImage, QPixmap
from vidServer import vidServer
from messageServer import sendCommand
import cv2

class ArrowButtonsDemo(QWidget):
    def __init__(self):
        super().__init__()
        self.vid_server = vidServer(6789)  # Create your vidServer instance
        self.commandPi = sendCommand('192.168.254.20', 65432)
        self.motorPos1 = 0
        self.motorPos2 = 0
        self.maxMotorPos = 100
        self.minMotorPos = 0
        self.initUI()

    def initTelescopeCam(self):
        # Create a QLabel to display the image
        self.label = QLabel()

        # Set up a QTimer to update the image
        self.timer = QTimer()
        self.timer.setInterval(10)  # Update interval in milliseconds
        self.timer.timeout.connect(self.update_image)
        self.timer.start()

    def initUI(self):
        layout = QVBoxLayout()

        # Create text box to send to server
        self.commandsLayout = self.createTextField()
        self.confirmCommandBtn.clicked.connect(self.sendCommand)
        # Create servo1 Buttons
        self.serv1layout = self.createServo1Buttons()
        self.serv1Lbutton.clicked.connect(self.serv1LeftClicked)
        self.serv1Rbutton.clicked.connect(self.serv1RightClicked)
        # Create servo2 Buttons
        self.serv2layout = self.createServo2Buttons()
        self.serv2Lbutton.clicked.connect(self.serv2LeftClicked)
        self.serv2Rbutton.clicked.connect(self.serv2RightClicked)

        # Set up an updating field for drone status
        self.statusLayout = self.infoLabels()
        self.infotimer = QTimer()
        self.infotimer.setInterval(300)  # Update interval in milliseconds
        self.infotimer.timeout.connect(self.update_info)
        self.infotimer.start()

        # Create vid window
        self.initTelescopeCam()

        # Add all the UI layouts together
        layout.addLayout(self.commandsLayout)
        layout.addLayout(self.serv1layout)
        layout.addLayout(self.serv2layout)
        layout.addLayout(self.statusLayout)
        
        # Main layout
        mainLayout = QHBoxLayout()
        mainLayout.addLayout(layout)
        mainLayout.addWidget(self.label)

        # Put final layout into window
        self.setLayout(mainLayout) 
        self.setWindowTitle('Prototype gui')

    def createTextField(self):
        commandsLayout = QHBoxLayout()

        commandServerLabel = QLabel("Command:") # Text 
        commandsLayout.addWidget(commandServerLabel)
        self.commandBox = QLineEdit() # Text box
        commandsLayout.addWidget(self.commandBox)
        self.confirmCommandBtn = QPushButton("Send") # Button
        commandsLayout.addWidget(self.confirmCommandBtn)
        return commandsLayout

    def createServo1Buttons(self):
        # Servo 1 buttons
        layout = QVBoxLayout()

        self.serv1Text = QLabel("Servo1 Position:")
        layout.addWidget(self.serv1Text)
        # buttons
        buttonLayout = QHBoxLayout()
        self.serv1Lbutton = QPushButton("←")
        buttonLayout.addWidget(self.serv1Lbutton)
        self.serv1Rbutton = QPushButton("→")
        buttonLayout.addWidget(self.serv1Rbutton)
        layout.addLayout(buttonLayout)
        return layout
    
    def createServo2Buttons(self):
        # Servo 2 buttons
        layout = QVBoxLayout()

        self.serv2Text = QLabel("Servo2 Position:")
        layout.addWidget(self.serv2Text)
        # buttons
        buttonLayout = QHBoxLayout()
        self.serv2Lbutton = QPushButton("←")
        buttonLayout.addWidget(self.serv2Lbutton)
        self.serv2Rbutton = QPushButton("→")
        buttonLayout.addWidget(self.serv2Rbutton)
        layout.addLayout(buttonLayout)
        return layout

    def sendCommand(self):
        text = self.commandBox.text() # String class data type
        self.process_command(text)

    def posToDict(self):
        return '{"Motor1": ' + str(self.motorPos1) + ', "Motor2": ' + str(self.motorPos2) + '}'

    def serv1LeftClicked(self):
        print("Servro 1 Left button clicked")
        if self.motorPos1 != self.minMotorPos:
            self.motorPos1 -= 1
        text = self.posToDict()
        print("Sending: ", text)
        self.commandPi.sendMsg(text)


    def serv1RightClicked(self):
        print("Servro 1 Right button clicked")
        if self.motorPos1 != self.maxMotorPos:
            self.motorPos1 += 1
        text = self.posToDict()
        print("Sending: ", text)
        self.commandPi.sendMsg(text)

    def serv2LeftClicked(self):
        print("Servro 2 Left button clicked")
        if self.motorPos2 != self.minMotorPos:
            self.motorPos2 -= 1
        text = self.posToDict()
        print("Sending: ", text)
        self.commandPi.sendMsg(text)

    def serv2RightClicked(self):
        print("Servro 2 Right button clicked")
        if self.motorPos2 != self.maxMotorPos:
            self.motorPos2 += 1
        text = self.posToDict()
        print("Sending: ", text)
        self.commandPi.sendMsg(text)
    
    def infoLabels(self):
        # Create layout
        layout = QVBoxLayout()

        # Text types
        self.constellation = QLabel("Current Constellation:")
        self.uavHeight = QLabel("Height: ")
        self.battery = QLabel("Battery left:")
        self.camAngle = QLabel("Camera Angle:")

        # Add into vertical layout
        layout.addWidget(self.constellation)
        layout.addWidget(self.uavHeight)
        layout.addWidget(self.battery)
        layout.addWidget(self.camAngle)

        return layout


    def process_command(self, command):
        parts = command.split()
        if len(parts) != 3 or parts[0].lower() != "set":
            print("Invalid command format.")
            return
        
        # Extract the servo name and position from the command
        servo_name = parts[1].lower()
        try:
            position = int(parts[2])
        except ValueError:
            print("Invalid position: must be a number.")
            return

        if servo_name == "servo1":
            print(f"Setting Servo1 to position {position}.")
            self.motorPos1 = position
        elif servo_name == "servo2":
            print(f"Setting Servo2 to position {position}.")
            self.motorPos2 = position
        else:
            # Handle the case where the servo name is unknown
            print(f"Unknown servo: {servo_name}")
            return
        
        text = self.posToDict()
        print("Sending: ", text)
        self.commandPi.sendMsg(text)
        


    def update_info(self):
        print("Getting info")
        #To change labels try
        #ADD self.constellation.setText(new_text)

        self.serv1Text.setText("Servo1 Position: " + str(self.motorPos1))
        self.serv2Text.setText("Servo2 Position: " + str(self.motorPos2))

    def update_image(self):
        # Get a new image from the vidServer
        img = self.vid_server.getImg()
        if img is not None:
            # Convert the NumPy array to QImage
            img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
            height, width, channels = img.shape
            bytes_per_line = channels * width
            q_image = QImage(img.data, width, height, bytes_per_line, QImage.Format.Format_RGB888)

            # Convert QImage to QPixmap and display it
            pixmap = QPixmap.fromImage(q_image)
            self.label.setPixmap(pixmap)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    demo = ArrowButtonsDemo()
    demo.show()
    sys.exit(app.exec())