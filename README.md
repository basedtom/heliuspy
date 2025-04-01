# heliuspy

A Python library for interacting with Helius endpoints.

## Installation

To install the `heliuspy` library, use the following command:

```bash
pip install heliuspy
```

## Example Usage

Here is an example of how to use the `heliuspy` library:

```python
from heliuspy import HeliusAPI

HeliusInterface = HeliusAPI(api_key=API_KEY)

latest_block_info = HeliusInterface.get_latest_blockhash()

transactions = HeliusInterface.get_parsed_transactions(
    address='XYZ',
    type="SWAP",
    before="37TBFEwuZnFfH1UA8XWPLsecmUWURZjVwou2i43MF7UAUqZLPu8aM7yKH3u14PjRv6qBU6vLvKsHarX6nJnAhNnx",
    limit=10,
)
```

## Module Structure

### `heliuspy/__init__.py`

The `__init__.py` file initializes the `HeliusAPI` class which integrates multiple API versions:

```python
__version__ = "0.3.0"

from heliuspy.api_versions.rpc20 import ApiRPC20
from heliuspy.api_versions.v0 import Apiv0

class HeliusAPI(ApiRPC20, Apiv0):
    def __init__(self, api_key: str, request_prefix: str = "RPC20-"):
        ApiRPC20.__init__(self, api_key=api_key, request_prefix=request_prefix)
        Apiv0.__init__(self, api_key=api_key)
```

### `heliuspy/api_versions/rpc20.py`

The `rpc20.py` file contains the `ApiRPC20` class which provides methods to interact with the Helius RPC version 20:

#### `ApiRPC20` Class

- `__init__(self, api_key: str, request_prefix: str = "RPC20-")`
- `get_token_accounts(self, **params) -> dict`
  - Retrieve all the token accounts associated with a specific mint or owner account.
- `get_signatures_for_address(self, address: str, **params) -> dict`
  - Returns signatures for confirmed transactions that include the given address in their accountKeys list.
- `get_account_info(self, address: str, **params) -> dict`
  - Returns all information associated with the account of provided Pubkey.
- `get_latest_blockhash(self, **params) -> dict`
  - Returns the latest blockhash.
- `get_block(self, slot_number: int, **params) -> dict`
  - Returns identity and transaction information about a confirmed block in the ledger.
- `get_asset(self, id: str, **params) -> dict`
  - Get an asset by its ID.
- `get_assets_by_owner(self, owner_address: str, **params) -> dict`
  - Get a list of assets owned by an address.

### `heliuspy/api_versions/v0.py`

The `v0.py` file contains the `Apiv0` class which provides methods to interact with the Helius API version 0:

#### `Apiv0` Class

- `__init__(self, api_key: str)`
- `get_parsed_transactions(self, address: str, **params)`
  - Parsed Transaction History for any given address.
- `get_token_metadata(self, mint_account: str, **params)`
  - Get both on-chain and off-chain metadata for Solana tokens.

### `heliuspy/utils`

Utils folder contains utility functions and classes used across the library.

## Additional Information

For more detailed information on usage and implementation, refer to the respective module files and their docstrings.
