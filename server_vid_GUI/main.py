from PySide6.QtWidgets import QApplication
from vidwindow import WebcamApp
import sys

app = QApplication(sys.argv)

window = WebcamApp(app)
window.show()
app.exec()