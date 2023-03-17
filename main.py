from PySide6.QtWidgets import QApplication, QWidget
from mainWindow import main_window

import sys

app = QApplication(sys.argv)

window = main_window()
window.show()

app.exec()