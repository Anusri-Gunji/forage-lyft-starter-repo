from tire import Tire

class Carrigan(Tire):
    def __init__(self, tire_condition):
        super().__init__(tire_condition)

    def needs_service(self):
        return sum(self.tire_condition) >= 3
