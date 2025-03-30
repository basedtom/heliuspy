from helius.utils import curl_helius


class TransactionsAPI:
    def __init__(self, api_key: str):
        self.base_url = "https://api.helius.xyz"
        self.base_rpc_url = "https://mainnet.helius-rpc.com"
        self.api_key = api_key
        self.api_key_query = f"?api-key={api_key}"
        self.request_id = 0

    def get_parsed_transactions(self, address: str, **params):
        """Parsed Transaction History for any given address.

        Helius Doc: https://docs.helius.dev/solana-apis/enhanced-transactions-api/parsed-transaction-history

        Args:
            address (str): The address to query for.
            before (str): Start searching backwards from this transaction signature.
            until (str): Search until this transaction signature.
            commitment (str) : How finalized a block must be to be included in the search.
                                          If not provided, will default to "finalized" commitment.
                                          Note that "processed" level commitment is not supported.
                                          Valid values: "finalized", "confirmed
            source (str): The TransactionSource to filter by
            typeTransactionType (str):  The TransactionType to filter by.
            limit(int): The number of transactions to retrieve. The value should be between 1 and 100.
                          Defaults to 100

        Returns:
            list of objs: list of enriched transactions data
                description(str):
                type(str): Transaction type e.g. 'SWAP'
                source(str): e.g. 'JUPITER'
                fee(int):
                feePayer(str)
                signature(str)
                slot(int):
                timestamp(int):
                nativeTransfers(list of objs):
                            fromUserAccount(str): The user account the sol is sent from.
                            toUserAccount(str): The user account the sol is sent to.
                            amount(int): The amount of sol sent (in lamports).
                tokenTransfers(list of objs):
                            fromUserAccount(str): The user account the tokens are sent from.
                            toUserAccount(str): The user account the tokens are sent to.
                            fromTokenAccount(str): The token account the tokens are sent from.
                            toTokenAccount(str): The token account the tokens are sent to.
                            tokenAmount(float): The number of tokens sent.
                            mint(str): The mint account of the token.
                accountData(list of objs):
                            accountstring The account that this data is provided for.
                            nativeBalanceChangenumber Native (SOL) balance change of the account.
                            tokenBalanceChanges(list of objs):  Token balance changes of the account.
                                        userAccount(str):
                                        tokenAccount(str):
                                        mint(str):
                                        rawTokenAmount(obj):
                                            tokenAmount(str):
                                            decimals(int):
                transactionError(obj):
                            error(str)
                instructions(list of objs):
                        accounts(list of strings): The accounts used in instruction.
                        data(str): Data passed into the instruction
                        programId(str): Program used in instruction
                        innerInstructions(list of objs): Inner instructions used in instruction
                            accounts(list of strs):
                            data(str):
                            programID(str)
                events(obj): Events associated with this transaction
        """

        path = "/v0/addresses/{address}/transactions".format(address=address)
        url = self.base_url + path

        params["api-key"] = self.api_key

        return curl_helius._send_request(url, params=params)
