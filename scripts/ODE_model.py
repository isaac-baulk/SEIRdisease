import numpy as np
from scipy.integrate import solve_ivp

class odeSEIR:
    def __init__(self, N, beta, sigma, gamma):
        self.N = N
        self.beta = beta
        self.sigma = sigma
        self.gamma = gamma
        
        self.t = None
        self.S = None
        self.E = None
        self.I = None
        self.R = None

    def _derivatives(self, t, y): #this is a 'private' method
        S, E, I, R = y
        
        #equations governing SEIR
        dSdt = -self.beta * S * I / self.N
        dEdt = self.beta * S * I / self.N - self.sigma * E
        dIdt = self.sigma * E - self.gamma * I
        dRdt = self.gamma * I
        
        return [dSdt, dEdt, dIdt, dRdt]

    def solve(self, days, E0, I0, R0=0):
        S0 = self.N - E0 - I0 - R0 #number of susceptible agents
        y0 = [S0, E0, I0, R0] #number of agents in each state
        
        t_span = (0, days)
        t_eval = np.linspace(0, days, days) #timestep array
        
        #use Runge-Kutta-Fehlberg method to solve ODEs
        solution = solve_ivp(self._derivatives, t_span, y0, t_eval=t_eval, method='RK45')
        
        #store results
        self.t = solution.t
        self.S = solution.y[0]
        self.E = solution.y[1]
        self.I = solution.y[2]
        self.R = solution.y[3]

