package metodosnumerico.com.utils;

import java.util.ArrayList;
import java.util.List;
import java.util.UUID;

public class Node {
    private Estados estado;
    private BancoDeDados banco;
    private List<Node> vizinhos;

    public Node(boolean possuiBackup) {
        this.estado = Estados.SUSCEPTIBLE;
        this.banco = new BancoDeDados(possuiBackup);
        this.vizinhos = new ArrayList<>();
    }

    public void addVizinho(Node vizinho) {
        this.vizinhos.add(vizinho);
    }

    public List<Node> getVizinhos() {
        return vizinhos;
    }

    public Estados getEstado() {
        return estado;
    }

    public BancoDeDados getBanco() {
        return banco;
    }

    public void infectar() {
        if (estado == Estados.SUSCEPTIBLE) {
            estado = Estados.INFECTED;
            banco.criptografar(UUID.randomUUID().toString());
        }
    }

    public void recuperar() {
        if (estado == Estados.INFECTED) {
            estado = Estados.RECOVERED;
            banco.descriptografar();
        }
    }
}
