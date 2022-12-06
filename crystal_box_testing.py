import unittest


def is_adult(age):
    if age >= 21:
        return True
    else:
        return False

# FLOW TESTING


class Crystal_Box_Testing(unittest.TestCase):

    def test_is_adult(self):
        age = 23

        result = is_adult(age)

        self.assertEqual(result, True)

    def test_not_adult(self):
        age = 13

        result = is_adult(age)

        self.assertEqual(result, False)


if __name__ == '__main__':
    unittest.main()
