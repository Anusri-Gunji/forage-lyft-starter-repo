from abc import ABC
from battery import Battery
from datetime import datetime
class Nubbin(Battery, ABC):
    def __init__(self, max_lifetime,last_service_date):
        super().__init__(max_lifetime)
        self.last_service_date=last_service_date
    
    def needs_service(self):
        today = datetime.today().date()
        return self.last_service_date < today.replace(today.year - self.max_lifetime)

