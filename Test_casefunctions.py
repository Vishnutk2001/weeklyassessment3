import Functions
import unittest

class check_armstrong(unittest.TestCase):
    def setUp(self):
        self.num1 = 371
        self.num2 = 125


    def tearDown(self):
        self.num1 = 0
        self.num2 = 0

    def test_case_armstrong(self):
        result = Functions.armstrong_number(self.num1)
        self.assertEqual(result,"Armstrong number")

    def test_case_notarmstrong(self):
        result = Functions.armstrong_number(self.num2)
        self.assertEqual(result,"not an Armstrong number")


class check_divisible(unittest.TestCase):
    def setUp(self):
        self.num1 = 125
        self.num2 = 12


    def tearDown(self):
        self.num1 = 0
        self.num2 = 0

    def test_case_divisible(self):
        result = Functions.divisible(self.num1)
        self.assertTrue(result,"divisible")

    def test_case_notdivisible(self):
        result = Functions.divisible(self.num2)
        self.assertTrue(result, "not divisible")


class Largest(unittest.TestCase):
    def setUp(self):
        self.a = 10
        self.b = 20
        self.c = 30

    def tearDown(self):
        self.a = 0
        self.b = 0
        self.c = 0

    def test_case_largest(self):
        result = Functions.Largest(self.a,self.b,self.c)
        self.assertEqual(result,self.c)

class check_even_odd(unittest.TestCase):
    def setUp(self):
        self.a = 10
        self.b = 15

    def tearDown(self):
        self.a = 0
        self.b = 0

    def test_case_even(self):
        result = Functions.evenorodd(self.a)
        self.assertEqual(result,"even")

    def test_case_odd(self):
        result = Functions.evenorodd(self.b)
        self.assertEqual(result,"odd")

if __name__ == "__main__":
    unittest.main()
