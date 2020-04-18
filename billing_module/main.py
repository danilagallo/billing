from src.billing import Billing

if __name__ == "__main__":

    orders = []
    list_to_cancel = []

    billing = Billing()
    billing.make_invoices(orders)
    billing.cancel_invoices()
    billing.generate_operations()

