from datetime import datetime

from engine.capulet_engine import CapuletEngine


class Thovex(CapuletEngine):
    def __init__(self,last_service_date, engine, battery):
        super().__init__(last_service_date,engine,battery)
