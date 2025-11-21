"""
Декоратори для пропуску

@unittest.skip(reason) - пропустити тест. reason описує причину пропуску.
@unittest.skipIf(condition, reason) - пропустити тест, якщо condition істинне.
@unittest.skipUnless(condition, reason) - пропустити тест, якщо condition хибне.
@unittest.expectedFailure - позначити тест як очікувану помилку.

Для пропущених тестів не запускаються setUp() і tearDown(). 
Для пропущених класів не запускаються setUpClass() іtearDownClass(). 
Для пропущених модулів не запускаються setUpModule() і tearDownModule().
"""

import unittest


class UserTestCase(unittest.TestCase):

    def test_example1(self):
        assert 1 == 1
        # assert 1 == 2

    def test_example2(self):
        self.assertEqual(1, 1)
        self.assertEqual('test1', 'test1')
        self.assertEqual(True, True)
        self.assertEqual({'t1': 1}, {'t1': 1})
        self.assertEqual({'t1', 1}, {1, 't1'})
        self.assertEqual(('t1', 1), ('t1', 1))
        self.assertListEqual(
            [1, 2, 3, 4, 5, 6, 7, 8, 9, 0, 1, 2, 3, 4, 5],
            [1, 2, 3, 4, 5, 6, 7, 8, 9, 0, 1, 2, 3, 4, 5]
        )
        self.assertEqual(
            {'t1': 1, 't2': 2, 't3': 3, 't4': 4, 't5': 5},
            {'t1': 1, 't2': 2, 't3': 3, 't4': 4, 't5': 5},
        )
        self.assertIsInstance('test', str)
        self.assertIs(10, 10)
        self.assertTrue(10 < 20)

        with self.assertRaises(ValueError):
            raise ValueError

        self.assertGreater(20, 10)
        self.assertGreaterEqual(20, 20)
        self.assertLess(10, 20)
        self.assertLessEqual(10, 10)

        self.assertRegex('test text', r'^test')

unittest.main(verbosity=2)
