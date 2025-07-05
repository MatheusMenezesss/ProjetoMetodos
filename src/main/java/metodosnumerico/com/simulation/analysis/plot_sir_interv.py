# analysis/plot_sir_interv.py

import pandas as pd
import matplotlib.pyplot as plt
from sir_intervencao import run_sir_interv_simulation, beta_func, gamma_func

# Carregar e normalizar dados
df = pd.read_csv("/home/matheus-menezes/Documentos/ProjetoMetodos/projetometodos/resultado.csv")
N = df[['Susceptible', 'Infected', 'Recovered']].iloc[0].sum()
df_norm = df[['Susceptible', 'Infected', 'Recovered']] / N

# Parâmetros iniciais
S0 = df_norm.loc[0, 'Susceptible']
I0 = df_norm.loc[0, 'Infected']
R0 = df_norm.loc[0, 'Recovered']
dias = len(df)

# Simulação com beta(t) e gamma(t)
t, sol = run_sir_interv_simulation(S0, I0, R0, beta_func, gamma_func, dias)
S, I, R = sol.T

# Plot
plt.figure(figsize=(10,6))
plt.plot(df['Step'], df_norm['Infected'], 'r--', label='Infectados (Java)')
plt.plot(t, I, 'r', label='Infectados (SIR c/ Intervenção)')
plt.plot(t, S, 'b', label='Suscetíveis (SIR c/ Intervenção)')
plt.plot(t, R, 'g', label='Recuperados (SIR c/ Intervenção)')
plt.title("Modelo SIR com Intervenção Dinâmica vs Simulação Java")
plt.xlabel("Dias")
plt.ylabel("Proporção")
plt.legend()
plt.grid()
plt.tight_layout()
plt.savefig("grafico_sir_interv.png")
plt.show()
