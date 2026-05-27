from abc import ABC, abstractmethod
from transport import Bike

class TransportServices(ABC):
    def __init__(self):
        self.available = True

    def order_transport(self):
        if self.available:
            transport = self.create_transport()
            print(f"Transport: {self.transport_name()}, available: {self.available}")
            print(f"Arrival time: {transport.arrival_time()}")
            print(f"Trip time: {transport.trip_time()}")
        else:
            print(f"Transport unavailable")

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