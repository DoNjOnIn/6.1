import unittest
from main import filter

class MyTestCase(unittest.TestCase):
    def test_filter(self):
        self.assertEqual(filter([2,5,9,15],0),[2,5,15])