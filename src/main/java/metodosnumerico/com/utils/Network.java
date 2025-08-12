package metodosnumerico.com.utils;

import java.io.BufferedWriter;
import java.io.FileWriter;
import java.io.IOException;
import java.util.ArrayList;
import java.util.List;
import java.util.Random;

public class Network {
    private List<Node> nodes;
    private double infectionRate;
    private double recoveryRate;
    private double backupRecoveryRate;
    private double backupProbability;
    private String hostId;
    private String runId;

    public Network(int size, double infectionRate, double recoveryRate, double backupRecoveryRate, double backupProbability, String hostId, String runId) {
        this.infectionRate = infectionRate;
        this.recoveryRate = recoveryRate;
        this.backupRecoveryRate = backupRecoveryRate;
        this.backupProbability = backupProbability;
        this.hostId = hostId;
        this.runId = runId;
        nodes = new ArrayList<>();
        for (int i = 0; i < size; i++) {
            nodes.add(new Node(Math.random() < backupProbability));
        }
        // Conexão simples: cada nó é vizinho dos dois próximos (circular)
        for (int i = 0; i < size; i++) {
            nodes.get(i).addVizinho(nodes.get((i + 1) % size));
            nodes.get(i).addVizinho(nodes.get((i + size - 1) % size));
        }
    }

    public void infectRandomNode() {
        Random rand = new Random();
        nodes.get(rand.nextInt(nodes.size())).infectar();
    }

    public void simulate(int steps, String outputFile) throws IOException {
        try (BufferedWriter writer = new BufferedWriter(new FileWriter(outputFile))) {
            writer.write("run_id,timestamp,host_id,event_type,event_value,infected_count,susceptible_count,recovered_count\n");
            for (int step = 0; step < steps; step++) {
                int susceptible = 0, infected = 0, recovered = 0;
                int newInfections = 0, newRecoveries = 0;
                for (Node node : nodes) {
                    switch (node.getEstado()) {
                        case SUSCEPTIBLE: susceptible++; break;
                        case INFECTED: infected++; break;
                        case RECOVERED: recovered++; break;
                    }
                }
                long timestamp = System.currentTimeMillis();
                writer.write(runId + "," + timestamp + "," + hostId + ",step," + step + "," +
                             infected + "," + susceptible + "," + recovered + "\n");
                step();
            }
            // Métricas agregadas finais
            writer.write(runId + "," + System.currentTimeMillis() + "," + hostId + ",summary,final,"
                         + getInfectedCount() + "," + getSusceptibleCount() + "," + getRecoveredCount() + "\n");
        }
    }

    private void step() {
        List<Node> toInfect = new ArrayList<>();
        List<Node> toRecover = new ArrayList<>();
        for (Node node : nodes) {
            if (node.getEstado() == Estados.INFECTED) {
                for (Node vizinho : node.getVizinhos()) {
                    if (vizinho.getEstado() == Estados.SUSCEPTIBLE && Math.random() < infectionRate) {
                        toInfect.add(vizinho);
                    }
                }
                if (Math.random() < (node.getBanco().possuiBackup() ? backupRecoveryRate : recoveryRate)) {
                    toRecover.add(node);
                }
            }
        }
        for (Node node : toInfect) node.infectar();
        for (Node node : toRecover) node.recuperar();
    }

    public int getInfectedCount() {
        int count = 0;
        for (Node node : nodes) {
            if (node.getEstado() == Estados.INFECTED) {
                count++;
            }
        }
        return count;
    }

    public int getSusceptibleCount() {
        int count = 0;
        for (Node node : nodes) {
            if (node.getEstado() == Estados.SUSCEPTIBLE) {
                count++;
            }
        }
        return count;
    }

    public int getRecoveredCount() {
        int count = 0;
        for (Node node : nodes) {
            if (node.getEstado() == Estados.RECOVERED) {
                count++;
            }
        }
        return count;
    }
}

