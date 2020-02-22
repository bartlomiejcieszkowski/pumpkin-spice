from pmps.storeroom import StoreroomInterface


class Device(object):
    def __init__(self):
        self.actions = {}
        self.equipment = {}


StoreroomInterface.register(Device)
