# Rocketry Gui


### General Description
This GUI has the primary and broader purpose of visualising rocket sensor data and actuating controls on board the rocket, including valve opening and soft/hard abort procedures.
The GUI has a single main screen, from which sensor data can be read, and valves can be actuated. Functionality in regards to displaying graphical data and locating sensors on PID diagram will be added in time.

## Current Modules
#### Required packages
PySide6

### Main
This module takes in the Main Window module and executes code.

### Main Window
This module takes in the various classes/modules that comprise the widgets and arranges them.

### Sensor Import
This module takes in sensor data and is accessible to Main Window to display on the GUI.

### Toggle Switch
The Open/Closed toggle switch is a basic state machine between on or off which is to be used with regards to opening/closing valves on the rocket. Actuation using it can be tested using a simple LED/resistor circuit on a breadboard, or connecting the switch 'output' to an LED on the LabJack.

Sourced from pyQT example state based code.

### Needle Valve Slider
The needle valve actuator is a draft slider switch that can be used to control how opeon the valve is. Currently not needed.
