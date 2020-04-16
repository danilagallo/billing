import datetime

from src.invoice_header import InvoiceHeader
from src.utils import Utils
from src.invoice_detail import InvoiceDetail
from src.invoice import Invoice
from src.invoice_footer import InvoiceFooter


class Billing:
    def __init__(self):
        self.invoice_list: list()

    def make_invoices(self, orders: list):
        i = 1
        code = 1
        for order in orders:
            # create invoice header

            letter = "A"

            header = InvoiceHeader(
                datetime.datetime.now(),
                i,
                code,
                letter,
                order.client
            )

            # create details header
            calculations = Utils.get_all(
                order.product_detail.product.code,
                order.product_detail.product.price,
                order.product_detail.quantity
            )

            detail = InvoiceDetail(
                order.order_number,
                order.product_detail.product,
                order.product_detail.product.price,
                calculations["vat"],
                order.product_detail.quantity,
                calculations["sale_price"],
                calculations["net_price"],
                calculations["vat_value"],
            )

            # create invoice footer
            # total = price * quantity
            total = order.product_detail.product.price * order.product_detail.quantity,
            footer = InvoiceFooter(
                total,
                # total VAT = total + vat_value
                total + calculations["vat_value"]
            )

            invoice = Invoice(header, detail, footer)
            self.invoice_list.append(invoice)
            i += 1
            code += 1
            

    def cancel_invoices(self, invoices: list):
        pass

    def generate_operations(self):
        pass
