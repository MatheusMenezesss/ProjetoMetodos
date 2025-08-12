# analysis/plot_sirq.py

import pandas as pd
import matplotlib.pyplot as plt
from sir_quarentena import run_sirq_simulation

# Carregar e filtrar dados
df = pd.read_csv("/home/matheus-menezes/Documentos/ProjetoMetodos/projetometodos/outputs/resultados.csv")
df_steps = df[df['event_type'] == 'step']

# Permitir análise por run_id (experimento)
run_id = df_steps['run_id'].unique()[0]
df_run = df_steps[df_steps['run_id'] == run_id]

# Normalizar
N = df_run.iloc[0][['infected_count', 'susceptible_count', 'recovered_count']].sum()
df_norm = df_run[['infected_count', 'susceptible_count', 'recovered_count']] / N

# Parâmetros iniciais e do modelo
S0 = df_norm.iloc[0]['susceptible_count']
I0 = df_norm.iloc[0]['infected_count']
Q0 = 0.0
R0 = df_norm.iloc[0]['recovered_count']
beta = 0.5
gamma = 0.1
delta = 0.05
gamma_q = 0.2
dias = len(df_run)

# Rodar simulação
t, sol = run_sirq_simulation(S0, I0, Q0, R0, beta, gamma, delta, gamma_q, dias)
S, I, Q, R = sol.T

# Plotar
plt.figure(figsize=(10,6))
plt.plot(df_run['event_value'], df_norm['infected_count'], 'r--', label='Infectados (Java)')
plt.plot(t, I, 'r', label='Infectados (SIR-Q)')
plt.plot(t, Q, color='orange', label='Quarentenados (SIR-Q)')
plt.plot(t, S, 'b', label='Suscetíveis (SIR-Q)')
plt.plot(t, R, 'g', label='Recuperados (SIR-Q)')
plt.title("Modelo SIR com Quarentena vs Simulação Java")
plt.xlabel("Passos")
plt.ylabel("Proporção")
plt.legend()
plt.grid()
plt.tight_layout()
plt.savefig("grafico_sirq.png")
plt.show()
