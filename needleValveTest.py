from PySide6.QtCore import Qt
from PySide6.QtWidgets import QApplication, QSlider

#The slot : responds when something happens
def respond_to_slider(data):
        print("Valve moved to : Degrees", data)

def respond_to_switch(data):
        if (data) == 1:
                print("Open")
        else:
                print("Closed")

app = QApplication()
slider = QSlider(Qt.Horizontal)
slider.setMinimum(0)
slider.setMaximum(720)
slider.setValue(1)



#You just do the connection. The Qt system takes care of
#  passing the data from the signal to the slot.
slider.valueChanged.connect(respond_to_slider)
slider.show()
app.exec()