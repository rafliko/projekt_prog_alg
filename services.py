from abc import ABC, abstractmethod
from transport import Bike
from transport import Car
from transport import Scooter


class TransportServices(ABC):
    """
    Abstrakcyjna klasa usług transportowych, tworząca obiekty przedstawiające środków transportu.
    Klasa ta implementuje wzorzec projektowy Factory Method.

    Attributes:
        available (bool): Flaga reprezentująca dostępność danego środka transportu.
    """

    def __init__(self):
        """
        Inicjalizacja klasy usług transportowych.
        """
        self.available = True

    def order_transport(self):
        """
        Metoda zamawiająca transport. Ustawia flagę available na False.
        """
        if self.available:
            transport = self.create_transport()
            print(f"Transport: {self.transport_name()}, available: {self.available}")
            print(f"Arrival time: {transport.arrival_time()}")
            print(f"Trip time: {transport.trip_time()}")
            self.available = False
        else:
            print(f"Transport unavailable")

    @abstractmethod
    def create_transport(self):
        """
        Abstrakcyjna metoda tworząca obiekt dla odpowiedniego środka transportu.

        Returns:
            object: Odpowiedni obiekt dziedziczący klasę Transport.
        """
        pass

    @abstractmethod
    def transport_name(self):
        """
        Abstrakcyjna metoda zwracająca nazwę odpowiedniego środka transportu.

        Returns:
            str: Nazwa odpowiedniego środka transportu.
        """
        pass


class BikeTransportServices(TransportServices):
    def create_transport(self):
        return Bike()

    def transport_name(self):
        return "Bike"


class CarTransportServices(TransportServices):
    def create_transport(self):
        return Car()

    def transport_name(self):
        return "Car"


class ScooterTransportServices(TransportServices):
    def create_transport(self):
        return Scooter()

    def transport_name(self):
        return "Scooter"