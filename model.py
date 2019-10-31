# Import appropriate libraries 
import matplotlib 
matplotlib.use('TkAgg')
import tkinter 
import matplotlib.animation 
import matplotlib.pyplot 
# Import the 'Agent' class which contains functions for the agents
import agentframework 
# Import csv library to read in the in.txt (environment) file
import csv
# Import random library to shuffle the agents in a pseudo-random way
import random
# Import imageio library to save images and gifs
import imageio 
# Import os functions to aid reading and writing paths - for saving the gif
import os

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
        # Append the rowlist to the environment list
        environment.append(environment_row)
      
# Set up an empty list for the agents variable
agents = []
# Set the number of agents (sheep) in the model 
num_of_agents = 50
# Set the number of iterations (times the agents/sheep move)
num_of_iterations = 20
# Create a neighbourhood variable to define the distance whereby agents begin
# interacting with one another
neighbourhood = 100

# Create the agents, using the imported agentframework and append 
# the agents to the environment
for i in range(num_of_agents):
    agents.append(agentframework.Agent(environment,agents))
   
# Create a figure using matplotlib and set the dimensons of this    
fig = matplotlib.pyplot.figure(figsize=(8, 8))
ax = fig.add_axes([0, 0, 1, 1])

# Define carry_on to continue running the model ??
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
    matplotlib.pyplot.ylabel("Environment")
    matplotlib.pyplot.xlabel("Environment")
    
    #  Create a stopping condition, whereby if the environment is empty,
    # the animation stops
    total = 0
    for row in range(99):
        for value in range(99):
            total += environment[row][value]
    if total <= 0:
        carry_on = False
    print('Stopping condition')
    
# Loop the animation until the number of iterations has been met
# and until the stopping condition is brought in
def general_function(b = [0]):
    a = 0
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

# Save a gif of the model 
# First set the filepath    
png_dir = 'C:/Users/hopeb/OneDrive/Documents/Fourth Year 201920/ENVS802 LEEDS Programming for Social Scientists/Leeds-Geog-5995/'
# Create an empty list, images, to later store the gif
images = []
# Create a for loop to append the resulting gif to the filepath
for file_name in os.listdir(png_dir):
    if file_name.endswith('png'):
        file_path = os.path.join(png_dir, file_name)
        images.append(imageio.imread(file_path))
# Set a location and filename for it to save to
imageio.mimsave('C:/Users/hopeb/OneDrive/Documents/Fourth Year 201920/ENVS802 LEEDS Programming for Social Scientists/Leeds-Geog-5995/sheepmovie.gif', images, duration = 5, fps=55)


root = tkinter.Tk()
root.wm_title("Agent Based Model of Sheep in an Environment")
canvas = matplotlib.backends.backend_tkagg.FigureCanvasTkAgg(fig, master=root)
canvas._tkcanvas.pack(side=tkinter.TOP, fill=tkinter.BOTH, expand=1)
menu_bar = tkinter.Menu(root)
root.config(menu=menu_bar)
model_menu = tkinter.Menu(menu_bar)
menu_bar.add_cascade(label="Model", menu=model_menu)
model_menu.add_command(label="Run model", command=run)
model_menu.add_command(label="Quit model", command=quit)

tkinter.mainloop()    
    



