test_address = "6n9VGHytR4SPBZQSoWVLgH2hLHmfXSSFJsbHAdMr5zzE"
test_mint_address = "63LfDmNb3MQ8mw9MtZ2To9bEA2M71kZUUGq5tiJxcqj9"


def test_get_parsed_transactions(HeliusInterface):
    transactions = HeliusInterface.get_parsed_transactions(
        address=test_address,
        type="SWAP",
        before="37TBFEwuZnFfH1UA8XWPLsecmUWURZjVwou2i43MF7UAUqZLPu8aM7yKH3u14PjRv6qBU6vLvKsHarX6nJnAhNnx",
        limit=10,
    )

    assert 1 <= len(transactions) <= 10

    transaction_keys = sorted(transactions[0].keys())

    expected_keys = sorted(
        [
            "description",
            "type",
            "source",
            "fee",
            "feePayer",
            "signature",
            "slot",
            "timestamp",
            "nativeTransfers",
            "tokenTransfers",
            "accountData",
            "transactionError",
            "instructions",
            "events",
        ]
    )

    assert transaction_keys == expected_keys


def test_get_token_metadata(HeliusInterface):
    token_metadata = HeliusInterface.get_token_metadata(mint_account=test_mint_address, includeOffChain=True)

    assert len(token_metadata) == 1

    expected_keys = sorted(["onChainAccountInfo", "account", "onChainMetadata", "legacyMetadata", "offChainMetadata"])
    response_keys = sorted(token_metadata[0].keys())

    assert expected_keys == response_keys
