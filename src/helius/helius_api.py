from helius.rpc20 import RpcAPI
from helius.transactions import TransactionsAPI


class HeliusAPI(RpcAPI, TransactionsAPI):
    def __init__(self, api_key: str):
        RpcAPI.__init__(self, api_key=api_key)
        TransactionsAPI.__init__(self, api_key=api_key)

    def test_function(self):
        print("here")
