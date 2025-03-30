def test_get_parsed_transactions(HeliusInterface):
    transactions = HeliusInterface.get_parsed_transactions(
        address="6n9VGHytR4SPBZQSoWVLgH2hLHmfXSSFJsbHAdMr5zzE",
        type="SWAP",
        before="37TBFEwuZnFfH1UA8XWPLsecmUWURZjVwou2i43MF7UAUqZLPu8aM7yKH3u14PjRv6qBU6vLvKsHarX6nJnAhNnx",
        limit=10,
    )

    assert len(transactions) == 10

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
