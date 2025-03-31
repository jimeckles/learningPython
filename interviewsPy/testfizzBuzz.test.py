import unittest
from fizzBuzz import fizzBuzz


class TestFizzBuzz(unittest.TestCase):

    # def test_fizzBuzz_15(self):
    #     expected = [
    #         "1",
    #         "2",
    #         "Fizz",
    #         "4",
    #         "Buzz",
    #         "Fizz",
    #         "7",
    #         "8",
    #         "Fizz",
    #         "Buzz",
    #         "11",
    #         "Fizz",
    #         "13",
    #         "14",
    #         "FizzBuzz",
    #     ]
    #     self.assertEqual(fizzBuzz(15), expected)

    # def test_fizzBuzz_3(self):
    #     expected = ["1", "2", "Fizz"]
    #     self.assertEqual(fizzBuzz(3), expected)

    # def test_fizzBuzz_5(self):
    #     expected = ["1", "2", "Fizz", "4", "Buzz"]
    #     self.assertEqual(fizzBuzz(5), expected)

    # def test_fizzBuzz_0(self):
    #     expected = []
    #     self.assertEqual(fizzBuzz(0), expected)

    # def test_fizzBuzz_negative(self):
    #     expected = []
    #     self.assertEqual(fizzBuzz(-1), expected)

    def test_fizzBuzz_53_FizzBuzz(self):
        expected = "FizzBuzz"
        last_element = fizzBuzz(53)[-1]
        self.assertEqual(last_element, expected)


if __name__ == "__main__":
    unittest.main()
