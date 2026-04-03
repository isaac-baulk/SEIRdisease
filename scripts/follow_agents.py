import seir_sim
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import numpy as np

def plot_populations(): 
    for _ in range(500): #run simulation steps
        sim.step()
        data = sim.getAgentCoordinates()

    #plot compoartment histories
    plt.plot(sim.getHistoryS(), label='susceptible', color='blue')
    plt.plot(sim.getHistoryE(), label='exposed', color='orange')
    plt.plot(sim.getHistoryI(), label='infectious', color='red')
    plt.plot(sim.getHistoryR(), label='recovered', color='green')

    plt.title("monte carlo version of SEIR model")
    plt.xlabel("monte carlo steps")
    plt.ylabel("population")
    plt.legend()
    plt.show()

def update(frame, ax, scatter, color_map):
    sim.step()

    #get all positions of all agents
    data = np.array(sim.getAgentCoordinates())
    
    #extract coordinates and states
    x_coords = data[:, 0]
    y_coords = data[:, 1]
    states = data[:, 2]
    
    #update x and y without redrawing the entire grid
    scatter.set_offsets(np.c_[x_coords, y_coords])
    
    #apply colour map
    colors = [color_map[state] for state in states]
    scatter.set_color(colors)
    
    ax.set_title(f"seir model - step: {frame}")
    return scatter,

def track_agents(grid_size):
    fig, ax = plt.subplots(figsize=(8, 8))
    ax.set_xlim(0, grid_size)
    ax.set_ylim(0, grid_size)
    ax.set_title("agent tracking")

    scatter = ax.scatter([], [], s=10)
    color_map = {
        0: 'blue',
        1: 'orange',
        2: 'red',
        3: 'green'
    }
    
    ani = animation.FuncAnimation(fig, update, frames=500, interval=30, fargs=[ax, scatter, color_map])

    plt.show()


#set parameters ----------------------------------------------------------------
grid_size = 100
beta = 0.4
sigma = 1
gamma = 0.1
prop_sus = 0.94
prop_exp = 0.05
prop_inf = 0.01
N = 8000

pop_density = N/(grid_size*grid_size)
k = 8 * pop_density #avg number of nearest neighbours is 8 neighbours * population density
beta = beta / k #beta accounts for number of contacts that agents make per step

#set up sim ----------------------------------------------------------------
sim = seir_sim.MCsim(grid_size, grid_size, beta, sigma, gamma)
sim.populate_agents(prop_sus, prop_exp, prop_inf, N)

#create animation to track agents around the grid
track_agents(grid_size)

#uncomment to plot poulation sizes
plot_populations()