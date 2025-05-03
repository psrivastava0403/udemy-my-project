#this is sample test

from django.test import SimpleTestCase # type: ignore

from app import calc

class CalcTests(SimpleTestCase):

    def test_add_number(self):
        res = calc.calculate(5, 6)
        self.assertEqual(res, 30)


    def test_calculator(self):
        res = calc.calculate_auto("substract", 5, 3)
        self.assertEqual(res,2)

    def test_calculator_error(self):
        res = calc.calculate_auto("divide", 5, "a")
        self.assertEqual(res, "Invalid pass variable value")