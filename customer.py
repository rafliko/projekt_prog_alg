class Customer:
    def __init__(self, name):
        self.name = name

    def order_transport(self, service):
        return service.order_transport()