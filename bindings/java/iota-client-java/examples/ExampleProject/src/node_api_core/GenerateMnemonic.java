package node_api_core;

import org.iota.Client;
import org.iota.types.ClientConfig;
import org.iota.types.ClientException;

public class GenerateMnemonic {
    public static void main(String[] args) throws ClientException {
        // Build the client.
        Client client = new Client(new ClientConfig().withNodes(new String[]{"https://api.testnet.shimmer.network"}));

        // Generate a mnemonic.
        String mnemonic = client.generateMnemonic();

        // Print the mnemonic.
        System.out.println(mnemonic);
    }
}