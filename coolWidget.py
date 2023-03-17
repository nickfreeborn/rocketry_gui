from PySide6.QtWidgets import QWidget,QPushButton,QHBoxLayout,QVBoxLayout
from PySide6.QtStateMachine import QState, QStateMachine


class hellYeah (QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Hell Yeah")


        button1 = QPushButton()
        # button1.clicked.connect(self.button1_clicked)
        button2 = QPushButton()
        # button2.clicked.connect(self.button2_clicked)

        machine1 = QStateMachine()
        machine2 = QStateMachine()

        closed1 = QState()
        closed1.assignProperty(button1, 'text', 'Closed')
        closed1.setObjectName('closed')

        closed2 = QState()
        closed2.assignProperty(button2, 'text', 'Closed')
        closed2.setObjectName('closed')

        open1 = QState()
        open1.setObjectName('Open')
        open1.assignProperty(button1, 'text', 'Open')

        open2 = QState()
        open2.setObjectName('Open')
        open2.assignProperty(button2, 'text', 'Open')

        closed1.addTransition(button1.clicked, open1)
        open1.addTransition(button1.clicked, closed1)

        closed2.addTransition(button2.clicked, open2)
        open2.addTransition(button2.clicked, closed2)

        machine1.addState(closed1)
        machine1.addState(open1)
        machine1.setInitialState(closed1)
        machine1.start()

        machine2.addState(closed2)
        machine2.addState(open2)
        machine2.setInitialState(closed2)
        machine2.start()


        button_layout = QHBoxLayout()
        button_layout.addWidget(button1)
        button_layout.addWidget(button2)

        self.setLayout(button_layout)

    # def button1_clicked(self):
    #     print("Button1 clicked")

    # def button2_clicked(self):
    #     print("Button2 clicked")


