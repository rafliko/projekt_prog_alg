class Customer:
    """
    Klasa reprezentująca klienta.

    Attributes:
        name (string): Nazwa klienta.
    """
    def __init__(self, name):
        """
        Inicjalizacja klasy klienta.

        Parameters:
            name (string): Nazwa klienta.
        """
        self.name = name

    def order_transport(self, service):
        """
        Metoda zamawiająca transport dla klienta.

        Parameters:
            service (TransportServices): Obiekt dziedziczący po klasie abstrakcyjnej TransportServices.
        """
        service.order_transport()