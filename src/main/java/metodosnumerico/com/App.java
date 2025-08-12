package metodosnumerico.com;

import java.io.IOException;
import java.time.Instant;
import java.util.UUID;
import metodosnumerico.com.utils.Network;

public class App {
    public static void main(String[] args) throws IOException {
        int numNodes = Integer.parseInt(System.getenv().getOrDefault("NUM_NODES", "100"));
        double scanRate = Double.parseDouble(System.getenv().getOrDefault("SCAN_RATE", "0.1"));
        double pExploit = Double.parseDouble(System.getenv().getOrDefault("P_EXPLOIT", "0.05"));
        double patchTime = Double.parseDouble(System.getenv().getOrDefault("PATCH_TIME", "0.02"));
        double backupProb = Double.parseDouble(System.getenv().getOrDefault("BACKUP_PROB", "0.5"));
        String hostId = System.getenv().getOrDefault("HOST_ID", UUID.randomUUID().toString());
        String runId = Instant.now().toEpochMilli() + "-" + UUID.randomUUID();

        Network network = new Network(numNodes, scanRate, pExploit, patchTime, backupProb, hostId, runId);
        network.infectRandomNode();
        network.simulate(50, "outputs/resultados.csv");
    }
}
