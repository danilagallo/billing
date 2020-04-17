import datetime
import threading

from src.credit_note import CreditNote
from src.credit_note_footer import CreditNoteFooter
from src.credit_note_header import CreditNoteHeader
from src.invoice_header import InvoiceHeader
from src.utils import Utils
from src.invoice_detail import InvoiceDetail
from src.invoice import Invoice
from src.invoice_footer import InvoiceFooter


class Billing:
    def __init__(self):
        self.invoice_list: list()
        self.invoice_dict = dict()
        self.credit_notes_dict = dict()
        filename = f"{datetime.datetime.now().date()}_{datetime.datetime.now().time()}-operations.out"
        self.file = open(filename, "w")

    def make_invoices(self, orders: list, number_threads=4, min_number_for_thread=100):
        """
        Execute the billing process with threads according to the number of invoices
        :param orders: list of invoices
        :param number_threads: by default 4 threads
        :param min_number_for_thread: by default 100 es the min value to use a thread
        in the execution billing process
        :return: None
        """
        n = len(orders)
        if n < min_number_for_thread:
            self.__real_make_invoices(orders)
        else:
            increment = n // number_threads
            i = 0
            start = 0
            end = increment
            thread_list = []

            while i <= number_threads:
                suborder = orders[start:end]
                start = end
                end += increment
                i += 1
                if len(suborder):
                    thr = threading.Thread(
                        target=self.__real_make_invoices,
                        args=(orders[start:end],)
                    )
                    thr.start()
                    thread_list.append(thr)

            for thr in thread_list:
                thr.join()

    def __real_make_invoices(self, orders: list):
        """
        Execute the billing process for a group of list of invoices
        :param orders: list of invoice.Invoice object
        :return: None
        """
        i = len(self.invoice_dict.keys()) + 1
        code = i
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
            self.invoice_dict[i](invoice)
            i += 1
            code += 1

    def cancel_invoices(self, invoices: list):
        """
        Cancel invoices. The status of invoices is set to canceled
        :param invoices: list of invoice numbers to cancel
        :return: None
        """
        for invoice_number in invoices:
            if invoice_number in self.invoice_dict.keys():
                invoice = self.invoice_dict[invoice_number]
                invoice.status = "canceled"

                # create notes of credit
                # create credit note header
                i = len(self.credit_notes_dict.keys()) + 1
                j = 1
                note_header = CreditNoteHeader(
                    datetime.datetime.now(),
                    i,
                    j,
                    invoice.invoice_header.letter,
                    invoice.invoice_header.client
                )

                # create credit note footer
                note_footer = CreditNoteFooter(
                    invoice.invoice_footer.total
                )

                self.credit_notes_dict[i] = CreditNote(
                    note_header, note_footer
                )

    def generate_operations(self):
        """
        Generate the operations of the day
        every line of the file has the following format
        client_number-document_type-letter-issue_date
        :return: None
        """
        for invoice in self.invoice_dict:
            client = invoice.invoice_header.client
            client_number = client.client_number
            document_type = client.identity_type
            letter = invoice.invoice_header.letter
            issue_date = invoice.invoice_header.issue_date
            self.file.write(
                f"{client_number}-{document_type}-{letter}-{issue_date} \n"
            )
        self.file.close()
