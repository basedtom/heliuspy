from helius.utils import curl_helius


class RpcAPI:
    def __init__(self, api_key: str):
        self.base_rpc_url = "https://mainnet.helius-rpc.com"
        self.api_key_query = f"?api-key={api_key}"
        self.request_id = 0

    def get_token_accounts(self, **params):
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
            "id": "RpcAPI-" + str(self.request_id),
            "method": "getTokenAccounts",
            "params": params,
        }

        url = self.base_rpc_url + self.api_key_query

        return curl_helius._send_request(url, postdict=payload)

    def get_signatures_for_address(self, address: str, **params):
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
            "id": "RpcAPI-" + str(self.request_id),
            "method": "getSignaturesForAddress",
            "params": [address, params],
        }

        url = self.base_rpc_url + self.api_key_query

        return curl_helius._send_request(url, postdict=payload)

    def get_account_info(self, address: str, **params):
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
            "id": "RpcAPI-" + str(self.request_id),
            "method": "getAccountInfo",
            "params": [address, params],
        }

        url = self.base_rpc_url + self.api_key_query

        return curl_helius._send_request(url, postdict=payload)
