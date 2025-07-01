package metodosnumerico.com;

import java.io.IOException;

import metodosnumerico.com.utils.Network;

public class App {
    public static void main(String[] args) throws IOException {
        Network network = new Network(100, 0.1, 0.05, 0.02, 0.5);
        network.infectRandomNode();
        network.simulate(50, "resultado.csv");
    }
}
