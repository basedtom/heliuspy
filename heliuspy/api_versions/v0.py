from heliuspy.utils import curl_helius


class Apiv0:
    def __init__(self, api_key: str):
        self.base_url = "https://api.helius.xyz"
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

    def get_token_metadata(self, mint_account: str, **params):
        """Get both on-chain and off-chain metadata for Solana tokens.

        This Token Metadata endpoint returns all metadata associated with an account (Token/NFT),
        including data from the legacy token list. In a single request, you can pass up to 100 mint accounts.

        Helius Doc: https://docs.helius.dev/solana-apis/deprecated-token-metadata-api

        Args:
            mint_account (str)              : The mint account of the token to retrieve metadata for.
            includeOffChain (bool, optional): Include offchain data referenced in the uri of the metadata account.
                                                Defaults to False
            disableCache (bool, optional)   : Disable usage of cache, useful for monitoring metadata changes.


        Returns:
            list of objs: Token metadata stored both on-chain and in the old token list

                account (str)           : The mint account of the token

                onChainAccountInfo (obj):
                        accountInfo (obj)  : Account data that is stored on-chain.
                                key (str)          :
                                isSigner (bool)    :
                                isWritable (bool)  :
                                data (obj)         :
                                        parsed (obj)    :
                                                info (obj) :
                                                        decimals (int)        : e.g. 5
                                                        freezeAuthority (str) :
                                                        isInitialized (bool)  :
                                                        mintAuthority (str)   :
                                                        supply (str)          : e.g.  "960390941527687"
                                                type (str) : e.g "mint"
                                        program (str)   :
                                        space (int)     :
                                owner (str)        :
                                executable (bool)  :
                                lamports (int)     :
                                rentEpoch (int)    :
                        error (str)        : Options: UNKNOWN, EMPTY_ACCOUNT, TIMEOUT, INVALID_ACCOUNT, INVALID_PUBKEY

                onChainMetadata (obj)   : Metaplex metadata that is stored on-chain.
                        error (str)         :
                        metadata (obj)      :
                                collection
                                collectionDetails (obj)   :
                                data (obj)                :
                                        creators (str)            :
                                        name (str)                : Name of token
                                        sellerFeeBasisPoints (int):
                                        symbol (str)              : Symbol of token
                                        uri (str)                 : URI for metadata
                                editionNonce (int)        :
                                isMutable (bool)          :
                                key (str)                 :
                                mint (str)                :
                                primarySaleHappened (bool):
                                tokenStandard (str)       :
                                updateAuthority (str)     :
                                uses (obj)                :
                                    remaining (int)             :
                                    total (int)                 :
                                    useMethod (str)             :
                offChainMetadata (obj)  :
                legacyMetadata (obj)    : Data from the old SPL token list.

        """

        path = "/v0/token-metadata"
        url = self.base_url + path + self.api_key_query

        params["mintAccounts"] = [mint_account]

        return curl_helius._send_request(url, postdict=params)
