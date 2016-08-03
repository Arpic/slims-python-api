from enum import Enum


class Status(Enum):
    DONE = 1
    FAILED = 2


class FlowRun(object):

    def __init__(self, slims_api, index, data):
        self.slims_api = slims_api
        self.index = index
        self.data = data

    def log(self, message):
        body = {
            'index': self.index,
            'flowRunGuid': self.data["flowInformation"]["flowRunGuid"],
            'message': message
        }
        self.slims_api.post("external/log", body)

    def update_status(self, status):
        body = {
            'index': self.index,
            'flowRunGuid': self.data["flowInformation"]["flowRunGuid"],
            'status': status.name
        }
        self.slims_api.post("external/status", body)
