import seir_sim
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import numpy as np

def plot_populations(): 
    for _ in range(100): #run simulation steps
        sim.step()
        data = sim.getAgentCoordinates()

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
    data = np.array(sim.getAgentCoordinates())
    
    x_coords = data[:, 0]
    y_coords = data[:, 1]
    states = data[:, 2]
    
    scatter.set_offsets(np.c_[x_coords, y_coords])
    
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
    
    ani = animation.FuncAnimation(fig, update, frames=300, interval=50, fargs=[ax, scatter, color_map])

    plt.show()


grid_size = 100
sim = seir_sim.MCsim(grid_size, grid_size, 1, 1, 0.1)
sim.populate_agents(0.94, 0.05, 0.01, 30)

#create animation to track agents around the grid
track_agents(grid_size)

#uncomment to plot poulation sizes
plot_populations()