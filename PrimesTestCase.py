#import unittest 
from prime import is_prime 
import unittest
class PrimesTestCase(unittest.TestCase):
   def test_is_five_prime(self):    
      self.assertTrue(is_prime(5)) 

if __name__ == '__main__':
	unittest.main()
