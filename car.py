from abc import ABC, abstractmethod


class Car(ABC):
    def __init__(self, last_service_date,engine,battery,tire):
        self.last_service_date = last_service_date
        self.dependecies=[engine, battery, tire]
        

    def needs_service(self):
        for dependency in self.dependecies:
            if dependency.needs_service():
                return True
        return False
