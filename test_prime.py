import unittest

from prime import is_prime


class TestPrime(unittest.TestCase):

    def test_is_prime(self):
        self.assertFalse(is_prime(1))
        self.assertTrue(is_prime(2))
        self.assertTrue(is_prime(3))
        self.assertFalse(is_prime(4))
        self.assertTrue(is_prime(5))
        self.assertFalse(is_prime(6))
        self.assertTrue(is_prime(7))
        self.assertFalse(is_prime(8))
        self.assertFalse(is_prime(9))
        self.assertFalse(is_prime(10))
        self.assertTrue(is_prime(11))
        self.assertTrue(is_prime(13))
        self.assertTrue(is_prime(17))
        self.assertTrue(is_prime(19))
        self.assertTrue(is_prime(23))
        self.assertFalse(is_prime(25))
        self.assertTrue(is_prime(29))
        self.assertFalse(is_prime(30))
        self.assertTrue(is_prime(31))
        self.assertFalse(is_prime(33))
        self.assertTrue(is_prime(37))
        self.assertTrue(is_prime(41))
        self.assertTrue(is_prime(43))
        self.assertFalse(is_prime(49))
        self.assertTrue(is_prime(53))
        # 他のテストケースも同様に追加


if __name__ == "__main__":
    unittest.main()
