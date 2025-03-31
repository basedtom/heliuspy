from heliuspy.api_versions.rpc20 import ApiRPC20
from heliuspy.api_versions.v0 import Apiv0


class HeliusAPI(ApiRPC20, Apiv0):
    def __init__(self, api_key: str, request_prefix: str = "RPC20-"):
        ApiRPC20.__init__(self, api_key=api_key, request_prefix=request_prefix)
        Apiv0.__init__(self, api_key=api_key)
