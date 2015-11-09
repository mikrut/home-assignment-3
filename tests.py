import unittest
from calculator import Calculator, Operations, InputError, EvaluationError

class TestCalculator(unittest.TestCase):
    def setUp(self):
        self.calc = Calculator()

    def test_input_integer(self):
        self.calc.inputDigit(2)
        self.calc.execute_operation(Operations.EQUALS)
        self.assertEqual(self.calc.inMemoryNumber, 2)

    def test_input_not_digit(self):
        self.assertRaises(InputError, self.calc.inputDigit, 10)

    def test_input_not_digit_less_zero(self):
        self.assertRaises(InputError, self.calc.inputDigit, -2)

    def test_input_with_plus(self):
        self.calc.execute_operation(Operations.ADDITION)
        self.calc.inputDigit(1)
        self.calc.execute_operation(Operations.EQUALS)
        self.assertEqual(self.calc.inMemoryNumber, 1)

    def test_input_with_minus(self):
        self.calc.execute_operation(Operations.SUBTRACTION)
        self.calc.inputDigit(3)
        self.calc.execute_operation(Operations.EQUALS)
        self.assertEqual(self.calc.inMemoryNumber, -3)

    def test_input_with_multiply(self):
        self.calc.execute_operation(Operations.MULTIPLICATION)
        self.calc.inputDigit(2)
        self.calc.execute_operation(Operations.EQUALS)
        self.assertEqual(self.calc.inMemoryNumber, 0)

    def test_input_with_divide(self):
        self.calc.execute_operation(Operations.DIVISION)
        self.calc.inputDigit(5)
        self.calc.execute_operation(Operations.EQUALS)
        self.assertEqual(self.calc.inMemoryNumber, 0)

    def test_integer_addition(self):
        self.calc.inputDigit(1)
        self.calc.execute_operation(Operations.ADDITION)
        self.calc.inputDigit(2)
        self.calc.execute_operation(Operations.EQUALS)
        self.assertEqual(self.calc.inMemoryNumber, 3)

    def test_integer_subtraction(self):
        self.calc.inputDigit(1)
        self.calc.execute_operation(Operations.SUBTRACTION)
        self.calc.inputDigit(2)
        self.calc.execute_operation(Operations.EQUALS)
        self.assertEqual(self.calc.inMemoryNumber, -1)

    def test_integer_multiply_integer(self):
        self.calc.inputDigit(5)
        self.calc.execute_operation(Operations.MULTIPLICATION)
        self.calc.inputDigit(3)
        self.calc.execute_operation(Operations.EQUALS)
        self.assertEqual(self.calc.inMemoryNumber, 15)

    def test_integer_divide_zero(self):
        self.calc.inputDigit(1)
        self.calc.inputDigit(0)
        self.calc.execute_operation(Operations.DIVISION)
        self.calc.inputDigit(0)
        self.assertRaises(EvaluationError, self.calc.execute_operation, Operations.EQUALS)

    def test_integer_divide_integer(self):
        self.calc.inputDigit(1)
        self.calc.inputDigit(0)
        self.calc.execute_operation(Operations.DIVISION)
        self.calc.inputDigit(2)
        self.calc.execute_operation(Operations.EQUALS)
        self.assertEqual(self.calc.inMemoryNumber, 5)

    def test_rational_input(self):
        self.calc.inputDigit(3)
        self.calc.click_dot()
        self.calc.inputDigit(1)
        self.calc.inputDigit(4)
        self.assertEqual(self.calc.inputNumber, 3.14)

    def test_ratonal_input_two_dots(self):
        self.calc.inputDigit(3)
        self.calc.click_dot()
        self.calc.inputDigit(1)
        self.calc.click_dot()
        self.calc.inputDigit(4)
        self.assertEqual(self.calc.inputNumber, 3.14)

    def test_rational_addition(self):
        self.calc.inputDigit(3)
        self.calc.click_dot()
        self.calc.inputDigit(2)
        self.calc.execute_operation(Operations.ADDITION)
        self.calc.inputDigit(1)
        self.calc.execute_operation(Operations.EQUALS)
        self.assertEqual(self.calc.inMemoryNumber, 4.2)

    def test_log_evaluation(self):
        self.calc.inputDigit(2)
        self.calc.execute_operation(Operations.LOG)
        self.calc.inputDigit(4)
        self.calc.execute_operation(Operations.EQUALS)
        self.assertEqual(self.calc.inMemoryNumber, 2)

    def test_log_filters_minus_x(self):
        self.calc.execute_operation(Operations.SUBTRACTION)
        self.calc.inputDigit(2)
        self.calc.execute_operation(Operations.EQUALS)
        self.calc.execute_operation(Operations.LOG)
        self.calc.inputDigit(4)
        self.assertRaises(EvaluationError, self.calc.execute_operation, Operations.EQUALS)

    def test_log_filters_zero_x(self):
        self.calc.execute_operation(Operations.LOG)
        self.calc.inputDigit(4)
        self.assertRaises(EvaluationError, self.calc.execute_operation, Operations.EQUALS)

    def test_log_filters_zero_y(self):
        self.calc.inputDigit(2)
        self.calc.execute_operation(Operations.LOG)
        self.assertRaises(EvaluationError, self.calc.execute_operation, Operations.EQUALS)

    def test_two_sequential_evaluations(self):
        self.calc.inputDigit(2)
        self.calc.execute_operation(Operations.ADDITION)
        self.calc.inputDigit(3)
        self.calc.execute_operation(Operations.SUBTRACTION)
        self.calc.inputDigit(8)
        self.calc.execute_operation(Operations.EQUALS)
        self.assertEquals(self.calc.inMemoryNumber, -3)
