from customer import Customer
from services import BikeTransportServices

c1 = Customer("Albert")
b1 = c1.order_transport(BikeTransportServices())
print(f"Arrival time: {b1.arrival_time()}")
print(f"Trip time: {b1.trip_time()}")