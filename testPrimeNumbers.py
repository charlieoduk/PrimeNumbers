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
    
    def test_list_prime_check_613_is_prime(self):
        sixthirteen = self.prime.list_prime(615)
        self.assertIn(613, sixthirteen)
    def test_list_prime_check_if_0_is_a_prime_number(self):
        self.assertNotIn(0, self.prime.list_prime(5))
    
    def test_list_prime_check_when_you_get_negative_input(self):
        self.assertFalse(self.prime.list_prime(-5))

    def test_list_prime_check_if_string_entered(self):
        self.assertRaises(ValueError, self.prime.list_prime, "5")

if __name__ == '__main__':
    unittest.main()