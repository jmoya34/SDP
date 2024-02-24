#pip install PySide6

from PySide6.QtWidgets import QApplication
from vidwindow import WebcamApp
from vidServer import vidServer
from vidwindow import WebcamApp
import sys

def main():
    app = QApplication(sys.argv)
    vid_img = vidServer(6789)  # Create your vidServer instance
    window = WebcamApp(vid_img)
    window.show()
    sys.exit(app.exec())

if __name__ == "__main__":
    main()