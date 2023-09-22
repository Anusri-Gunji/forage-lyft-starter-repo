from abc import ABC, abstractmethod

class Tire(ABC):
    def __init__(self, tire_condition):
        self.tire_condition = tire_condition

    @abstractmethod
    def needs_service(self):
        pass
