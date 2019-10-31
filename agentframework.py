# Import random library to generate pseudo-random numbers 
import random
        
# Create a class of agents 
class Agent: 
    #Use the __init__ function to construct attributes of the agents
    def __init__(self, environment, agents):
    # Set the x and y value of agents to be a random integer between 0
    # and the maximum length of the rows and columns of the environment.
    # To do this, first create the variables 'nrows' and 'ncols' to store 
    # the defined boundaries of the environment
        nrows = len(environment)
        ncols = len(environment[0])
        # Select a random starting point for the agents 
        self.x = random.randint(0, ncols-1)
        self.y = random.randint(0, nrows-1)
        # Set the environment for the agents, which they will eat
        self.environment = environment 
        # Set up a food store for all of the agents, which will be altered as they eat the environment
        self.store = 0
        # Set up an attribute used for sharing food with nearby neighbours
        self.agents = agents 
      
    # Move agents with a conditional statement 
    def move(self):
        if random.random() < 0.5:
            self.y = (self.y + 1) % 300 # If random number is <0.5, add 1 to y axis of agent
        else:
            self.y = (self.y - 1) % 300 # If random number >0.5, subtract 1 from y axis of agent 

        if random.random() <0.5:
            self.x = (self.x + 1) % 300 # If random number is <0.5, add 1 to x axis of agent 
        else:
            self.x = (self.x - 1) % 300 # If random number is >0.5, subtract 1 from x axis of agent

    # Defining eating patterns of agents
    def eat(self):
        # Set the agents to eat the environment when the environment's value is greater than 10
        if self.environment[self.y][self.x] > 100:
            self.environment[self.y][self.x] -= 100
            self.store += 10 
        else:
            # if the store is equal to the environment's value
            self.store += self.environment[self.y][self.x]  
            # deplete the environment's value so it equals 0
            self.environment[self.y][self.x] = 0
            
        #If self-stores (of food) become too big, make the agents puke it back into the environment
        if self.store>=10000:                               #if the self.stores are more than or equal to 10,000:
            self.environment[self.y][self.x] += 60          #add 60 back to the environment and;
            self.store=0     
    
    # Calculate distance between agents using pythagoras theorem   
    def distance_between(self, agent):
        return (((self.x - agent.x) **2) + ((self.y - agent.y)
                 **2))**0.5

    # Defining food sharing between nearby neighbours 
    def share(self, neighbourhood):
        # Create a for loop which searches for nearby agents
        for i in range(len(self.agents)):
            # Create a variable, dist, to store distances between each agent and nearby neighbours
            dist = self.distance_between(self.agents[i])
            # Use a conditional statement to test whether dist is within the neighbourhood
            # boundaries (set in the model)
            if dist <= neighbourhood:
                # If the agents are within a certain neighbourhood distance of one another,
                # Add the stores of both the agents
                sum = self.store + self.agents[i].store 
                # Find the average store between the nearby neighbours, by halving the store 
                #(using round to keep whole numbers)
                average = round(sum/2)
                # Test whether this works by printing
                print(self)
                print("Sharing with agent", i, "my store is", self.store, "their store is", self.agents[i].store)
                # Give each agent the average between the nearby neighbours
                self.store = average
                # Give the neighbouring agent the average store also
                self.agents[i].store = average


