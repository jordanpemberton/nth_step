import unittest
from nth_step import nth_step


class TestNthStep(unittest.TestCase):
    """
    Testing the nth_step function.
    """
    pass


def create_test_case(data, func):
    def test(self):
        inp, exp = data
        actual = func(*inp)     # expand input
        self.assertEqual(actual, exp)
    return test


def make_tests(data, func):
    for k, pair in enumerate(data):
        test = create_test_case(pair, func)
        test.__name__ = 'test_' + str(func.__name__) + str(k)
        setattr(TestNthStep, test.__name__, test)


if __name__ == '__main__':
    # Input and expected results, testing
    # nth_step func from 0..9, 1 or 2 steps:
    data = [
            ([0, 2], 1),
            ([1, 2], 1),
            ([2, 2], 2),
            ([3, 2], 3),
            ([4, 2], 5),
            ([5, 2], 8),
            ([6, 2], 13),
            ([7, 2], 21),
            ([8, 2], 34),
            ([9, 2], 55)
           ]

    make_tests(data, nth_step)

    unittest.main()
