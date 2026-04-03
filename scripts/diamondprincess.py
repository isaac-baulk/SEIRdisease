import numpy as np
import matplotlib.pyplot as plt
import seir_sim
from ODE_model import odeSEIR

#data from Mizumoto, K., et al. (March 2020). Eurosurveillance, 25(10)
historical_days = np.arange(0, 15)
historical_cumulative = [10, 20, 61, 64, 70, 135, 174, 174, 218, 218, 285, 355, 454, 542, 621]

#simulation params --------------------------------------------------------------------------------------
N = 3711
beta = 0.44 #from Rocklöv, J., et al. (February 2020). Journal of Travel Medicine, 27(3).
sigma = 0.19 #from Li, Q., et al. (January 2020). The New England Journal of Medicine (NEJM).
gamma = 0.1 #from Rocklöv, J., et al.
reinfect = 0.0
days = 15

prop_exposed = 0.0269 #100 people initially exposed)
prop_infected = 0.00269 #10 initially infected
prop_susceptible = 1.0 - prop_exposed - prop_infected

#convert parameters from ODE model to suitable equivalents for mcsim model -----------------------------
steps_per_day = 100 #one step per hour
grid_size = 393 #393

p_gamma = gamma / steps_per_day #convert gamma to a probability for mcsim
p_sigma = sigma / steps_per_day #convert sigma to a probability for mcsim

pop_density = N/(grid_size*grid_size)
k = 8 * pop_density #avg number of nearest neighbours is 8 neighbours * population density

beta_mc = beta / (k*steps_per_day) #beta accounts for number of contacts that agents make per day

# MONTE CARLO METHOD --------------------------------------------------------------------------------------
mc_sim = seir_sim.MCsim(grid_size, grid_size, beta_mc, p_sigma, p_gamma, reinfect)
mc_sim.populate_agents(prop_susceptible, prop_exposed, prop_infected, N)

num_steps = steps_per_day * days
for _ in range(num_steps):
    mc_sim.step()

# ODE METHOD --------------------------------------------------------------------------------------
initial_exposed = prop_exposed * N
initial_infected = prop_infected * N

ode_sim = odeSEIR(N, beta, sigma, gamma)
ode_sim.solve(days, E0=initial_exposed, I0=initial_infected)

#cumulative cases --------------------------------------------------------------------------------------
ode_cumulative = ode_sim.I + ode_sim.R
mc_cumulative = np.array(mc_sim.getHistoryI()[::steps_per_day]) + np.array(mc_sim.getHistoryR()[::steps_per_day])

#plot --------------------------------------------------------------------------------------
plt.figure(figsize=(10, 6))

plt.plot(historical_days, historical_cumulative, 'ko', label='Historical data')
plt.plot(ode_sim.t, ode_cumulative, 'r-', label='ODE cumulative cases')
plt.plot(mc_cumulative, 'r--', label='MC cumulative cases')

plt.title("COVID-19 on the Diamond Princess")
plt.xlabel("Days since quarantine (5th Feb)")
plt.ylabel("Cumulative Cases")
plt.legend()
plt.show()