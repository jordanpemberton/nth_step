import unittest
from nth_step import nth_step


class TestNthStep(unittest.TestCase):
    """
    Testing the nth_step function.
    """
    pass


def clear_outfile(out_src):
    outfile = open(out_src, 'w')
    outfile.write('')


def write_output(inp, out, exp, out_src):
    # Append to end of out file:
    outfile = open(out_src, 'a')
    outfile.write('input: ' + str(inp) + ',  ')
    outfile.write('output: ' + str(out) + ',  ')
    outfile.write('expected: ' + str(exp) + '\n')
    outfile.close()


def create_test_case(data, func, outfile=''):
    def test(self):
        inp, exp = data
        out = func(*inp)     # expand input
        # Output to text file:
        write_output(inp, out, exp, outfile)
        self.assertEqual(out, exp)
    return test


def make_tests(data, func, outfile=''):
    for k, pair in enumerate(data):
        test = create_test_case(pair, func, outfile)
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

    # Clear the output file:
    clear_outfile('nth_step_output.txt')

    make_tests(data, nth_step, 'nth_step_output.txt')

    unittest.main()
