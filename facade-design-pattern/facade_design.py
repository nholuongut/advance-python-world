"""
facade design pattern is suitable for :

having multiple base classes with methods
facade design class orchestrate those classes using facade methods
like access point with overall functionality
"""

from typing import Any, Dict, List
from util_class import Senor, Smoke, Lights
from meta_class import MetaClass
from logger import Logger

logger_cls = Logger()


class Facade(metaclass=MetaClass):
    def __init__(self) -> None:
        """initialize the device connections"""
        self.setup_devices()

    @classmethod
    def setup_devices(cls):
        cls._sensor = Senor()
        cls._smoke = Smoke()
        cls._lights = Lights()

    @logger_cls.log
    def emergency_on(self):
        """emergency react method

        Args:
            user_trigger (str, optional): user input. Defaults to "".
        """
        self._sensor.SensorOn()
        self._smoke.SmokeOn()
        self._lights.LightsOn()

    def emergency_off(self):
        """emergency alarm off steps"""
        self._sensor.SensorOff()
        self._smoke.SmokeOff()
        self._lights.LigthsOff()


if __name__ == "__main__":
    # define logger

    facade_point = Facade()
    print(facade_point)
    facade_point.emergency_on()
    facade_point.emergency_off()

    """
    since we enclosed our facade design with the metaclass , metaclass also wrapped with singleton design
    developer won't be  able to create new instance with same class
    """
    # define second facade class
    facade_point2 = Facade()
    print(facade_point2)
