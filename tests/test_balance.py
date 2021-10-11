import unittest

from utils.get_balance import get_balance

class TestBalance(unittest.TestCase):
    res = get_balance()
    self.assertIsNotNone(res)
    self.assertIsNotNone(res['balances'])
    self.assertTrue(res['balances'] > 0)
