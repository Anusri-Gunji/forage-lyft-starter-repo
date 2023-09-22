from datetime import datetime

from engine.capulet_engine import CapuletEngine
from car import Car


class Calliope(Car):
    def __init__(self,last_service_date, engine, battery):
        super().__init__(last_service_date,engine,battery)
