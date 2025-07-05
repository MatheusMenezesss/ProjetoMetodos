# analysis/plot_simulation.py

import pandas as pd
import matplotlib.pyplot as plt
from sir_model import run_sir_simulation

# Carregar CSV gerado pelo Java
df = pd.read_csv("/home/matheus-menezes/Documentos/ProjetoMetodos/projetometodos/resultado.csv")

# Normalizar os dados
total_nodes = df.loc[0, ['Susceptible', 'Infected', 'Recovered']].sum()
df_norm = df[['Susceptible', 'Infected', 'Recovered']] / total_nodes

# Parâmetros do modelo SIR
beta = 0.5  # taxa de infecção
gamma = 0.1  # taxa de recuperação
S0 = df_norm.loc[0, 'Susceptible']
I0 = df_norm.loc[0, 'Infected']
R0 = df_norm.loc[0, 'Recovered']

# Simulação com EDO
t, sir_sim = run_sir_simulation(S0, I0, R0, beta, gamma, len(df))

# Plot
plt.figure(figsize=(10,6))
plt.plot(df['Step'], df_norm['Susceptible'], 'b--', label='Susc. (Simulação Java)')
plt.plot(df['Step'], df_norm['Infected'], 'r--', label='Infec. (Simulação Java)')
plt.plot(df['Step'], df_norm['Recovered'], 'g--', label='Recup. (Simulação Java)')

plt.plot(t, sir_sim[:,0], 'b', label='Susc. (SIR)')
plt.plot(t, sir_sim[:,1], 'r', label='Infec. (SIR)')
plt.plot(t, sir_sim[:,2], 'g', label='Recup. (SIR)')

plt.xlabel("Dias")
plt.ylabel("Proporção")
plt.legend()
plt.grid()
plt.title("Comparação entre Simulação Java e Modelo SIR")
plt.tight_layout()
plt.savefig("grafico_simulacao.png")
plt.show()
