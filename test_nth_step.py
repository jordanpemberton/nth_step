"""
Jordan Pemberton
CS325 Algorithms
Extra Credit: Nth Step Problem
"""


import unittest
from nth_step import nth_step
from nth_step_math import nth_step_math


class TestNthStep(unittest.TestCase):
    """
    Testing the nth_step function.
    """
    pass


def clear_outfile(out_src):
    """
    Clear the given file by overwriting.
    """
    outfile = open(out_src, 'w')
    outfile.write('')
    outfile.close()


def write_header(out_src, header):
    """
    Append a given line to the passed file.
    """
    outfile = open(out_src, 'a')
    outfile.write('\n' + header + '\n')
    outfile.close()


def write_output(inp, out, exp, out_src):
    """
    Append a inp, out, and exp line to out file.
    """
    # Append to end of out file:
    outfile = open(out_src, 'a')
    outfile.write('input: ' + str(inp) + ',  ')
    outfile.write('output: ' + str(out) + ',  ')
    outfile.write('expected: ' + str(exp) + '\n')
    outfile.close()


def create_test_case(data, func, outfile=''):
    """
    Returns a test case function.
    """
    def test(self):
        inp, exp = data
        out = func(*inp)     # expand input
        # Output to text file:
        write_output(inp, out, exp, outfile)
        # Assert
        self.assertEqual(out, exp)
    return test


def make_tests(data, func, outfile=''):
    """
    For each data, create a test case and add
    it as attribute to the TestNthStep class.
    """
    for pair in data:
        test = create_test_case(pair, func, outfile)
        test_number = str(pair[0][0]).zfill(3) + str(pair[0][1]).zfill(3)
        test.__name__ = 'test_' + str(func.__name__) + test_number
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
            ([9, 2], 55),
            ([10, 2], 89)
           ]

    data2 = [
            ([0, 3], 1),
            ([1, 3], 1),
            ([2, 3], 2),
            ([3, 3], 4),
            ([4, 3], 7),
            ([5, 3], 13),
            ([6, 3], 24),
            ([7, 3], 44),
            ([8, 3], 81),
            ([9, 3], 149),
            ([10, 3], 274)
           ]

    # Output file:
    outfile_str = 'nth_step_output.txt'

    # Clear the output file:
    clear_outfile(outfile_str)

    # Make tests:
    make_tests(data, nth_step, outfile_str)
    make_tests(data, nth_step_math, outfile_str)
    make_tests(data2, nth_step, outfile_str)

    # This won't work:
    # make_tests(data2, nth_step_math, outfile_str)

    unittest.main()
