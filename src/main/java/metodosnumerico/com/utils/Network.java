package metodosnumerico.com.utils;

import java.util.*;
import java.io.*;

public class Network {
    private List<Node> nodes;
    private double infectionRate;
    private double recoveryRate;
    private double backupRecoveryRate;
    private double backupProbability;

    public Network(int size, double infectionRate, double recoveryRate, double backupRecoveryRate, double backupProbability) {
        this.infectionRate = infectionRate;
        this.recoveryRate = recoveryRate;
        this.backupRecoveryRate = backupRecoveryRate;
        this.backupProbability = backupProbability;
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
            writer.write("Step,Susceptible,Infected,Recovered\n");
            for (int step = 0; step < steps; step++) {
                int susceptible = 0, infected = 0, recovered = 0;
                for (Node node : nodes) {
                    switch (node.getEstado()) {
                        case SUSCEPTIBLE: susceptible++; break;
                        case INFECTED: infected++; break;
                        case RECOVERED: recovered++; break;
                    }
                }
                writer.write(step + "," + susceptible + "," + infected + "," + recovered + "\n");
                step();
            }
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
}

