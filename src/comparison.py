import matplotlib.pyplot as plt
import seir_sim
from part1 import odeSEIR

N = 5000
beta = 0.5
sigma = 0.2
gamma = 0.1
days = 150
grid_size = 100
initial_exposed = 10

# --------- PART 2 METHOD -----------
mc_sim = seir_sim.MCsim(grid_size, grid_size, beta, sigma, gamma)
mc_sim.populate_agents(0.998, 0.002, N)

for _ in range(days):
    mc_sim.step()

# ------- PART 1 METHOD --------------
ode_sim = odeSEIR(N, beta, sigma, gamma)
ode_sim.solve(days, E0=initial_exposed, I0=0)

# ------- PLOT AND COMPARE ------------
plt.figure(figsize=(10, 6))

#PART 2
plt.plot(mc_sim.getHistoryS(), 'b--', alpha=0.5, label=' MC susceptible')
plt.plot(mc_sim.getHistoryE(), 'orange', linestyle='--', alpha=0.5, label='MC exposed')
plt.plot(mc_sim.getHistoryI(), 'r--', alpha=0.5, label='MC infectious')
plt.plot(mc_sim.getHistoryR(), 'g--', alpha=0.5, label='MC recovered')

#PART 1
plt.plot(ode_sim.t, ode_sim.S, 'b-', linewidth=2, label='ODE susceptible')
plt.plot(ode_sim.t, ode_sim.E, color='darkorange', linewidth=2, label='ODE exposed')
plt.plot(ode_sim.t, ode_sim.I, 'r-', linewidth=2, label='ODE infectious')
plt.plot(ode_sim.t, ode_sim.R, 'g-', linewidth=2, label='ODE recovered')

plt.title("SEIR model comparison: Monte Carlo vs ODE")
plt.xlabel("Time")
plt.ylabel("Population")
plt.legend(loc='center right', bbox_to_anchor=(1.25, 0.5))
plt.tight_layout()
plt.show()