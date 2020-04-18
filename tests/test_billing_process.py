import unittest

from billing_module import billing


class TestsBillingProcess(unittest.TestCase):

    billing_instance = billing.Billing()

    def test_make_invoices(self):
        """
        The idea is:
            - generate an orders lists of know number
            - use the instance of the billing.Billing and make_invoices
            - and then compare:
                - the count of the orders list
                - the count of invoices generated
            - success if both count are equal
        :return:
        """
        self.assertEqual(sum([1, 2, 3]), 7, "Should be 6")

    def test_cancel_invoices(self):
        """
        The idea is:
           - generate a random number less than N, N = invoices count generated before
                to use as a number of invoices to cancel.
           - use the billing instance an cancel the N invoices
           - and then compare:
               - N
               - the count of invoices in canceled status
        :return:
        """
        self.assertEqual(sum((1, 2, 2)), 6, "Should be 6")

    def test_generate_files(self):
        """
        The idea is:
           - call the generate operation method after call
                - make_invoices
                - cancel_invoices
           - check if the lines of the generated files are equal to the non-canceled invoices
           - check if the file was generated with the format of:
                - client_number-document_type-letter-issue_date
        :return:
        """
        self.assertEqual(sum((1, 2, 2)), 1, "Should be 6")
