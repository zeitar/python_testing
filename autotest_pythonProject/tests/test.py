import pytest

from app.calculator import Calculator


class TestCalc:
    def setup(self):
        self.calc = Calculator

    def test_adding_success(self):
        assert self.calc.adding(self, 1, 1) == 2

    def test_multiply(self):
       self.calc.multiply(self, 1, 0) == 0

    def test_division(self):
       self.calc.division(self, 4, 2) == 2

    def test_subtraction(self):
       self.calc.multiply(self, 7, 4) == 3

    def teardown(self):
        print('Выполнение метода teardown')
