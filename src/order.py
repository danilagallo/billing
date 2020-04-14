from src.client import Client
from src.product_detail import ProductDetail


class Order:

    def __init__(self, order_number, client: Client, product_detail:  ProductDetail):
        self.order_number = order_number
        self.client = client
        self.product_detail = product_detail
