from battery import Battery
from abc import ABC
from datetime import datetime


class Spindler(Battery, ABC):
    def __init__(self, max_lifetime, last_service_date):
        super().__init__(max_lifetime)
        self.last_service_date = last_service_date

    def needs_service(self):
        today=datetime.today().date()
        return self.last_service_date < today.replace(today.year - self.max_lifetime)
