import time
import random

class num_types(object):

    def list_prime(self, n):
        if isinstance(n, int):
            if n <= 1:
                return False
            my_arr = []
            for num in range(2, n):
                prime = True
                for i in range(2, num):
                    # if the number is divisible by any other number
                    if (num % i == 0):
                        prime = False
                if prime:
                    my_arr.append(num)
            return my_arr
        else:
            raise ValueError




# asymptotic analysis
# decided to have the code run 3 times to have 3 tests
for i in range(3):
    # generates random numbers between 3 and 1000
    n = random.randrange(3,1000)
    # the time at which the code begins to run
    start = time.time()
    num_types().list_prime(n)
    # the time at which the code stops running
    end = time.time()
    print('when the range is 2 to {} it takes {} \n'.format(n, (end - start)))


