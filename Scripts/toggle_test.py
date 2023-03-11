# Copyright (C) 2010 velociraptor Genjix <aphidia@hotmail.com>
# Copyright (C) 2022 The Qt Company Ltd.
# SPDX-License-Identifier: LicenseRef-Qt-Commercial OR BSD-3-Clause

import sys

from PySide6.QtWidgets import QApplication, QPushButton
from PySide6.QtStateMachine import QState, QStateMachine


if __name__ == '__main__':
    app = QApplication(sys.argv)
    button = QPushButton()
    machine = QStateMachine()

    closed = QState()
    closed.assignProperty(button, 'text', 'Closed')
    closed.setObjectName('closed')

    open = QState()
    open.setObjectName('Open')
    open.assignProperty(button, 'text', 'Open')

    closed.addTransition(button.clicked, open)
    open.addTransition(button.clicked, closed)

    machine.addState(closed)
    machine.addState(open)
    machine.setInitialState(closed)
    machine.start()
    button.resize(100, 50)
    button.show()
    sys.exit(app.exec())