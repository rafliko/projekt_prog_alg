from customer import Customer
from services import BikeTransportServices

bts = BikeTransportServices()

c1 = Customer("Albert")
c1.order_transport(bts)

c2 = Customer("David")
c2.order_transport(bts)