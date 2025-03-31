TEST_ADDRESS = "6n9VGHytR4SPBZQSoWVLgH2hLHmfXSSFJsbHAdMr5zzE"
TEST_MINT_ADDRESS = "63LfDmNb3MQ8mw9MtZ2To9bEA2M71kZUUGq5tiJxcqj9"


def test_get_token_accounts(HeliusInterface):

    token_accounts = HeliusInterface.get_token_accounts(
        owner=TEST_ADDRESS,
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
    sigs = HeliusInterface.get_signatures_for_address(address=TEST_MINT_ADDRESS, limit=50)

    expected_keys = sorted(["jsonrpc", "result", "id"])
    response_keys = sorted(sigs.keys())

    assert expected_keys == response_keys

    expected_result_keys = sorted(["signature", "slot", "err", "memo", "blockTime", "confirmationStatus"])
    response_result_keys = sorted(sigs["result"][0].keys())

    assert expected_result_keys == response_result_keys

    assert len(sigs["result"]) == 50


def test_get_account_info(HeliusInterface):
    accountinfo = HeliusInterface.get_account_info(address=TEST_ADDRESS, limit=50)

    expected_keys = sorted(["jsonrpc", "result", "id"])
    response_keys = sorted(accountinfo.keys())

    assert expected_keys == response_keys

    expected_result_keys = sorted(["context", "value"])
    response_result_keys = sorted(accountinfo["result"].keys())

    assert expected_result_keys == response_result_keys


def test_get_latest_blockhash(HeliusInterface):
    latest_block_info = HeliusInterface.get_latest_blockhash()

    expected_keys = sorted(["jsonrpc", "result", "id"])
    response_keys = sorted(latest_block_info.keys())

    assert expected_keys == response_keys

    expected_result_keys = sorted(["context", "value"])
    response_result_keys = sorted(latest_block_info["result"].keys())

    assert expected_result_keys == response_result_keys


def test_get_block(HeliusInterface):
    def get_slot_number() -> int:
        """Get latest slot number

        Returns:
            int: slot number
        """
        latest_blockhash = HeliusInterface.get_latest_blockhash()
        return latest_blockhash["result"]["context"]["slot"]

    slot_number = get_slot_number()

    block_info = HeliusInterface.get_block(slot_number=slot_number, rewards=False)

    expected_keys = sorted(["jsonrpc", "result", "id"])
    response_keys = sorted(block_info.keys())

    assert expected_keys == response_keys

    # Should not include rewards key
    expected_result_keys = sorted(
        ["blockhash", "previousBlockhash", "parentSlot", "transactions", "blockTime", "blockHeight"]
    )
    response_result_keys = sorted(block_info["result"].keys())

    assert expected_result_keys == response_result_keys

    # Test no transaction parameter
    block_info = HeliusInterface.get_block(slot_number=slot_number, rewards=True, transactionDetails="none")

    # Should not include transactions key
    expected_result_keys_no_transaction = sorted(
        ["blockhash", "previousBlockhash", "parentSlot", "blockTime", "blockHeight", "rewards"]
    )
    response_result_keys_no_transaction = sorted(block_info["result"].keys())

    assert expected_result_keys_no_transaction == response_result_keys_no_transaction


def test_get_asset(HeliusInterface):

    asset_info = HeliusInterface.get_asset(id=TEST_MINT_ADDRESS)

    expected_keys = sorted(["jsonrpc", "result", "id"])
    response_keys = sorted(asset_info.keys())

    assert expected_keys == response_keys

    assert "token_info" in asset_info["result"]
    assert "interface" in asset_info["result"]
    assert "supply" in asset_info["result"]
    assert "burnt" in asset_info["result"]


def test_get_assets_by_owner(HeliusInterface):

    owner_assets = HeliusInterface.get_assets_by_owner(
        owner_address=TEST_ADDRESS, options={"showFungible": True}, limit=5
    )

    expected_keys = sorted(["jsonrpc", "result", "id"])
    response_keys = sorted(owner_assets.keys())

    assert expected_keys == response_keys

    assert "items" in owner_assets["result"]
    assert "cursor" in owner_assets["result"]
    assert "limit" in owner_assets["result"]
    assert "total" in owner_assets["result"]

    assert "interface" in owner_assets["result"]["items"][0]
