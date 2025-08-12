# analysis/sir_vacinacao.py

import numpy as np
from scipy.integrate import odeint

def sirv_model(y, t, beta, gamma, nu):
    S, I, V, R = y
    dSdt = -beta * S * I - nu * S
    dIdt = beta * S * I - gamma * I
    dVdt = nu * S
    dRdt = gamma * I
    return [dSdt, dIdt, dVdt, dRdt]

def run_sirv_simulation(S0, I0, V0, R0, beta, gamma, nu, days):
    y0 = [S0, I0, V0, R0]
    t = np.linspace(0, days - 1, days)
    sol = odeint(sirv_model, y0, t, args=(beta, gamma, nu))
    return t, sol
