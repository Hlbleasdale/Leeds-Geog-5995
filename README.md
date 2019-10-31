# Leeds-Geog-5995
Agent Based Modelling for Assignment 1 of Leeds 2019 Programming for Social Sciences Module

## This repository contains outputs from the Leeds Programming for Social Sciences Module, which focussed on Agent Based Modelling. 

The agent based model has been programmed in python, using the platform Spyder. 

### agentframework.py
The file, agentframework.py, contains the class which 
specifically deals with the agents - which represent sheep in this simulation. The agentframework.py defines various functions for the agents 
(sheep): 

* to initially place the sheep at a random starting point within the environment 
* to move the sheep depending on the output of a (pseudo-)random conditional statement 
* to make the sheep eat the environment and increase their food stores
* to work out the distance (using pythagoras theorem) between nearby sheep and itself
* to share food stores with nearby sheep within a given neighbourhood area (defined in the model)

### model.py
The model.py file executes the Agent Based Model, the animation of the model, and displays this with a Graphical User Interface (GUI).
It is also in the model.py program where the number of agents (sheep) can be altered, along with the number of iterations (times the sheep
may move) and the boundary of the neighbourhood which affects how the agent (sheep) shares its food stores.

For the model to run as a GUI, the graphics settings on the Spyder IPython console should to be set to Tkinter. To do this: go to Tools > Preferences >
IPython Console > Graphics > Graphics Backend, and in the Backened dropdown list, the backend should be set to Tkinter. Then restart the console and 
the GUI should run. After the code has run, and a model box appears, click on Model and a dropdown list should appear with Run or Quit. Choose Run to 
see the model. 
