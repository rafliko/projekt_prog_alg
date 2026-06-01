class Customer:
    """
    Klasa reprezentująca klenta.

    Attributes:
        name (string): Nazwa klienta.
    """
    def __init__(self, name):
        """
        Inicjalizacja klasy klienta.

        Parameters:
            name (int): Nazwa klienta.
        """
        self.name = name

    def order_transport(self, service):
        """
        Metoda zamawiajaaca transport dla klienta.

        Parameters:
            service (TransportServices): Obiekt dziedziczący po klasie abstrakcyjnej TransportServices.
        """
        service.order_transport()