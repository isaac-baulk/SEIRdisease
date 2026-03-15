import seir_sim
import matplotlib.pyplot as plt

sim = seir_sim.MCsim(100, 100, 1, 0.1, 0.005)

sim.populate_agents(0.95, 0.05, 250)

for _ in range(2000):
    sim.step()

plt.plot(sim.getHistoryS(), label='susceptible', color='blue')
plt.plot(sim.getHistoryE(), label='exposed', color='orange')
plt.plot(sim.getHistoryI(), label='infectious', color='red')
plt.plot(sim.getHistoryR(), label='recovered', color='green')

plt.title("monte carlo version of SEIR model")
plt.xlabel("monte carlo steps")
plt.ylabel("population")
plt.legend()
plt.show()