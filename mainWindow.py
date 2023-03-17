from PySide6.QtWidgets import QWidget, QGridLayout
from buttonTest import button_row
from sensorImport import sensorValues

class main_window(QWidget):

    def __init__(self):
        super(main_window, self).__init__()

        self.setWindowTitle("Draft GUI")

        layout = QGridLayout()

        buttons = button_row()
        data = sensorValues()

        layout.addWidget(buttons.btnOneLabel, 0, 0)
        layout.addWidget(buttons.btnTwoLabel, 0, 1)
        layout.addWidget(buttons.btnThreeLabel, 0, 2)
        layout.addWidget(buttons.btnFourLabel, 0, 3)

        layout.addWidget(buttons.btnOne, 1, 0)
        layout.addWidget(buttons.btnTwo, 1, 1)
        layout.addWidget(buttons.btnThree, 1, 2)
        layout.addWidget(buttons.btnFour, 1, 3)

        layout.addWidget(data.sensorLabel1, 3, 0)
        layout.addWidget(data.sensorLabel2, 3, 1)
        layout.addWidget(data.sensorLabel3, 3, 2)
        layout.addWidget(data.sensorLabel4, 3, 3)

        layout.addWidget(data.sensor1, 4, 0)
        layout.addWidget(data.sensor2, 4, 1)
        layout.addWidget(data.sensor3, 4, 2)
        layout.addWidget(data.sensor4, 4, 3)

        self.setLayout(layout)