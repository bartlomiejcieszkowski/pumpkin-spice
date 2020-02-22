from abc import ABC, abstractmethod

class StoreroomInterface(ABC):
    @abstractmethod
    def get_equipment(self, id):
        raise NotImplementedError

    @abstractmethod
    def has_equipment(self, id):
        raise NotImplementedError

    @abstractmethod
    def reserve_equipment(self, id):
        raise NotImplementedError

    @abstractmethod
    def add_equipment(self, eq):
        raise NotImplementedError


