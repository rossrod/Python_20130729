#! /usr/bin/env python3.3

def isPrime(x):
    for i in range(2, x):
        if x % i == 0:
            return False
    return True

def primesUpTo(limit):
    '''
    Calculates primes up to limit.

    Return empty tuple for limit < 2
    '''
    if limit < 2:
        return ()
    primes = [2]
    for x in range(3, limit, 2):
        if isPrime(x):
            primes.append(x)
    return tuple(primes)

def firstNPrimes(count):
    '''
    Calculates the first count primes.

    For count < 0 return empty tuple.
    '''
    if count < 1:
        return ()
    primes = [2]
    i = 3
    while len(primes) < count:
        if isPrime(i):
            primes.append(i)
        i += 2
    return tuple(primes)

if __name__ == '__main__':
    import unittest

    class PrimesUpTo_Test(unittest.TestCase):
        def test_minusOne(self):
            self.assertEqual((), primesUpTo(-1))

        def test_zero(self):
            self.assertEqual((), primesUpTo(0))

        def test_one(self):
            self.assertEqual((), primesUpTo(1))

        def test_thirty(self):
            self.assertEqual((2, 3, 5, 7, 11, 13, 17, 19, 23, 29), primesUpTo(30))


    class FirstNPrimes_Test(unittest.TestCase):
        def test_minusOne(self):
            self.assertEqual((), firstNPrimes(-1))

        def test_zero(self):
            self.assertEqual((), firstNPrimes(0))

        def test_ten(self):
            self.assertEqual((2, 3, 5, 7, 11, 13, 17, 19, 23, 29), firstNPrimes(10))


    unittest.main()
