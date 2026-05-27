from abc import ABC, abstractmethod

class Transport(ABC):
    @abstractmethod
    def transport_type(self):
        pass

    @abstractmethod
    def arrival_time(self):
        pass

    @abstractmethod
    def trip_time(self):
        pass

class Bike(Transport):
    def transport_type(self):
        return "Bike"

    def arrival_time(self):
        return "8:00"

    def trip_time(self):
        return "4h"

class car(Transport):
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