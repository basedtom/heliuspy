# heliuspy

A Python library for interacting with Helius endpoints.

## Installation

```bash
pip install heliuspy
```

## Example Usage

```python
from heliuspy import HeliusAPI

H = HeliusAPI(api_key=API_KEY)

latest_block_info = HeliusInterface.get_latest_blockhash()

transactions = HeliusInterface.get_parsed_transactions(
        address='XYZ',
        type="SWAP",
        before="37TBFEwuZnFfH1UA8XWPLsecmUWURZjVwou2i43MF7UAUqZLPu8aM7yKH3u14PjRv6qBU6vLvKsHarX6nJnAhNnx",
        limit=10,
    )

```


