# analysis/plot_sir_interv.py

import pandas as pd
import matplotlib.pyplot as plt
from sir_intervencao import run_sir_interv_simulation, beta_func, gamma_func

# Carregar e filtrar dados
df = pd.read_csv("/home/matheus-menezes/Documentos/ProjetoMetodos/projetometodos/outputs/resultados.csv")
df_steps = df[df['event_type'] == 'step']

# Permitir análise por run_id (experimento)
run_id = df_steps['run_id'].unique()[0]
df_run = df_steps[df_steps['run_id'] == run_id]

# Normalizar
N = df_run.iloc[0][['infected_count', 'susceptible_count', 'recovered_count']].sum()
df_norm = df_run[['infected_count', 'susceptible_count', 'recovered_count']] / N

# Parâmetros iniciais
S0 = df_norm.iloc[0]['susceptible_count']
I0 = df_norm.iloc[0]['infected_count']
R0 = df_norm.iloc[0]['recovered_count']
dias = len(df_run)

# Simulação com beta(t) e gamma(t)
t, sol = run_sir_interv_simulation(S0, I0, R0, beta_func, gamma_func, dias)
S, I, R = sol.T

# Plot
plt.figure(figsize=(10,6))
plt.plot(df_run['event_value'], df_norm['infected_count'], 'r--', label='Infectados (Java)')
plt.plot(t, I, 'r', label='Infectados (SIR c/ Intervenção)')
plt.plot(t, S, 'b', label='Suscetíveis (SIR c/ Intervenção)')
plt.plot(t, R, 'g', label='Recuperados (SIR c/ Intervenção)')
plt.title("Modelo SIR com Intervenção Dinâmica vs Simulação Java")
plt.xlabel("Passos")
plt.ylabel("Proporção")
plt.legend()
plt.grid()
plt.tight_layout()
plt.savefig("grafico_sir_interv.png")
