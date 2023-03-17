from PySide6.QtWidgets import QWidget, QGridLayout, QPushButton, QLabel, QApplication

import sys

class button_row (QWidget):

    def __init__(self, parent=None):
        super().__init__(parent)
        self.btnOneLabel = QLabel("Valve 1")
        self.btnTwoLabel = QLabel("Valve 2")
        self.btnThreeLabel = QLabel("Valve 3")
        self.btnFourLabel = QLabel("Valve 4")

        self.btnOne = QPushButton(text="I'm Open!", parent=self)
        self.btnOne.setFixedSize(150, 60)
        self.btnOne.setCheckable(True)
        self.btnOne.setChecked(True)
        self.btnOne.clicked.connect(self.onBtnOneClicked)

        self.btnTwo = QPushButton(text="I'm Open!", parent=self)
        self.btnTwo.setFixedSize(150, 60)
        self.btnTwo.setCheckable(True)
        self.btnTwo.setChecked(True)
        self.btnTwo.clicked.connect(self.onBtnTwoClicked)

        self.btnThree = QPushButton(text="I'm Open!", parent=self)
        self.btnThree.setFixedSize(150, 60)
        self.btnThree.setCheckable(True)
        self.btnThree.setChecked(True)
        self.btnThree.clicked.connect(self.onBtnThreeClicked)

        self.btnFour = QPushButton(text="I'm Open!", parent=self)
        self.btnFour.setFixedSize(150, 60)
        self.btnFour.setCheckable(True)
        self.btnFour.setChecked(True)
        self.btnFour.clicked.connect(self.onBtnFourClicked)

        # self.setWindowTitle("Draft GUI")

        # layout = QGridLayout()

        # #buttons = button_row()
        # #data = sensorValues()

        # layout.addWidget(self.btnOneLabel, 0, 0)
        # layout.addWidget(self.btnTwoLabel, 0, 1)
        # layout.addWidget(self.btnThreeLabel, 0, 2)
        # layout.addWidget(self.btnFourLabel, 0, 3)

        # layout.addWidget(self.btnOne, 1, 0)
        # layout.addWidget(self.btnTwo, 1, 1)
        # layout.addWidget(self.btnThree, 1, 2)
        # layout.addWidget(self.btnFour, 1, 3)

        # self.setLayout(layout)

        

    def onBtnOneClicked(self):

        print("Valve 1 actuated")

        if self.btnOne.isChecked():
            self.btnOne.setText("I'm Open!")
        else:
            self.btnOne.setText("I'm Closed!")

    def onBtnTwoClicked(self):
        
        print("Valve 2 actuated")

        if self.btnTwo.isChecked():
            self.btnTwo.setText("I'm Open!")
        else:
            self.btnTwo.setText("I'm Closed!")

    def onBtnThreeClicked(self):

        print("Valve 3 actuated")

        if self.btnThree.isChecked():
            self.btnThree.setText("I'm Open!")
        else:
            self.btnThree.setText("I'm Closed!")

    def onBtnFourClicked(self):

        print("Valve 4 actuated")

        if self.btnFour.isChecked():
            self.btnFour.setText("I'm Open!")
        else:
            self.btnFour.setText("I'm Closed!")

class main_window(QWidget):

    def __init__(self):
        super(main_window, self).__init__()

        self.setWindowTitle("Draft GUI")

        layout = QGridLayout()

        layout.addWidget(button_row.btnOneLabel, 0, 0)
        layout.addWidget(button_row().btnTwoLabel, 0, 1)
        layout.addWidget(button_row().btnThreeLabel, 0, 2)
        layout.addWidget(button_row().btnFourLabel, 0, 3)

        layout.addWidget(button_row().btnOne, 1, 0)
        layout.addWidget(button_row().btnTwo, 1, 1)
        layout.addWidget(button_row().btnThree, 1, 2)
        layout.addWidget(button_row().btnFour, 1, 3)

        self.setLayout(layout)

app = QApplication(sys.argv)

window = main_window()
window.show()

app.exec()