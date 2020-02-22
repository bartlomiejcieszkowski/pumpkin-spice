from abc import ABC, abstractmethod

class EquipmentInterface(ABC):
    @abstractmethod
    def get_transport(self):
        pass


class Equipment(object):
    def __init__(self):
        self.transport = None

