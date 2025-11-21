import unittest


def test_function(value):
    return value * 20


class UserTestCase(unittest.TestCase):

    def test_sum(self):
        self.assertEqual(2 + 2, 4)

    def test_multiply(self):
        self.assertTrue(2 * 4 == 8)

    def test_test_function(self):
        value = 100
        self.assertEqual(test_function(value), value * 20)

    def test_test_function_wrong(self):
        value = 100
        self.assertNotEqual(test_function(value), value * 30)

def sum_two_values(a, b):
    return a + b


def power(x, n):
    return x ** n


def concat_values(*args):
    result = ''
    for item in args:
        result += str(item)
    return result


def desc(x, y):
    if x == 0:
        raise ValueError('`x` should not be equal 0')
    return y / x


class UtilsTestCase(unittest.TestCase):

    def test_sum_two_values(self):
        value1 = 10
        value2 = 20
        result = sum_two_values(value1, value2)
        self.assertEqual(result, value1 + value2)

    def test_power(self):
        value = 2
        st = 8
        result = power(value, st)
        expected_value = value ** st
        self.assertEqual(result, expected_value)

    def test_concat_values(self):
        values = 1, 2, 3, 4
        result = concat_values(*values)
        expected_result = '1234'
        self.assertEqual(result, expected_result)

    def test_desc(self):
        x, y = 10, 20
        result = desc(x, y)
        expected_result = y / x
        self.assertEqual(result, expected_result)

    def test_desc_with_zero(self):
        with self.assertRaises(ValueError):
            desc(0, 20)

unittest.main(verbosity=2)