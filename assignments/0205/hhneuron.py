from dataclasses import dataclass
import math


sim_config = {
    "step_size": 0.2,
    "n_steps": 100,
    "current": lambda t: math.sin(t)+1
}

constants = {
    "ena": 115,
    "gna": 120,
    "ek": -12,
    "gk": 36,
    "el": 10.6,
    "gl": 0.3
}

def alpha_n(V):
    return (0.01 * (10 - V)) / (math.exp((10-V)/10) - 1)
def alpha_m(V):
    return (0.1 * (25 - V)) / (math.exp((25-V)/10) - 1)
def alpha_h(V):
    return 0.07*(math.exp(-1*V / 80))


def beta_n(V):
    return 0.125*(math.exp(-1*V / 80))
def beta_m(V):
    return 4*(math.exp(-1*V / 18))
def beta_h(V):
    return 1/ (math.exp((30-V)/10) + 1)

@dataclass
class State:
    m: float
    n: float
    h: float
    I: float
    V: float = 0
    t: float = 0

    def dmdt(self):
        return alpha_m(self.V) * (1 - self.m) - beta_m(self.V) * self.m
    
    def dndt(self):
        return alpha_n(self.V) * (1 - self.n) - beta_n(self.V) * self.n
    
    def dhdt(self):
        return alpha_h(self.V) * (1 - self.h) - beta_h(self.V) * self.h
    
    def dvdt(self):
        term_na = constants["gna"] * (self.m ** 3) * (self.h) * (self.V - constants["ena"])
        term_k = constants["gk"] * (self.n ** 4) * (self.V - constants["ek"])
        term_l = constants["gl"] * (self.V - constants["el"])
        return self.I - (term_na + term_k + term_l)
    
    def step(self):
        dt = sim_config["step_size"]
        self.t += dt
        dv = self.dvdt() * dt
        dm = self.dmdt() * dt
        dn = self.dndt() * dt
        dh = self.dhdt() * dt
        self.V += dv
        self.m += dm
        self.n += dn
        self.h += dh
        self.I = sim_config["current"](self.t)

state = State(0, 0, 0, sim_config["current"](0))
T = []
V = []

for _ in range(sim_config["n_steps"]):
    T.append(state.t)
    V.append(state.V)
    print(state)
    state.step()

print(V)