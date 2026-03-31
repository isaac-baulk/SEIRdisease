import matplotlib.pyplot as plt
import seir_sim
from ODE_model import odeSEIR

# sim parameters --------------------------------------------------------------------------------------
N = 1000
beta = 0.4
sigma = 1
gamma = 0.1
days = 30

prop_exposed = 0.05
prop_infected = 0.01
prop_susceptible = 1.0 - prop_exposed - prop_infected

#convert parameters from ODE model to suitable equivalents for mcsim model
steps_per_day = 20
grid_size = 100

p_gamma = gamma / steps_per_day #convert gamma to a probability for mcsim
p_sigma = sigma / steps_per_day #convert sigma to a probability for mcsim

pop_density = N/(grid_size*grid_size)
k = 8 * pop_density #avg number of nearest neighbours is 8 neighbours * population density
beta_mc = beta / (k*steps_per_day) #beta accounts for number of contacts that agents make per day

# MONTE CARLO METHOD --------------------------------------------------------------------------------------
mc_sim = seir_sim.MCsim(grid_size, grid_size, beta_mc, p_sigma, p_gamma)
mc_sim.populate_agents(prop_susceptible, prop_exposed, prop_infected, N)

num_steps = steps_per_day * days
for _ in range(num_steps):
    mc_sim.step()

# ODE METHOD --------------------------------------------------------------------------------------
initial_exposed = prop_exposed * N
initial_infected = prop_infected * N

ode_sim = odeSEIR(N, beta, sigma, gamma)
ode_sim.solve(days, E0=initial_exposed, I0=initial_infected)

# PLOT AND COMPARE --------------------------------------------------------------------------------------
R_factor = beta / gamma
print(f'R factor for this epidemic: {R_factor}')

plt.figure(figsize=(10, 6))

# MONTE CARLO - slicing data so that only ODE relevant steps are plotted -------------------------------------------
plt.plot(mc_sim.getHistoryS()[::steps_per_day], 'b--', alpha=0.5, label=' MC susceptible')
plt.plot(mc_sim.getHistoryE()[::steps_per_day], 'orange', linestyle='--', alpha=0.5, label='MC exposed')
plt.plot(mc_sim.getHistoryI()[::steps_per_day], 'r--', alpha=0.5, label='MC infectious')
plt.plot(mc_sim.getHistoryR()[::steps_per_day], 'g--', alpha=0.5, label='MC recovered')

# ODE --------------------------------------------------------------------------------------
plt.plot(ode_sim.t, ode_sim.S, 'b-', linewidth=2, label='ODE susceptible')
plt.plot(ode_sim.t, ode_sim.E, color='darkorange', linewidth=2, label='ODE exposed')
plt.plot(ode_sim.t, ode_sim.I, 'r-', linewidth=2, label='ODE infectious')
plt.plot(ode_sim.t, ode_sim.R, 'g-', linewidth=2, label='ODE recovered')

# FORMATTING
plt.title("SEIR model comparison: Monte Carlo vs ODE")
plt.xlabel("Time")
plt.ylabel("Population")
plt.legend(loc='center right', bbox_to_anchor=(1.25, 0.5))
plt.tight_layout()
plt.show()