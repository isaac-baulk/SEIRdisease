import seir_sim
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import numpy as np
from validation_methods import get_inputs

def plot_populations(sim, simulation_steps): 
    for _ in range(simulation_steps): #run simulation steps
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

def update(frame, ax, scatter, color_map, sim):
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

def track_agents(sim, grid_size, simulation_steps):

    #initialise plot
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
    
    #animation object
    ani = animation.FuncAnimation(fig, update, frames=simulation_steps, interval=30, fargs=[ax, scatter, color_map, sim])

    plt.show()
 
def main():
    #get user inputs using validation function
    param_results, N, beta_mc, grid_size, days = get_inputs()

    #unpack results
    simulation_steps = days * 20
    sigma = param_results['sigma']
    gamma = param_results['gamma']
    reinfect = param_results['reinfect']
    prop_exp = param_results['prop_exp']
    prop_inf = param_results['prop_inf']

    #set up sim ----------------------------------------------------------------
    sim = seir_sim.MCsim(grid_size, grid_size, beta_mc, sigma, gamma, reinfect)
    print('Simulating agents')
    sim.populate_agents(prop_exp, prop_inf, N)

    #create animation to track agents around the grid
    track_agents(sim, grid_size, simulation_steps)

    #plot poulation sizes
    print('Plotting populations')
    plot_populations(sim, simulation_steps)

main()