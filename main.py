from customer import Customer
from services import BikeTransportServices

bike_transport_service = BikeTransportServices()

c1 = Customer("Albert")
c1.order_transport(bike_transport_service)

c2 = Customer("David")
c2.order_transport(bike_transport_service)