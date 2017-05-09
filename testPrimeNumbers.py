import unittest
import PrimeNumbers

# testcases

# 1. When someone enters 1
# 2. When someone enters a -ve number
# 3. Enter a range and test the expected outputs
# 4. When a string is entered instead of an int
# 5. when number is a decimal or fraction

class primeTestCases(object):
    def setUp(self):
        self.prime = PrimeNumbers.list_prime()

    
    def test_list_prime_check_expected_output(self):
        result = self.prime.list_prime(6)
        self.assertEqual([2, 3, 5], result)
        pass


if __name__ == '__main__':
    unittest.main()