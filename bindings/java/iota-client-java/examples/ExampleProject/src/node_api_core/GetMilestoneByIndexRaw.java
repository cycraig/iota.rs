package node_api_core;

import org.apache.commons.codec.binary.Hex;
import org.iota.Client;
import org.iota.types.ClientConfig;
import org.iota.types.ClientException;

public class GetMilestoneByIndexRaw {
    public static void main(String[] args) throws ClientException {
        // Build the client.
        Client client = new Client(new ClientConfig().withNodes(new String[]{"https://api.testnet.shimmer.network"}));

        // Set up a milestone index for this example.
        int milestoneIndex = ExampleUtils.setUpMilestoneIndex(client);

        // Get the milestone bytes.
        byte[] milestoneBytes = client.getMilestoneByIndexRaw(milestoneIndex);

        // Print the milestone bytes.
        System.out.println(Hex.encodeHex(milestoneBytes));
    }
}