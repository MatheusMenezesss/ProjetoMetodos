# analysis/sir_quarentena.py

import numpy as np
from scipy.integrate import odeint

def sirq_model(y, t, beta, gamma, delta, gamma_q):
    S, I, Q, R = y
    dSdt = -beta * S * I
    dIdt = beta * S * I - gamma * I - delta * I
    dQdt = delta * I - gamma_q * Q
    dRdt = gamma * I + gamma_q * Q
    return [dSdt, dIdt, dQdt, dRdt]

def run_sirq_simulation(S0, I0, Q0, R0, beta, gamma, delta, gamma_q, days):
    y0 = [S0, I0, Q0, R0]
    t = np.linspace(0, days - 1, days)
    sol = odeint(sirq_model, y0, t, args=(beta, gamma, delta, gamma_q))
    return t, sol
