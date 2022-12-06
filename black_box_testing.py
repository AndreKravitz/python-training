import unittest


def sum(num_1, num_2):
    return num_1 + num_2

# INPUT AND OUTPUT TESTING


class Black_Box_Testing(unittest.TestCase):

    def test_sum_two_positive_int(self):
        num_1 = 30
        num_2 = 20

        result = sum(num_1, num_2)

        self.assertEqual(result, 50)

    def test_sum_two_negative_int(self):
        num_1 = -10
        num_2 = -5

        result = sum(num_1, num_2)

        self.assertEqual(result, -15)


if __name__ == '__main__':
    unittest.main()
