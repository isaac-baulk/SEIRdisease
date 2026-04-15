import matplotlib.pyplot as plt
import seir_sim
from ODE_model import odeSEIR
from validation_methods import get_inputs

def main():
    
    #use validation method to get user inputs
    param_results, N, beta_mc, grid_size, days = get_inputs()

    #unpack parameters
    beta = param_results['beta']
    sigma = param_results['sigma']
    gamma = param_results['gamma']
    reinfect = param_results['reinfect']
    prop_exp = param_results['prop_exp']
    prop_inf = param_results['prop_inf']

    #calculate number of steps for MC simulation
    steps_per_day = 20
    simulation_steps = steps_per_day * days

    p_gamma = gamma / steps_per_day #convert gamma to a probability for mcsim
    p_sigma = sigma / steps_per_day #convert sigma to a probability for mcsim


    # MONTE CARLO METHOD --------------------------------------------------------------------------------------
    mc_sim = seir_sim.MCsim(grid_size, grid_size, beta_mc, p_sigma, p_gamma, reinfect)
    mc_sim.populate_agents(prop_exp, prop_inf, N)

    for _ in range(simulation_steps):
        mc_sim.step()

    # ODE METHOD --------------------------------------------------------------------------------------
    initial_exposed = prop_exp * N
    initial_infected = prop_inf * N

    ode_sim = odeSEIR(N, beta, sigma, gamma)
    ode_sim.solve(days, E0=initial_exposed, I0=initial_infected)

    # PLOT AND COMPARE --------------------------------------------------------------------------------------
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
    plt.xlabel("Days")
    plt.ylabel("Population")
    plt.legend(loc='center right', bbox_to_anchor=(1.25, 0.5))
    plt.tight_layout()
    plt.show()

    #calculate R factor
    R_factor = beta / gamma
    print(f'R factor for this epidemic: {R_factor}')

main()