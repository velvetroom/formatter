import unittest
from formatter import fibonacci

class Tests(unittest.TestCase):
	def test(self):
		self.assertEqual(2, fibonacci(1))
