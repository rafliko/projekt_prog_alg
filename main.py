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