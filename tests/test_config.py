import unittest
from config import config

class TestConfig(unittest.TestCase):
    def test_config_contain_keys(self):
        self.assertIsNotNone(config.binance_api_key)
        self.assertIsNotNone(config.binance_api_secret)