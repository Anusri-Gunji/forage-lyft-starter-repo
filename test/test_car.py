import unittest
from datetime import datetime

# from car import Car
from engine.capulet_engine import CapuletEngine
from engine.sternman_engine import SternmanEngine
from engine.willoughby_engine import WilloughbyEngine
from battery.spindler import Spindler
from battery.nubbin import Nubbin
from model.calliope import Calliope
from model.glissade import Glissade
from model.palindrome import Palindrome
from model.rorschach import Rorschach
from model.thovex import Thovex


class TestCalliope(unittest.TestCase):
    def test_battery_should_be_serviced(self):
        today = datetime.today().date()
        last_service_date = today.replace(year=today.year - 3)
        current_mileage = 0
        last_service_mileage = 0
        engine = CapuletEngine(last_service_date, current_mileage, last_service_mileage, 30000)
        battery = Spindler(2, last_service_date)
        car = Calliope(last_service_date, engine, battery)
        self.assertTrue(car.needs_service())

    def test_battery_should_not_be_serviced(self):
        today = datetime.today().date()
        last_service_date = today.replace(year=today.year - 1)
        current_mileage = 0
        last_service_mileage = 0
        engine = CapuletEngine(last_service_date, current_mileage, last_service_mileage, 30000)
        battery = Spindler(2, last_service_date)
        car = Calliope(last_service_date, engine, battery)
        self.assertFalse(car.needs_service())

    def test_engine_should_be_serviced(self):
        last_service_date = datetime.today().date()
        current_mileage = 30001
        last_service_mileage = 0
        engine = CapuletEngine(last_service_date, current_mileage, last_service_mileage, 30000)
        battery = Spindler(2, last_service_date)
        car = Calliope(last_service_date, engine, battery)
        self.assertTrue(car.needs_service())

    def test_engine_should_not_be_serviced(self):
        last_service_date = datetime.today().date()
        current_mileage = 30000
        last_service_mileage = 0
        engine = CapuletEngine(last_service_date, current_mileage, last_service_mileage, 30000)
        battery = Spindler(2, last_service_date)
        car = Calliope(last_service_date, engine, battery)
        self.assertFalse(car.needs_service())


class TestGlissade(unittest.TestCase):
    def test_battery_should_be_serviced(self):
        today = datetime.today().date()
        last_service_date = today.replace(year=today.year - 3)
        current_mileage = 0
        last_service_mileage = 0
        engine = WilloughbyEngine(last_service_date, current_mileage, last_service_mileage, 60000)
        battery = Spindler(2, last_service_date)
        car = Glissade(last_service_date, engine, battery)
        self.assertTrue(car.needs_service())

    def test_battery_should_not_be_serviced(self):
        today = datetime.today().date()
        last_service_date = today.replace(year=today.year - 1)
        current_mileage = 0
        last_service_mileage = 0
        engine = WilloughbyEngine(last_service_date, current_mileage, last_service_mileage, 60000)
        battery = Spindler(2, last_service_date)
        car = Glissade(last_service_date, engine, battery)
        self.assertFalse(car.needs_service())

    def test_engine_should_be_serviced(self):
        last_service_date = datetime.today().date()
        current_mileage = 60001
        last_service_mileage = 0
        engine = WilloughbyEngine(last_service_date, current_mileage, last_service_mileage, 60000)
        battery = Spindler(2, last_service_date)
        car = Glissade(last_service_date, engine, battery)
        self.assertTrue(car.needs_service())

    def test_engine_should_not_be_serviced(self):
        last_service_date = datetime.today().date()
        current_mileage = 60000
        last_service_mileage = 0
        engine = WilloughbyEngine(last_service_date, current_mileage, last_service_mileage, 60000)
        battery = Spindler(2, last_service_date)
        car = Glissade(last_service_date, engine, battery)
        self.assertFalse(car.needs_service())


class TestPalindrome(unittest.TestCase):
    def test_battery_should_be_serviced(self):
        today = datetime.today().date()
        last_service_date = today.replace(year=today.year - 5)
        warning_light_is_on = False
        engine = SternmanEngine(last_service_date, warning_light_is_on)
        battery = Spindler(2, last_service_date)
        car = Palindrome(last_service_date, engine, battery)
        self.assertTrue(car.needs_service())

    def test_battery_should_not_be_serviced(self):
        today = datetime.today().date()
        last_service_date = today.replace(year=today.year - 3)
        warning_light_is_on = False
        engine = SternmanEngine(last_service_date, warning_light_is_on)
        battery = Spindler(2, last_service_date)
        car = Palindrome(last_service_date, engine, battery)
        self.assertFalse(car.needs_service())

    def test_engine_should_be_serviced(self):
        last_service_date = datetime.today().date()
        warning_light_is_on = True
        engine = SternmanEngine(last_service_date, warning_light_is_on)
        battery = Spindler(2, last_service_date)
        car = Palindrome(last_service_date, engine, battery)
        self.assertTrue(car.needs_service())

    def test_engine_should_not_be_serviced(self):
        last_service_date = datetime.today().date()
        warning_light_is_on = False
        engine = SternmanEngine(last_service_date, warning_light_is_on)
        battery = Spindler(2, last_service_date)
        car = Palindrome(last_service_date, engine, battery)
        self.assertFalse(car.needs_service())


class TestRorschach(unittest.TestCase):
    def test_battery_should_be_serviced(self):
        today = datetime.today().date()
        last_service_date = today.replace(year=today.year - 5)
        current_mileage = 0
        last_service_mileage = 0
        engine = WilloughbyEngine(last_service_date, current_mileage, last_service_mileage, 60000)
        battery = Nubbin(4, last_service_date)
        car = Rorschach(last_service_date, engine, battery)
        self.assertTrue(car.needs_service())

    def test_battery_should_not_be_serviced(self):
        today = datetime.today().date()
        last_service_date = today.replace(year=today.year - 3)
        current_mileage = 0
        last_service_mileage = 0
        engine = WilloughbyEngine(last_service_date, current_mileage, last_service_mileage, 60000)
        battery = Nubbin(4, last_service_date)
        car = Rorschach(last_service_date, engine, battery)
        self.assertFalse(car.needs_service())

    def test_engine_should_be_serviced(self):
        last_service_date = datetime.today().date()
        current_mileage = 60001
        last_service_mileage = 0
        engine = WilloughbyEngine(last_service_date, current_mileage, last_service_mileage, 60000)
        battery = Nubbin(4, last_service_date)
        car = Rorschach(last_service_date, engine, battery)
        self.assertTrue(car.needs_service())

    def test_engine_should_not_be_serviced(self):
        last_service_date = datetime.today().date()
        current_mileage = 60000
        last_service_mileage = 0
        engine = WilloughbyEngine(last_service_date, current_mileage, last_service_mileage, 60000)
        battery = Nubbin(4, last_service_date)
        car = Rorschach(last_service_date, engine, battery)
        self.assertFalse(car.needs_service())


class TestThovex(unittest.TestCase):
    def test_battery_should_be_serviced(self):
        today = datetime.today().date()
        last_service_date = today.replace(year=today.year - 5)
        current_mileage = 0
        last_service_mileage = 0
        engine = CapuletEngine(last_service_date, current_mileage, last_service_mileage, 30000)
        battery = Nubbin(4, last_service_date)
        car = Thovex(last_service_date, engine, battery)
        self.assertTrue(car.needs_service())

    def test_battery_should_not_be_serviced(self):
        today = datetime.today().date()
        last_service_date = today.replace(year=today.year - 3)
        current_mileage = 0
        last_service_mileage = 0
        engine = CapuletEngine(last_service_date, current_mileage, last_service_mileage, 30000)
        battery = Nubbin(4, last_service_date)
        car = Thovex(last_service_date, engine, battery)
        self.assertFalse(car.needs_service())

    def test_engine_should_be_serviced(self):
        last_service_date = datetime.today().date()
        current_mileage = 30001
        last_service_mileage = 0
        engine = CapuletEngine(last_service_date, current_mileage, last_service_mileage, 30000)
        battery = Nubbin(4, last_service_date)
        car = Thovex(last_service_date, engine, battery)
        self.assertTrue(car.needs_service())

    def test_engine_should_not_be_serviced(self):
        last_service_date = datetime.today().date()
        current_mileage = 30000
        last_service_mileage = 0
        engine = CapuletEngine(last_service_date, current_mileage, last_service_mileage, 30000)
        battery = Nubbin(4, last_service_date)
        car = Thovex(last_service_date, engine, battery)
        self.assertFalse(car.needs_service())


if __name__ == '__main__':
    unittest.main()
