# analysis/sir_intervencao.py

import numpy as np
from scipy.integrate import odeint

def sir_interv_model(y, t, beta_func, gamma_func):
    S, I, R = y
    beta = beta_func(t)
    gamma = gamma_func(t)
    dSdt = -beta * S * I
    dIdt = beta * S * I - gamma * I
    dRdt = gamma * I
    return [dSdt, dIdt, dRdt]

def run_sir_interv_simulation(S0, I0, R0, beta_func, gamma_func, days):
    y0 = [S0, I0, R0]
    t = np.linspace(0, days - 1, days)
    sol = odeint(sir_interv_model, y0, t, args=(beta_func, gamma_func))
    return t, sol

# Exemplo de função beta(t) e gamma(t)
def beta_func(t):
    # Redução da infecção após o dia 20 (intervenção)
    return 0.5 if t < 20 else 0.2

def gamma_func(t):
    # Aumento da recuperação após o dia 30
    return 0.1 if t < 30 else 0.3
