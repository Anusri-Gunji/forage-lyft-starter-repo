from datetime import datetime

from engine.willoughby_engine import WilloughbyEngine
from car import Car


class Glissade(Car):
    def __init__(self,last_service_date, engine, battery):
        super().__init__(last_service_date,engine,battery)
