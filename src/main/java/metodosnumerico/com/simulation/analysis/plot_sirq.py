# analysis/plot_sirq.py

import pandas as pd
import matplotlib.pyplot as plt
from sir_quarentena import run_sirq_simulation

# Carregar e normalizar dados
df = pd.read_csv("/home/matheus-menezes/Documentos/ProjetoMetodos/projetometodos/resultado.csv")
N = df[['Susceptible', 'Infected', 'Recovered']].iloc[0].sum()
df_norm = df[['Susceptible', 'Infected', 'Recovered']] / N

# Parâmetros iniciais e do modelo
S0 = df_norm.loc[0, 'Susceptible']
I0 = df_norm.loc[0, 'Infected']
Q0 = 0.0
R0 = df_norm.loc[0, 'Recovered']
beta = 0.5
gamma = 0.1
delta = 0.05
gamma_q = 0.2
dias = len(df)

# Rodar simulação
t, sol = run_sirq_simulation(S0, I0, Q0, R0, beta, gamma, delta, gamma_q, dias)
S, I, Q, R = sol.T

# Plotar
plt.figure(figsize=(10,6))
plt.plot(df['Step'], df_norm['Infected'], 'r--', label='Infectados (Java)')
plt.plot(t, I, 'r', label='Infectados (SIR-Q)')
plt.plot(t, Q, 'orange', label='Quarentenados (SIR-Q)')
plt.plot(t, S, 'b', label='Suscetíveis (SIR-Q)')
plt.plot(t, R, 'g', label='Recuperados (SIR-Q)')
plt.title("Modelo SIR com Quarentena vs Simulação Java")
plt.xlabel("Dias")
plt.ylabel("Proporção")
plt.legend()
plt.grid()
plt.tight_layout()
plt.savefig("grafico_sirq.png")
plt.show()
