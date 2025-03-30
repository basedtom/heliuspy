from helius.api_versions.rpc20 import RpcAPI
from helius.api_versions.v0 import APIv0


class HeliusAPI(RpcAPI, APIv0):
    def __init__(self, api_key: str, request_prefix: str = "RPC20-"):
        RpcAPI.__init__(self, api_key=api_key, request_prefix=request_prefix)
        APIv0.__init__(self, api_key=api_key)
