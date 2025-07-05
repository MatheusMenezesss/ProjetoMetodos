# analysis/sir_model.py

import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt

def sir_model(y, t, beta, gamma):
    S, I, R = y
    dSdt = -beta * S * I
    dIdt = beta * S * I - gamma * I
    dRdt = gamma * I
    return [dSdt, dIdt, dRdt]

def run_sir_simulation(S0, I0, R0, beta, gamma, days):
    y0 = [S0, I0, R0]
    t = np.linspace(0, days - 1, days)
    sol = odeint(sir_model, y0, t, args=(beta, gamma))
    return t, sol
