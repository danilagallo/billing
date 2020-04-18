import unittest
from tests.test_billing_process import TestsBillingProcess
from tests.test_multithread_process import TestsThreadBillingProcess


def group_of_test():
    group = unittest.TestSuite()
    group.addTest(TestsBillingProcess("test_make_invoices"))
    group.addTest(TestsBillingProcess("test_cancel_invoices"))
    group.addTest(TestsBillingProcess("test_generate_files"))
    group.addTest(TestsThreadBillingProcess("test_thread_make_invoices"))
    return group


if __name__ == '__main__':
    runner = unittest.TextTestRunner()
    runner.run(group_of_test())

