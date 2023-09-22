from abc import ABC, abstractmethod


class Battery(ABC):
    def __init__(self, max_lifetime):
        self.max_lifetime = max_lifetime

    @abstractmethod
    def needs_service(self):
        pass
