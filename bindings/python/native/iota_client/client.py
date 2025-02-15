import iota_client
from iota_client._node_core_api import NodeCoreAPI
from iota_client._node_indexer_api import NodeIndexerAPI
from iota_client._high_level_api import HighLevelAPI
from iota_client._utils import Utils
from json import dumps


class IotaClient(NodeCoreAPI, NodeIndexerAPI, HighLevelAPI, Utils):
    def __init__(self, client_config=None):
        """Initialize the IOTA Client.
        """
        if client_config:
            client_config = dumps(client_config)

        # Create the message handler
        self.handle = iota_client.create_message_handler(client_config)

    def get_handle(self):
        return self.handle

    def build_alias_output(self,
                           alias_id,
                           unlock_conditions,
                           amount=None,
                           native_tokens=None,
                           state_index=None,
                           state_metadata=None,
                           foundry_counter=None,
                           features=None,
                           immutable_features=None):
        """Build an AliasOutput.
        """
        return self.send_message('BuildAliasOutput', {
            'aliasId': alias_id,
            'unlockConditions': unlock_conditions,
            'amount': amount,
            'nativeTokens': native_tokens,
            'stateIndex': state_index,
            'stateMetadata': state_metadata,
            'foundryCounter': foundry_counter,
            'features': features,
            'immutableFeatures': immutable_features
        })

    def build_basic_output(self,
                           unlock_conditions,
                           amount=None,
                           native_tokens=None,
                           features=None):
        """Build a BasicOutput.
        """
        return self.send_message('BuildBasicOutput', {
            'unlockConditions': unlock_conditions,
            'amount': amount,
            'nativeTokens': native_tokens,
            'features': features,
        })

    def build_foundry_output(self,
                             serial_number,
                             token_scheme,
                             unlock_conditions,
                             amount=None,
                             native_tokens=None,
                             features=None,
                             immutable_features=None):
        """Build a FoundryOutput.
        """
        return self.send_message('BuildFoundryOutput', {
            'serial_number': serial_number,
            'token_scheme': token_scheme,
            'unlockConditions': unlock_conditions,
            'amount': amount,
            'nativeTokens': native_tokens,
            'features': features,
            'immutableFeatures': immutable_features
        })

    def build_nft_output(self,
                         nft_id,
                         unlock_conditions,
                         amount=None,
                         native_tokens=None,
                         features=None,
                         immutable_features=None):
        """Build an NftOutput.
        """
        return self.send_message('BuildNftOutput', {
            'nftId': nft_id,
            'unlockConditions': unlock_conditions,
            'amount': amount,
            'nativeTokens': native_tokens,
            'features': features,
            'immutableFeatures': immutable_features
        })

    def generate_addresses(self, secret_manager, options):
        """Generate addresses.
        """
        return self.send_message('GenerateAddresses', {
            'secretManager': secret_manager,
            'options': options
        })

    def build_and_post_block(self, secret_manager=None, options=None):
        """Build and post a block.
        """
        return self.send_message('BuildAndPostBlock', {
            'secretManager': secret_manager,
            'options': options
        })

    def get_node(self):
        """Get a node candidate from the synced node pool.
        """
        return self.send_message('GetNode')

    def get_network_info(self):
        """Gets the network related information such as network_id and min_pow_score.
        """
        return self.send_message('GetNetworkInfo')

    def get_network_id(self):
        """Gets the network id of the node we're connecting to.
        """
        return self.send_message('GetNetworkId')

    def get_bech32_hrp(self):
        """Returns the bech32_hrp.
        """
        return self.send_message('GetBech32Hrp')

    def get_min_pow_score(self):
        """Returns the min pow score.
        """
        return self.send_message('GetMinPowScore')

    def get_tips_interval(self):
        """Returns the tips interval.
        """
        return self.send_message('GetTipsInterval')

    def get_local_pow(self):
        """Returns if local pow should be used or not.
        """
        return self.send_message('GetLocalPow')

    def get_fall_back_to_local_pow(self):
        """Get fallback to local proof of work timeout.
        """
        return self.send_message('GetFallbackToLocalPow')

    def unsynced_nodes(self):
        """Returns the unsynced nodes.
        """
        return self.send_message('UnsyncedNodes')

    def get_ledger_nano_status(self, is_simulator):
        """Returns the Ledger Status.
        """
        return self.send_message('GetLedgerNanoStatus', { 'isSimulator': is_simulator })

    def prepare_transaction(self, secret_manager=None, options=None):
        """Prepare a transaction for signing.
        """
        return self.send_message('PrepareTransaction', {
            'secretManager': secret_manager,
            'options': options
        })

    def sign_transaction(self, secret_manager, prepared_transaction_data):
        """Sign a transaction.
        """
        return self.send_message('SignTransaction', {
            'secretManager': secret_manager,
            'preparedTransactionData': prepared_transaction_data
        })

    def store_mnemonic(self, secret_manager, mnemonic):
        """Store a mnemonic in the Stronghold vault.
        """
        return self.send_message('StoreMnemonic', {
            'secretManager': secret_manager,
            'mnemonic': mnemonic
        })

    def submit_payload(self, payload_dto):
        """Submit a payload in a block.
        """
        return self.send_message('SubmitPayload', {
            'payloadDto': payload_dto
        })
