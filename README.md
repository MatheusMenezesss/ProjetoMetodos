# Simulação de Propagação de Malware em Rede Virtual (Java + Docker)

## Instalação

- Instale [Docker](https://docs.docker.com/get-docker/) e [Docker Compose](https://docs.docker.com/compose/install/).

## Como rodar

```bash
./run_simulation.sh 10 0.2 0.1 0.05 0.6
```

Os resultados estarão em `./outputs/resultados.csv`.

## Segurança

**Nenhum malware real é executado.**  
A simulação apenas modela o comportamento de propagação de forma benigna e isolada, sem risco ao sistema.

## Parâmetros

- NUM_NODES: número de nós simulados
- SCAN_RATE: taxa de varredura
- P_EXPLOIT: probabilidade de exploração
- PATCH_TIME: tempo de correção
- BACKUP_PROB: probabilidade de backup

## Rede

Todo o tráfego simulado é restrito à rede Docker `simnet`.



Relatório: 
