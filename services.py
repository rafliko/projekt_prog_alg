from abc import ABC, abstractmethod
from transport import Bike

class TransportServices(ABC):
    def __init__(self):
        self.available = True

    def order_transport(self):
        if self.available:
            print(f"Transport: {self.transport_name()}, available: {self.available}")
            return self.create_transport()
        else:
            print(f"Transport unavailable")
            return None

    @abstractmethod
    def create_transport(self):
        pass

    @abstractmethod
    def transport_name(self):
        pass

class BikeTransportServices(TransportServices):
    def create_transport(self):
        return Bike()

    def transport_name(self):
        return "Bike"