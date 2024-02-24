from PySide6.QtWidgets import QApplication, QMainWindow, QLabel, QHBoxLayout, QWidget, QPushButton
import numpy
import cv2
from PySide6.QtGui import QImage, QPixmap
from PySide6.QtCore import QTimer

class WebcamApp(QMainWindow):
    def __init__(self, stream):
        super().__init__()
        self.vid_server = stream

        # Create a QLabel to display the image
        self.label = QLabel()
        self.setCentralWidget(self.label)

        # Set up a QTimer to update the image
        self.timer = QTimer()
        self.timer.setInterval(10)  # Update interval in milliseconds
        self.timer.timeout.connect(self.update_image)
        self.timer.start()


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
