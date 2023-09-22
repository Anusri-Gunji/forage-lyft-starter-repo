from datetime import datetime

from car import Car

class Rorschach(Car):
    def __init__(self, last_service_date, engine, battery):
        super().__init__(last_service_date, engine, battery)
