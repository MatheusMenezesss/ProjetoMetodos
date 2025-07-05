# analysis/plot_sirv.py

import pandas as pd
import matplotlib.pyplot as plt
from sir_vacinacao import run_sirv_simulation

# Carregar e normalizar dados
df = pd.read_csv("/home/matheus-menezes/Documentos/ProjetoMetodos/projetometodos/resultado.csv")
N = df[['Susceptible', 'Infected', 'Recovered']].iloc[0].sum()
df_norm = df[['Susceptible', 'Infected', 'Recovered']] / N

# Parâmetros
S0 = df_norm.loc[0, 'Susceptible']
I0 = df_norm.loc[0, 'Infected']
V0 = 0.0
R0 = df_norm.loc[0, 'Recovered']
beta = 0.5
gamma = 0.1
nu = 0.05  # taxa de vacinação
dias = len(df)

# Simulação
t, sol = run_sirv_simulation(S0, I0, V0, R0, beta, gamma, nu, dias)
S, I, V, R = sol.T

# Plot
plt.figure(figsize=(10,6))
plt.plot(df['Step'], df_norm['Infected'], 'r--', label='Infectados (Java)')
plt.plot(t, I, 'r', label='Infectados (SIR-V)')
plt.plot(t, V, 'purple', label='Vacinados (SIR-V)')
plt.plot(t, S, 'b', label='Suscetíveis (SIR-V)')
plt.plot(t, R, 'g', label='Recuperados (SIR-V)')
plt.title("Modelo SIR com Vacinação vs Simulação Java")
plt.xlabel("Dias")
plt.ylabel("Proporção")
plt.legend()
plt.grid()
plt.tight_layout()
plt.savefig("grafico_sirv.png")
plt.show()
