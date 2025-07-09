import uuid
import json

class Message:

    def __init__(self, uuid, flag):

        self.uuid = str(uuid)
        self.flag = flag

    def to_json(self):

        return json.dumps({'uuid': self.uuid, 'flag': self.flag}) + "\n"

    @staticmethod
    def from_json(data):

        obj = json.loads(data.strip())

        return Message(uuid.UUID(obj['uuid']), obj['flag'])
