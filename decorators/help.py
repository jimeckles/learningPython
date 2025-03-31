from functools import lru_cache, wraps
import time
import unittest


# 6th fibby is "8"
# 0, 1, 2, 3, 4, 5, 6,  7, 8 -F postition
# 0, 1, 1, 2, 3, 5, 8, 13,
# print(fibonacci(6, getNextFunc()))
# myFib(6)


def timer(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        start = time.time_ns()
        result = func(*args, **kwargs)
        end = time.time_ns()
        nonoSecondsElapse = end - start
        print(f"Execution time of {func.__name__}: {nonoSecondsElapse:0.4f} seconds")
        return result

    return wrapper


@timer
@lru_cache(maxsize=None)
def fibonacci(n):
    """Returns the nth Fibonacci number"""
    print("Calculating F", "(", n, ")", sep="", end=", ")
    if n == 0 or n == 1:
        return n
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)


@timer
def myFib(n):
    if n == 0 or n == 1:
        return n
    a, b = 0, 1
    for _ in range(0, n):
        a, b = b, a + b
    return a



class TestLearning(unittest.TestCase):

    def test_fib_6(self):

        fibonacciVal = myFib(6)
        self.assertEqual(8, fibonacciVal)

    def test_fib_0(self):

        fibonacciVal = myFib(0)
        self.assertEqual(0, fibonacciVal)

    def test_fib_1(self):

        fibonacciVal = myFib(1)
        self.assertEqual(1, fibonacciVal)

    def test_fib_2(self):

        fibonacciVal = myFib(2)
        self.assertEqual(1, fibonacciVal)

    def test_fib_3(self):

        fibonacciVal = myFib(3)
        self.assertEqual(2, fibonacciVal)

    def test_fib_fibonacci(self):

        fibonacciVal = fibonacci(3)
        self.assertEqual(2, fibonacciVal)
    def test_fib_fibonacci_25(self):

        fibonacciVal = fibonacci(25)
        print('here' + str(fibonacciVal))


if __name__ == "__main__":
    unittest.main()
