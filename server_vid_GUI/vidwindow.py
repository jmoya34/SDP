from PySide6.QtWidgets import QApplication, QMainWindow, QLabel, QVBoxLayout, QWidget
from PySide6.QtGui import QImage, QPixmap
from PySide6.QtCore import QTimer
from vidServer import vidServer

class WebcamApp(QMainWindow):
    def __init__(self, app):
        super().__init__()
        self.vidImg = vidServer(6789)
        # Initialize QLabel as the central widget
        self.image_label = QLabel(self)
        self.setCentralWidget(self.image_label)

        # Setup Timer
        self.timer = QTimer(self)
        self.timer.timeout.connect(self.update_image)
        self.timer.start(100)  # Update interval in milliseconds (e.g., 100 ms for 10 times per second)

        # Window settings
        self.setWindowTitle('PyQt6 Live Image Update')
        self.setGeometry(100, 100, 800, 600)  # x, y, width, height

        # Initial image setup or variable
        self.image_path = self.img
        self.display_image(self.image_path)

    def display_image(self, image_path):
        # Load the image
        pixmap = QPixmap(image_path)

        # Set the pixmap onto the label
        self.image_label.setPixmap(pixmap)

        # Resize the label to fit the image
        self.image_label.resize(pixmap.width(), pixmap.height())

    def update_image(self):
        self.img = self.vidImg.getImg()
        if self.img is not None:
            self.image_path = self.img
            self.display_image(self.image_path)