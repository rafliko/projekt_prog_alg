# Projekt - wzorzec projektowy Factory Method

---

## Instrukcja uruchomienia
Uruchom plik main.py (projekt nie korzysta z zewnętrznych bibliotek):
```commandline
python main.py
```

---

## Wzorzec Factory Method
Factory Method jest kreacyjnym wzorcem projektowym, 
który udostępnia interfejs do tworzenia obiektów w ramach klasy bazowej, 
ale pozwala podklasom zmieniać typ tworzonych obiektów.

Ten projekt implementuje wzorzec Factory Method poprzez abstrakyjną klasę *TransportServices*
oraz dziedziczące po niej klasy *BikeTransportServices*, *CarTransportServices* oraz *ScooterTransportServices*.

---

## Przykłady działania
### 1. Dwukrotne wywołanie metody *order_transport*
Poniższy przykład prezentuje działanie metody *order_transport*
wywołanej dwukrotnie z tym samym obiektem klasy *BikeTransportServices*.
```python
from customer import Customer
from services import BikeTransportServices
from services import CarTransportServices
from services import ScooterTransportServices

bike_transport_service = BikeTransportServices()

c1 = Customer("Albert")
c1.order_transport(bike_transport_service)

c2 = Customer("David")
c2.order_transport(bike_transport_service)
```
Wynik:
```commandline
Transport: Bike, available: True
Arrival time: 8:00
Trip time: 4h
Transport unavailable
```
Metoda *order_transport* wyświetla informacje o zamówionym transporcie.
Raz zamówiony transport staje się niedostępny i wyświetla komunikat *'Transport unavailable'*.
### 2. Zamawianie wielu środków transportu
Poniższy przykład prezentuje zamawianie wielu środków transportu przez jednego klienta.
```python
from customer import Customer
from services import BikeTransportServices
from services import CarTransportServices
from services import ScooterTransportServices

bike_transport_service = BikeTransportServices()
car_transport_service = CarTransportServices()
scooter_transport_service = ScooterTransportServices()

c1 = Customer("Albert")
c1.order_transport(bike_transport_service)
c1.order_transport(car_transport_service)
c1.order_transport(scooter_transport_service)
```
Wynik:
```commandline
Transport: Bike, available: True
Arrival time: 8:00
Trip time: 4h
Transport: Car, available: True
Arrival time: 5:00
Trip time: 1h
Transport: Scooter, available: True
Arrival time: 6:00
Trip time: 2h
```