# analysis/plot_simulation.py

import pandas as pd
import matplotlib.pyplot as plt
from sir_model import run_sir_simulation

# Carregar CSV
df = pd.read_csv("/home/matheus-menezes/Documentos/ProjetoMetodos/projetometodos/outputs/resultados.csv")

# Filtrar apenas eventos de passo
df_steps = df[df['event_type'] == 'step']

# Permitir análise por run_id ou host_id
run_id = df_steps['run_id'].unique()[0]  # escolha o primeiro experimento
df_run = df_steps[df_steps['run_id'] == run_id]

# Normalizar
total_nodes = df_run.iloc[0][['infected_count', 'susceptible_count', 'recovered_count']].sum()
df_norm = df_run[['infected_count', 'susceptible_count', 'recovered_count']] / total_nodes

# Parâmetros do modelo SIR
beta = 0.5
gamma = 0.1
S0 = df_norm.iloc[0]['susceptible_count']
I0 = df_norm.iloc[0]['infected_count']
R0 = df_norm.iloc[0]['recovered_count']

t, sir_sim = run_sir_simulation(S0, I0, R0, beta, gamma, len(df_run))

# Plot
plt.figure(figsize=(10,6))
plt.plot(df_run['event_value'], df_norm['susceptible_count'], 'b--', label='Susc. (Simulação Java)')
plt.plot(df_run['event_value'], df_norm['infected_count'], 'r--', label='Infec. (Simulação Java)')
plt.plot(df_run['event_value'], df_norm['recovered_count'], 'g--', label='Recup. (Simulação Java)')

plt.plot(t, sir_sim[:,0], 'b', label='Susc. (SIR)')
plt.plot(t, sir_sim[:,1], 'r', label='Infec. (SIR)')
plt.plot(t, sir_sim[:,2], 'g', label='Recup. (SIR)')

plt.xlabel("Passos")
plt.ylabel("Proporção")
plt.legend()
plt.grid()
plt.title("Comparação entre Simulação Java e Modelo SIR")
plt.tight_layout()
plt.savefig("grafico_simulacao.png")
plt.show()
