from src.billing import Billing

if __name__ == "__main__":

    orders = []

    billing = Billing()
    billing.make_invoices(orders)
