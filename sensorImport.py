from PySide6.QtWidgets import QLabel

class sensorValues (QLabel):
    def __init__(self, parent=None):
        super().__init__(parent)

        self.sensorLabel1 = QLabel("Sensor 1")
        self.sensorLabel2 = QLabel("Sensor 2")
        self.sensorLabel3 = QLabel("Sensor 3")
        self.sensorLabel4 = QLabel("Sensor 4")

        self.sensor1 = QLabel("1000")
        self.sensor2 = QLabel("1000")
        self.sensor3 = QLabel("1000")
        self.sensor4 = QLabel("1000")