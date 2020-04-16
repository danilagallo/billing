class Utils:

    @staticmethod
    def percent_vat(self, code):
        if code == 1:
            return 10.05
        elif code == 2:
            return 21
        elif code == 3:
            return 70

    @staticmethod
    def calculate_vat_value(self, code, price):
        if code == 1:
            return price * 0.1005
        elif code == 2:
            return price * 0.21
        elif code == 3:
            return price * 0.70

    @staticmethod
    def calculate_net_price(self, price, quantity):
        return price * quantity

    @staticmethod
    def calculate_sale_price(self, net_price, vat_value):
        return net_price + vat_value

    @staticmethod
    def get_all(self, code, price, quantity):

        vat_value = Utils.calculate_vat_value(code, price)
        net_price = Utils.calculate_net_price(code, quantity)
        vat = Utils.percent_vat(code)
        return {
            "vat_value": vat_value,
            "net_price": net_price,
            "sale_price": net_price + vat_value,
            "vat": vat
        }
