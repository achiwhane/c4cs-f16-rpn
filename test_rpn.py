import unittest
import rpn

class TestBasics(unittest.TestCase):

    def test_add(self):
        result = rpn.calculate("1 1 +")
        self.assertEqual(2, result)


    def test_subtract(self):
        result = rpn.calculate("5 3 -")
        self.assertEqual(2, result)


    def test_multiply(self):
        result = rpn.calculate("2 -3 *")
        self.assertEqual(-6, result)


    def test_divide(self):
        result = rpn.calculate("3 6 /")
        self.assertEqual(0.5, result)

    def test_exponentiate(self):
        result = rpn.calculate("2 3 ^")
        self.assertEqual(8, result)


    def test_too_many_things(self):
        with self.assertRaises(TypeError):
            rpn.calculate("1 2 3 +")
