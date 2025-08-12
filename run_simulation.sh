#!/bin/bash

NUM_NODES=${1:-5}
SCAN_RATE=${2:-0.1}
P_EXPLOIT=${3:-0.05}
PATCH_TIME=${4:-0.02}
BACKUP_PROB=${5:-0.5}

cat <<EOF > .env
NUM_NODES=$NUM_NODES
SCAN_RATE=$SCAN_RATE
P_EXPLOIT=$P_EXPLOIT
PATCH_TIME=$PATCH_TIME
BACKUP_PROB=$BACKUP_PROB
HOST_ID=$(uuidgen)
EOF

docker-compose up --build --scale node=$NUM_NODES

mkdir -p outputs
#cp /app/outputs/resultados.csv ./outputs/