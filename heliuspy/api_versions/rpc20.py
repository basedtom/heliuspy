from heliuspy.utils import curl_helius


class ApiRPC20:
    def __init__(self, api_key: str, request_prefix: str = "RPC20-"):
        self.base_rpc_url = "https://mainnet.helius-rpc.com"
        self.api_key_query = f"?api-key={api_key}"
        self.request_id = 0
        self.request_prefix = request_prefix

    def get_token_accounts(self, **params) -> dict:
        """Retrieve all the token accounts associated with a specific mint or owner account.
        This is an efficient way to get all the owners of an SPL token or all tokens owned by a particular address.
        You can use the showZeroBalanceflag to include empty token accounts.

        Helius Doc: https://docs.helius.dev/compression-and-das-api/digital-asset-standard-das-api/get-token-accounts

        Args:
            mint (str): The mint address key.
            owner (str): The owner address key.
            page (int): The page of results to return.
            limit (int): The maximum number of assets to return.
            cursor (str): The cursor used for pagination.
            before (str): Returns results before the specified cursor.
            after (str): Returns results after the specified cursor.
            objects (obj):
                            showZeroBalance (bool): If true, show accounts with empty token balances.

        Returns:
            An object with the following keys:

            jsonrpc (str): rpc version
            result (obj) :
                            total (int)          : The number of results found for the request.
                            limit (int)          : The maximum number of results requested.
                            cursor(str)          : The cursor used for pagination.
                            token_accounts (list): An array of token accounts.
                                address (str)         : The address of the token account.
                                mint (str)            : The address of the mint account.
                                owner (str)           : The address of the token account owner.
                                amount (int)          : Number of tokens in the account.
                                delegated_amount (int): Number of delegated tokens in the account.
                                frozen (bool)         : If the account is frozen.
            id (any)     : ID used in the request

        """
        self.request_id += 1

        payload = {
            "jsonrpc": "2.0",
            "id": self.request_prefix + str(self.request_id),
            "method": "getTokenAccounts",
            "params": params,
        }

        url = self.base_rpc_url + self.api_key_query

        return curl_helius._send_request(url, postdict=payload)

    def get_signatures_for_address(self, address: str, **params) -> dict:
        """Returns signatures for confirmed transactions that include the given address in their accountKeys list.
        Returns signatures backwards in time from the provided signature or most recent confirmed block

        Helius Doc: https://docs.helius.dev/rpc/http/getsignaturesforaddress

        Args:
            address (str): The address to query.
            limit (int): Limit results
            before (str): Returns results before the specified signature.
            until (str): Returns results after the specified signature.
        Returns:
            An object with the following keys:

            jsonrpc (str): rpc version
            result (list of objs):
                    signature (str):  Transaction signature as a base-58 encoded string.
                    slot (int) The slot that contains the block with the transaction.
                    err (obj): Error if the transaction failed, or null if successful.
                    memo (str): Memo associated with the transaction, or null if none.
                    blockTime (int): Estimated production time as Unix timestamp, or null if not available.
                    confirmationStatus (str): Transaction's cluster confirmation status. e.g. "finalized"
            id (any): ID used in the request

        """
        self.request_id += 1

        payload = {
            "jsonrpc": "2.0",
            "id": self.request_prefix + str(self.request_id),
            "method": "getSignaturesForAddress",
            "params": [address, params],
        }

        url = self.base_rpc_url + self.api_key_query

        return curl_helius._send_request(url, postdict=payload)

    def get_account_info(self, address: str, **params) -> dict:
        """Returns all information associated with the account of provided Pubkey

        Helius Doc: https://docs.helius.dev/rpc/http/getaccountinfo

        Args:
            address (str): The address to query.
            limit (int): Limit results

        Returns:
            An object with the following keys:

            jsonrpc (str): rpc version
            result (obj):
                    context (obj):  Context of the request.
                        apiVersion (str): API version of the request.
                        slot (int): Slot number of the response.
                    value (obj):
                        data (str):
                        executable (bool):
                        lamports (int):
                        owner (str):
                        rentEpoch (int):
                        space (int):
            id (any): ID used in the request

        """
        self.request_id += 1

        payload = {
            "jsonrpc": "2.0",
            "id": self.request_prefix + str(self.request_id),
            "method": "getAccountInfo",
            "params": [address, params],
        }

        url = self.base_rpc_url + self.api_key_query

        return curl_helius._send_request(url, postdict=payload)

    def get_latest_blockhash(self, **params) -> dict:
        """Returns the latest blockhash

        Helius Doc: https://docs.helius.dev/rpc/http/getlatestblockhash

        Args:
            commitment (str, optional): The commitment level for the request.
                                    Options: confirmed, finalized, processed
            minContextSlot (int, optional): The minimum slot that the request can be evaluated at. E.g. 1000

        Returns:
            An object with the following keys:

            jsonrpc (str): rpc version
            result (obj) :
                    context (obj):  Context of the request.
                        slot (int): Slot number of the response.
                        apiVersion (str): API version of the request.
                    value (obj):
                        blockhash (str): A hash as a base-58 encoded string.
                        lastValidBlockHeight (int): The last block height at which the blockhash will be valid.
            id (any): ID used in the request

        """
        self.request_id += 1

        payload = {
            "jsonrpc": "2.0",
            "id": self.request_prefix + str(self.request_id),
            "method": "getLatestBlockhash",
            "params": [params],
        }

        url = self.base_rpc_url + self.api_key_query

        return curl_helius._send_request(url, postdict=payload)

    def get_block(self, slot_number: int, **params) -> dict:
        """Returns identity and transaction information about a confirmed block in the ledger

        Helius Doc: https://docs.helius.dev/rpc/http/getblock

        Args:
            slot_number (str): Slot number as a u64 integer.
            commitment (str, optional): The commitment level for the request. Defaults to "finalized"
                                Options: confirmed, finalized, processed
            encoding (str, optional): The encoding format for each returned transaction. Defaults to "json"
                                Options: json, jsonParsed, base58, base64
            transactionDetails (str, optional): Level of transaction detail to return. Defaults to "full"
                                        Options: full, accounts, signatures, none

            maxSupportedTransactionVersion (int, optional): Maximum transaction version to return in responses.
                                                             Defaults to 1
            rewards (bool, optional): Whether to populate the rewards array. Defaults to True


        Returns:
            An object with the following keys:

            jsonrpc (str): rpc version
            result (obj) :
                    blockhash (str)            : The blockhash of this block (base-58 encoded string).
                    previousBlockhash (str)    : The blockhash of the block's parent.
                    parentSlot (int)           : The slot index of this block's parent.
                    transactions (list of objs): Array of transaction details if full transaction details are
                                                 requested.
                            transaction (obj)       : Transaction details in the requested encoding format.
                            meta (obj)              : Metadata associated with the transaction.
                                        fee (int)              : Fee charged for the transaction.
                                        preBalances (list)     : Array of account balances before the transaction.
                                        postBalances (list)    : Array of account balances after the transaction.
                                        rewards (list of objs) : Rewards for the transaction, if requested.
                                                commission (int)   :
                                                postBalance (int)  :
                                                pubkey(str)        : The public key of the account that received the
                                                                      reward.
                                                lamports (int)     : Number of reward lamports credited or debited.
                                                rewardType (str)   : Type of reward (e.g., "fee", "rent").

                    blockTime (int)            : Estimated production time as Unix timestamp.
                    blockHeight (int)          : Number of blocks beneath this block.
            id (any): ID used in the request

        """
        self.request_id += 1

        if "maxSupportedTransactionVersion" not in params:
            params["maxSupportedTransactionVersion"] = 1

        payload = {
            "jsonrpc": "2.0",
            "id": self.request_prefix + str(self.request_id),
            "method": "getBlock",
            "params": [slot_number, params],
        }

        url = self.base_rpc_url + self.api_key_query

        return curl_helius._send_request(url, postdict=payload)

    def get_asset(self, id: str, **params) -> dict:
        """Get an asset by its ID.

        This method will return all relevant information, including metadata for a given Token or Any NFT (cNFT, pNFT,
        core NFT).

        To support tokens (Fungible Extensions), set the showFungible flag to true.

        You can optionally display inscription and SPL-20 token data with the showInscription flag.

        Helius Doc: https://docs.helius.dev/compression-and-das-api/digital-asset-standard-das-api/get-asset

        Args:
            id (str)                                    : An ID to identify the request.
            showUnverifiedCollections (bool, optional)  : Displays grouping information for unverified collections
                                                            instead of skipping them. Defaults to False.
            showCollectionMetadata (bool, optional)     : Displays metadata for the collection. Defaults to False.
            showFungible (bool, optional)               : Displays fungible tokens held by the owner.
                                                            Defaults to False.
            showInscription (bool, optional)            : Displays inscription details of assets inscribed on-chain.
                                                            Defaults to False.

        Returns:
            An object with the following keys:

            jsonrpc (str): rpc version
            result (obj) :
                    interface (str)             : The interface type of the asset.
                                                 Options: V1_NFT, V1_PRINT, LEGACY_NFT, V2_NFT, FungibleAsset,
                                                 FungibleToken, Custom, Identity, Executable, ProgrammableNFT

                    id (str)                    : The unique identifier of the asset.

                    content (obj)               : Content information of the asset.
                                $schema (str)         : The schema URL for the asset metadata.
                                json_uri (str)        : URI pointing to the JSON metadata.
                                files (list of objs)  : Array of files associated with the asset.
                                        cdn_uri (str)       :
                                        mime (str)          :
                                        uri (str)           :
                                metadata (obj)        : Metadata information about the asset.
                                        name (str)          : The name of the asset.
                                        symbol (str)        : The symbol of the asset.
                                links (obj)           : External links related to the asset.
                                        image (str)         : URI to an image

                    authorities (list of obj)   : List of authorities associated with the asset.
                                address (str)         : The authority's address.
                                scopes (list of str)  : The scopes of authority.

                    compression (obj)           : Compression details of the asset.
                                eligible (bool)       : Whether the asset is eligible for compression.
                                compressed (bool)     : Whether the asset is currently compressed.
                                data_hash (str)       : Hash of the asset data.
                                creator_hash (str)    : Hash of the creator data.
                                asset_hash (str)      : Hash of the entire asset.
                                tree (str)            : Merkle tree address.
                                seq (int)             : Sequence number.
                                leaf_id (int)         : Leaf identifier in the merkle tree.

                    grouping (obj)              : Grouping information for the asset.
                                group_key (str)       : The key identifying the group.
                                group_value (str)     : The value associated with the group.

                    royalty (obj)               : Royalty information for the asset.
                                royalty_model (str)         : The model used for royalties.
                                target (str)                : The target address for royalties.
                                percent (float)             : Royalty percentage.
                                basis_points (int)          : Royalty basis points.
                                primary_sale_happened (bool): Whether the primary sale has occurred.
                                locked (bool)               : Whether the royalty is locked.

                    creators (list of objs)     : List of creators of the asset.
                                address (str)       : The creator's address.
                                share (int)         : The creator's share percentage.
                                verified (bool)     : Whether the creator is verified.

                    ownership (obj)             : Ownership details of the asset.
                                frozen (bool)        : Whether the asset is frozen.
                                delegated (bool)     : Whether the asset is delegated.
                                delegate (str)       : The delegate's address if delegated.
                                ownership_model (str): The model of ownership.
                                owner (str)          : The owner's address.

                    supply (obj)                : Supply information for the asset.
                                print_max_supply (int)    : Maximum supply that can be printed.
                                print_current_supply (int): Current printed supply.
                                edition_nonce (int)       : Edition nonce.
                    mutable (bool)              : Whether the asset is mutable.
                    burnt (bool)                : Whether the asset has been burnt.
                    token_info (obj)            : Token-specific information.
                                supply (int)           : Total token supply.
                                decimals (int)         : Number of decimals.
                                token_program (str)    : Token program ID.
                                mint_authority (str)   : Mint authority address.
                                freeze_authority (str) : Freeze authority address.
                                symbol (str)           : Symbol of asset.
                                price_info (obj)       : Current price of asset.
                                    currency (str)          : Base currency of quote e.g. "USDC"
                                    price_per_token (float) : Price e.g. 0.017219

            id (any): ID used in the request

        """
        self.request_id += 1

        if "id" not in params:
            params["id"] = id

        payload = {
            "jsonrpc": "2.0",
            "id": self.request_prefix + str(self.request_id),
            "method": "getAsset",
            "params": params,
        }

        url = self.base_rpc_url + self.api_key_query

        return curl_helius._send_request(url, postdict=payload)

    def get_assets_by_owner(self, owner_address: str, **params) -> dict:
        """Get a list of assets owned by an address.

        This method is the fastest way to return all assets belonging to a wallet.

        Supported assets include NFTs, compressed NFTs (regular DAS), fungible tokens, and Token22.

        Helius Doc: https://docs.helius.dev/compression-and-das-api/digital-asset-standard-das-api/get-assets-by-owner

        Args:
            owner_address (str)     : The owner address key.
            page (int, optional)    : The page of results to return. Defaults to 1.
            limit (int, optional)   : The maximum number of assets to return.
            sortBy (dict, optional) : The sorting options for the response.
                            sortBy (str)        : The criteria by which the retrieved assets will be sorted.
                                                    Options: created, recent_action, updated, none
                            sortDirection (str) : The direction by which the retrieved assets will be sorted.
                                                    Options: asc, desc
            options (bool, optional):
                            showUnverifiedCollections (bool): Displays grouping information for unverified collections.
                                                                Defaults to False.
                            showCollectionMetadata (bool)   : Displays metadata for the collection. Defaults to False.
                            showGrandTotal (bool)           : Shows the total number of assets. Slower request.
                                                                Defaults to False.
                            showFungible (bool)             : Shows fungible tokens. Defaults to False.
                            showNativeBalance (bool)        : Shows the SOL balance held by the owner.
                                                                Defaults to False.
                            showInscription (bool)          : Displays inscription details. Defaults to False
                            showZeroBalance (bool)          : Displays assets with zero balance. Defaults to False

        Returns:
            An object with the following keys:

            jsonrpc (str): rpc version
            result (obj) :
                    cursor (str)        : Used for pagination
                    limit (int)         : Number of items results are limited to
                    total (int)         : Number of items in results
                    items (list of objs): List of assets. See `get_asset` for obj structure

        """

        self.request_id += 1

        if "ownerAddress" not in params:
            params["ownerAddress"] = owner_address

        payload = {
            "jsonrpc": "2.0",
            "id": self.request_prefix + str(self.request_id),
            "method": "getAssetsByOwner",
            "params": params,
        }

        url = self.base_rpc_url + self.api_key_query

        return curl_helius._send_request(url, postdict=payload)
