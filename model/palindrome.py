from datetime import datetime

from engine.sternman_engine import SternmanEngine

from car import Car

class Palindrome(Car):
    def __init__(self,last_service_date, engine, battery):
        super().__init__(last_service_date,engine,battery)
