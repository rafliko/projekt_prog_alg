from abc import ABC, abstractmethod
from transport import Bike
from transport import Car
from transport import Scooter

class TransportServices(ABC):
    def __init__(self):
        self.available = True

    def order_transport(self):
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
        pass

    @abstractmethod
    def transport_name(self):
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