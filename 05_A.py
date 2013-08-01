#! /usr/bin/env python3

from functools import reduce
from operator import mul

def _validate(x):
    '''
    Data validation for factorial parameters.
    '''
    if not isinstance(x, int):
        raise ValueError('Factorial only defined for nonnegative integers.')
    if x < 0:
        raise ValueError('Negative values not defined.')

def iterative(x):
    '''
    Factorial iterative implementation.
    '''
    _validate(x)
    if x < 2:
        return 1
    t = 1
    for i in range(2, x+1):
        t *= i
    return t

def recursive(x):
    '''
    Factorial using a recursive implementation.
    '''
    _validate(x)
    if x < 2:
        return 1
    return x * recursive(x -1)

def reduction(x):
    _validate(x)
    if x < 2:
        return 1
    return reduce(mul, range(2, x+1))

if __name__ == '__main__':
    from unittest import TestCase, main

    class Recursive_Test(TestCase):
        def test_zero(self):
            self.assertEqual(1, recursive(0))

        def test_one(self):
            self.assertEqual(1, recursive(1))

        def test_two(self):
            self.assertEqual(2, recursive(2))

        def test_three(self):
            self.assertEqual(6, recursive(3))

        def test_seven(self):
            self.assertEqual(5040, recursive(7))

        def test_twenty(self):
            self.assertEqual(2432902008176640000, recursive(20))

        def test_None(self):
            self.assertRaises(ValueError, recursive, None)

        def test_onePointFive(self):
            self.assertRaises(ValueError, recursive, 1.5)

        #def test_onethousand(self):
        #    recursive(1000)


    class Iterative_Test(TestCase):

        def test_None(self):
            self.assertRaises(ValueError, iterative, None)

        def test_minusOne(self):
            self.assertRaises(ValueError, iterative, -1)

        def test_zero(self):
            self.assertEqual(1, iterative(0))

        def test_one(self):
            self.assertEqual(1, iterative(1))

        def test_two(self):
            self.assertEqual(2, iterative(2))

        def test_three(self):
            self.assertEqual(6, iterative(3))

        def test_seven(self):
            self.assertEqual(5040, iterative(7))

        def test_twenty(self):
            self.assertEqual(2432902008176640000, iterative(20))

        def test_onePointFive(self):
            self.assertRaises(ValueError, iterative, 1.5)


    class Reduction_Test(TestCase):

        def test_None(self):
            self.assertRaises(ValueError, reduction, None)

        def test_minusOne(self):
            self.assertRaises(ValueError, reduction, -1)

        def test_zero(self):
            self.assertEqual(1, reduction(0))

        def test_one(self):
            self.assertEqual(1, reduction(1))

        def test_two(self):
            self.assertEqual(2, reduction(2))

        def test_three(self):
            self.assertEqual(6, reduction(3))

        def test_seven(self):
            self.assertEqual(5040, reduction(7))

        def test_twenty(self):
            self.assertEqual(2432902008176640000, reduction(20))

        def test_onePointFive(self):
            self.assertRaises(ValueError, reduction, 1.5)



    main()
