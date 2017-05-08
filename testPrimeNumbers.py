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

    def test_list_prime_prints_prime_numbers(self):
        pass

    def test_list_prime_check_if_1_is_prime(self):
        pass

    def test_list_prime_check_if_negative_number_is_prime(self):
        pass

    def test_list_prime_check_when_string_is_entered(self):
        pass

    def test_list_prime_check_when_number_entered_is_decimal(self):
        pass


if __name__ == '__main__':
    unittest.main()