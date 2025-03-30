test_address = "6n9VGHytR4SPBZQSoWVLgH2hLHmfXSSFJsbHAdMr5zzE"
test_mint_address = "63LfDmNb3MQ8mw9MtZ2To9bEA2M71kZUUGq5tiJxcqj9"


def test_get_token_accounts(HeliusInterface):

    token_accounts = HeliusInterface.get_token_accounts(
        owner=test_address,
        displayOptions={"showZeroBalance": False},
        page=1,
        limit=10,  # Adjust limit as needed
    )
    assert token_accounts

    expected_keys = sorted(["jsonrpc", "result", "id"])
    response_keys = sorted(token_accounts.keys())

    assert expected_keys == response_keys

    response_result_keys = sorted(token_accounts["result"].keys())

    assert "token_accounts" in response_result_keys
    assert "total" in response_result_keys
    assert "limit" in response_result_keys

    assert "address" in token_accounts["result"]["token_accounts"][0]
    assert "mint" in token_accounts["result"]["token_accounts"][0]
    assert "owner" in token_accounts["result"]["token_accounts"][0]
    assert "amount" in token_accounts["result"]["token_accounts"][0]
    assert "delegated_amount" in token_accounts["result"]["token_accounts"][0]
    assert "frozen" in token_accounts["result"]["token_accounts"][0]


def test_get_signatures_for_address(HeliusInterface):
    sigs = HeliusInterface.get_signatures_for_address(address=test_mint_address, limit=50)

    expected_keys = sorted(["jsonrpc", "result", "id"])
    response_keys = sorted(sigs.keys())

    assert expected_keys == response_keys

    expected_result_keys = sorted(["signature", "slot", "err", "memo", "blockTime", "confirmationStatus"])
    response_result_keys = sorted(sigs["result"][0].keys())

    assert expected_result_keys == response_result_keys

    assert len(sigs["result"]) == 50


def test_get_account_info(HeliusInterface):
    accountinfo = HeliusInterface.get_account_info(address=test_address, limit=50)

    expected_keys = sorted(["jsonrpc", "result", "id"])
    response_keys = sorted(accountinfo.keys())

    assert expected_keys == response_keys

    expected_result_keys = sorted(["context", "value"])
    response_result_keys = sorted(accountinfo["result"].keys())

    assert expected_result_keys == response_result_keys
