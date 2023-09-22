from abc import ABC

from engine import Engine
from car import Car


class WilloughbyEngine(Engine, ABC):
    def __init__(self, last_service_date, current_mileage, last_service_mileage,max_mileage):
        super().__init__(last_service_date)
        self.current_mileage = current_mileage
        self.last_service_mileage = last_service_mileage
        self.max_mileage=max_mileage

    def needs_service(self):
        return self.current_mileage - self.last_service_mileage > self.max_mileage
