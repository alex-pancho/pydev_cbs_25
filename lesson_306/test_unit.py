import unittest
from our_function import sum_list_last_first

class SumListTest(unittest.TestCase):

    def test_01_tree(self):
        """
        Test sum_list_last_first with a list of three elements
        """
        my_list = [1, 2, 3]
        actual = sum_list_last_first(my_list)
        expected = 1.5
        self.assertEqual(actual, expected)
    
    def test_02_two(self):
        """
        Test sum_list_last_first with a list of two elements
        """
        my_list = [1, 2]
        actual = sum_list_last_first(my_list)
        expected = 1.0
        self.assertEqual(actual, expected)
    
    def test_03_one(self):
        my_list = [1]
        actual = sum_list_last_first(my_list)
        self.assertIsNone(actual)

    def test_04_zerro_div_err(self):
        """
        Test for ZeroDivisionError
        """
        my_list = [3, 5, -3]
        with self.assertRaises(
                ZeroDivisionError
            ) as zde:
            sum_list_last_first(my_list)


    def test_05_val_err(self):
        """
        Test for ValueError
        """
        my_list = {3, 5, -3}
        with self.assertRaises(
                ValueError
            ) as ve:
            sum_list_last_first(my_list)
    

if __name__ == "__main__":
    unittest.main(verbosity=2)
    # Can be false-positive
    # self.assertTrue
    # self.assertNotEqual
    # self.assertIsNotNone
