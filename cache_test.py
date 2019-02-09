import unittest
from datetime import datetime, timedelta
from cache_manager import CacheManager, CacheItem


class Car:
    def __init__(self, brand, price):
        self.brand = brand
        self.price = price


class CacheTest(unittest.TestCase):
    def setUp(self):
        self.cache_manager = CacheManager()

    def test_use_cache(self):
        key1 = "honda"
        self.cache_manager.add(key1, Car(key1, 32000))
        car = self.cache_manager.get(key1)
        self.assertEqual(key1, car.brand)
        self.assertEqual(32000, car.price)
        self.cache_manager.remove(key1)
        self.assertIsNone(self.cache_manager.get(key1))

    def test_can_expire_cache(self):
        key1 = "mykey"
        self.cache_manager.add(key1, 'Value', expiry_time=timedelta(minutes=2))
        value = self.cache_manager.get(key1, current_time=datetime.now() + timedelta(minutes=5))
        self.assertIsNone(value)
