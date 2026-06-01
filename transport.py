from abc import ABC, abstractmethod


class Transport(ABC):
    """
    Abstrakcyjna klasa reprezentująca środek transportu.
    """
    @abstractmethod
    def transport_type(self):
        """
        Abstrakcyjna metoda zwracająca nazwę środka transportu.

        Returns:
            str: Nazwa środka transportu.
        """
        pass

    @abstractmethod
    def arrival_time(self):
        """
        Abstrakcyjna metoda zwracająca czas przyjazdu.

        Returns:
            str: Czas przyjazdu.
        """
        pass

    @abstractmethod
    def trip_time(self):
        """
        Abstrakcyjna metoda zwracająca czas podróży.

        Returns:
            str: Czas podróży.
        """
        pass


class Bike(Transport):
    def transport_type(self):
        return "Bike"

    def arrival_time(self):
        return "8:00"

    def trip_time(self):
        return "4h"

class Car(Transport):
    def transport_type(self):
        return "Car"

    def arrival_time(self):
        return "5:00"

    def trip_time(self):
        return "1h"


class Scooter(Transport):
    def transport_type(self):
        return "Scooter"

    def arrival_time(self):
        return "6:00"

    def trip_time(self):
        return "2h"