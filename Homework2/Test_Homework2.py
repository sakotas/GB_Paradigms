import unittest
import Homework2


# Класс для юнит-тестирования
class TestMultiplicationTable(unittest.TestCase):
    def test_multiplication_table(self):
        expected_output = "1 * 1 = 1\n1 * 2 = 2\n\n2 * 1 = 2\n2 * 2 = 4\n\n"
        self.assertEqual(Homework2.multiplication_table(2), expected_output)


if __name__ == '__main__':
    unittest.main()
