# Import appropriate libraries 
# Import matplotlib for plotting
import matplotlib 
# Ask matplotlib to use 'Tkagg' - this uses a different backend for graphics,
# this must be done before importing matplotlib.pyplot or it will have no effect
matplotlib.use('TkAgg')
# Import Tk interface - a GUI toolkit
import tkinter
# Import matplotlib.animation to enable animations
import matplotlib.animation
# Import matplotlib.pyplot to aid plotting
import matplotlib.pyplot 
# Import the 'Agent' class which contains functions for the agents
import agentframework 
# Import csv library to read in the in.txt (environment) file
import csv
# Import random library to shuffle the agents in a pseudo-random way
import random

# Initialise environment, firstly by creating an empty list
environment = []
# Read in the text file using the relevant file path and using 
# the delimiter (,) to separate the values in the file
with open("C:/Users/hopeb/OneDrive/Documents/Fourth Year 201920/ENVS802 LEEDS Programming for Social Scientists/in.txt") as f:
    reader = csv.reader(f, delimiter=',', quoting = csv.QUOTE_NONNUMERIC)
    # Create a for-loop to make each row a list in the environment,
    # with each row being filled with values 
    for row in reader:
        # Create an empty variable, environment_row, to store values 
        environment_row = []
        for value in row:
            # Use the append function to add values to the rows 
            environment_row.append(int(value))
        # Append the environment_row to the environment list
        environment.append(environment_row)
      
# Set up an empty list for the agents variable
agents = []
# Set the number of agents (sheep) in the model 
num_of_agents = 40
# Set the number of iterations (times the agents/sheep move)
num_of_iterations = 100
# Create a neighbourhood variable to define the distance whereby agents begin
# interacting with one another
neighbourhood = 10

# Create the agents, using the imported agentframework and append 
# the agents to the environment
for i in range(num_of_agents):
    agents.append(agentframework.Agent(environment,agents))
   
# Create a figure using matplotlib and set the dimensons of this    
fig = matplotlib.pyplot.figure(figsize=(8, 8))
ax = fig.add_axes([0, 0, 1, 1])

# Define carry_on
carry_on = True

# Set up the model for the animation
def update(frame_number):
    fig.clear()
    global carry_on
    
    # Display the environment
    matplotlib.pyplot.imshow(environment)
    
    # Shuffle the agents (pseudo-)randomly
    random.shuffle(agents)
    
    # Make the agents move, eat and share food stores with neighbours, using a for-loop
    for i in range(num_of_agents):
        agents[i].move()
        agents[i].eat()
        agents[i].share(neighbourhood)
    
    # Plot the agents - using the marker "d" for a diamond shape, colour is set to white with a black outline and size is 100
    for i in range(num_of_agents):
        matplotlib.pyplot.scatter(agents[i].x,agents[i].y, marker="d", edgecolor='black', c="white", s=100)
        # Add labels of the agent's (sheep's) food stores
        matplotlib.pyplot.annotate(agents[i].store, (agents[i].x,agents[i].y), fontsize=10, 
                                   color="pink", weight="bold", va="bottom", ha="right")
        
    # Set up the x and y axis limits
    matplotlib.pyplot.xlim(0,300)
    matplotlib.pyplot.ylim(0,300)
    # Set the title
    matplotlib.pyplot.title("Agent Based Model of Sheep in an Environment", fontsize='x-large')
    # Set the axis labels to 'Environment'
    matplotlib.pyplot.ylabel("Environment")
    matplotlib.pyplot.xlabel("Environment")
        
    # Create a stopping function, where when all the sheep have eaten enough, 
    # the model stops. 
    # First create an empty variable, total, which will store the number of
    # agents that have eaten enough
    total = 0
    # Create a for-loop, which calls the eaten_enough function and tests whether
    # the agents are full
    for i in range(num_of_agents):
        agent_full = agents[i].eaten_enough() 
        if agent_full == 1:
            # When agents are full, add 1 to the total
            total += 1
            # Test this works by printing
            #print("Sheep", agents[i], "has eaten enough, my store is: {}".format(agents[i].store))
            print("Amount of sheep that have eaten enough:", total)
    # Once total reaches the number of agents (once all of the sheep are full)        
    if total == (num_of_agents):
        # Stop the model and print 'stopping condition'
        carry_on = False
        print ("Stopping condition: all the sheep have eaten enough.")
        
# Loop the animation until the number of iterations has been met
# and until the stopping condition is brought in
def general_function(b = [0]):
    # Set up an empty variable, a
    a = 0
    # continue running the model whilst the number of iterations hasn't been
    # reached and carry on is still set to True
    global carry_on 
    while (a < num_of_iterations) & (carry_on) :
        yield a			
        a = a + 1
 
# Create a command to run the animation 
def run(): 
    animation = matplotlib.animation.FuncAnimation(fig, update, frames=general_function, repeat=False)
    canvas.draw()

# Create a 'quitting' function to use to stop the animation at any time 
def quit():
    global root
    root.destroy 

# When the code is run, python creates a window 'root' where the animation is displayed
root = tkinter.Tk()
# Set the title of the animation
root.wm_title("Agent Based Model of Sheep in an Environment")
# Set a canvas for the animation to be plotted onto
canvas = matplotlib.backends.backend_tkagg.FigureCanvasTkAgg(fig, master=root)
canvas._tkcanvas.pack(side=tkinter.TOP, fill=tkinter.BOTH, expand=1)
# Create a menu bar for the window 
menu_bar = tkinter.Menu(root)
root.config(menu=menu_bar)
model_menu = tkinter.Menu(menu_bar)
menu_bar.add_cascade(label="Model", menu=model_menu)
# Create commands which call functions - run and quit
# This allows the user to click run - to run model
model_menu.add_command(label="Run model", command=run)
# And allows the user to click quit - to quit model
model_menu.add_command(label="Quit model", command=quit)

# The following line of code must go at the end - this runs the animation
tkinter.mainloop()  
