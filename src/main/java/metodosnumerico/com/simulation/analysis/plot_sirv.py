# analysis/plot_sirv.py

import pandas as pd
import matplotlib.pyplot as plt
from sir_vacinacao import run_sirv_simulation

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
V0 = 0.0
R0 = df_norm.iloc[0]['recovered_count']
beta = 0.5
gamma = 0.1
nu = 0.05  # taxa de vacinação
dias = len(df_run)

# Simulação
t, sol = run_sirv_simulation(S0, I0, V0, R0, beta, gamma, nu, dias)
S, I, V, R = sol.T

# Plot
plt.figure(figsize=(10,6))
plt.plot(df_run['event_value'], df_norm['infected_count'], 'r--', label='Infectados (Java)')
plt.plot(t, I, 'r', label='Infectados (SIR-V)')
plt.plot(t, V, 'purple', label='Vacinados (SIR-V)')
plt.plot(t, S, 'b', label='Suscetíveis (SIR-V)')
plt.plot(t, R, 'g', label='Recuperados (SIR-V)')
plt.title("Modelo SIR com Vacinação vs Simulação Java")
plt.xlabel("Passos")
plt.ylabel("Proporção")
plt.legend()
plt.grid()
plt.tight_layout()
plt.savefig("grafico_sirv.png")
plt.show()
