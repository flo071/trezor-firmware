# Automatically generated by pb2py
import protobuf as p


class ButtonRequest(p.MessageType):
    FIELDS = {
        1: ('code', p.UVarintType, 0),
        2: ('data', p.UnicodeType, 0),
    }
    MESSAGE_WIRE_TYPE = 26