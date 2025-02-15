# Interface: IClientOptions

Options for the client builder

## Table of contents

### Properties

- [offline](IClientOptions.md#offline)
- [primaryNode](IClientOptions.md#primarynode)
- [primaryPowNode](IClientOptions.md#primarypownode)
- [nodeSyncEnabled](IClientOptions.md#nodesyncenabled)
- [nodeSyncInterval](IClientOptions.md#nodesyncinterval)
- [quorum](IClientOptions.md#quorum)
- [minQuorumSize](IClientOptions.md#minquorumsize)
- [quorumThreshold](IClientOptions.md#quorumthreshold)
- [networkInfo](IClientOptions.md#networkinfo)
- [brokerOptions](IClientOptions.md#brokeroptions)
- [apiTimeout](IClientOptions.md#apitimeout)
- [remotePowTimeout](IClientOptions.md#remotepowtimeout)
- [powWorkerCount](IClientOptions.md#powworkercount)
- [localPow](IClientOptions.md#localpow)

## Properties

### offline

• `Optional` **offline**: `boolean`

If the Client should be able to use without a node connection

___

### primaryNode

• `Optional` **primaryNode**: `string` \| [`INode`](INode.md)

Node which will be tried first for all requests

___

### primaryPowNode

• `Optional` **primaryPowNode**: `string` \| [`INode`](INode.md)

Node which will be tried first when using remote PoW, even before the primary_node

___

### nodeSyncEnabled

• `Optional` **nodeSyncEnabled**: `boolean`

If node syncing is enabled

___

### nodeSyncInterval

• `Optional` **nodeSyncInterval**: [`IDuration`](IDuration.md)

Interval in which nodes will be checked for their sync status and the NetworkInfo gets updated

___

### quorum

• `Optional` **quorum**: `boolean`

If node quorum is enabled. Will compare the responses from multiple nodes and only returns the
response if quorum_threshold of the nodes return the same one

___

### minQuorumSize

• `Optional` **minQuorumSize**: `number`

Minimum amount of nodes required for request when quorum is enabled

___

### quorumThreshold

• `Optional` **quorumThreshold**: `number`

% of nodes that have to return the same response so it gets accepted

___

### networkInfo

• `Optional` **networkInfo**: [`INetworkInfo`](INetworkInfo.md)

Data related to the used network

___

### brokerOptions

• `Optional` **brokerOptions**: [`IMqttBrokerOptions`](IMqttBrokerOptions.md)

Options for the MQTT broker

___

### apiTimeout

• `Optional` **apiTimeout**: [`IDuration`](IDuration.md)

Timeout for API requests

___

### remotePowTimeout

• `Optional` **remotePowTimeout**: [`IDuration`](IDuration.md)

Timeout when sending a block that requires remote proof of work

___

### powWorkerCount

• `Optional` **powWorkerCount**: `number`

The amount of threads to be used for proof of work

___

### localPow

• `Optional` **localPow**: `boolean`

Whether the PoW should be done locally or remotely.
