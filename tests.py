import pytest

from customer import Customer
from services import BikeTransportServices, CarTransportServices, ScooterTransportServices
from transport import Bike, Car, Scooter

#tests for transport.

@pytest.mark.parametrize("transport_option, expected_type, expected_arrival, expected_trip", [
    (Bike, "Bike", "8:00", "4h"),
    (Car, "Car", "5:00", "1h"),
    (Scooter, "Scooter", "6:00", "2h"),
])

def test_transport(transport_option, expected_type, expected_arrival, expected_trip):
    """Czy każdy transport zwraca poprawne dane"""

    transport = transport_option()

    assert transport.transport_type() == expected_type
    assert transport.arrival_time() == expected_arrival
    assert transport.trip_time() == expected_trip

#test for services.

@pytest.mark.parametrize("service_option, expected_transport_option, expected_name", [
    (BikeTransportServices, Bike, "Bike"),
    (CarTransportServices, Car, "Car"),
    (ScooterTransportServices, Scooter, "Scooter"),
])

def test_service_correct(service_option, expected_transport_option, expected_name):
    """Czy serwis produkuje odpowiedni obiekt"""

    service = service_option()
    transport = service.create_transport()

    assert isinstance(transport, expected_transport_option)
    assert service.transport_name() == expected_name

def test_service_order_available():
    """Czy zamiówiony transport zmienia status na niedostępny """

    service = BikeTransportServices()
    service.order_transport()

    assert service.available is False

def test_service_order_not_available():
    """Próba zamówienia niedostępnego transportu"""

    service = BikeTransportServices()
    service.available = False #wymusza niedostępność
    service.order_transport()

    assert service.available is False

#tests for customers

def test_customer_check():
    """Przypisywanie imienia"""

    customer = Customer("Ola")

    assert customer.name == "Ola"

