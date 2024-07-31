
from qdpc_core_models.models.user import User


class ResponseInfo(object):
    def __init__(self, **args):
        self.response = {
            "message": args.get('message', ""),
            "status": args.get('status', ""),
            "isSuccess": args.get('success', ""),
        }

