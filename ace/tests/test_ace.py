'''
Unit tests for ACE methods
'''

import unittest

import ace.ace
import ace.samples.breiman85

class TestAce(unittest.TestCase):

    def setUp(self):
        self.ace = ace.ace.ACESolver()
        x, y = ace.samples.breiman85.build_sample_ace_problem_breiman85()
        self.ace.specify_data_set(x, y)
        self.ace._initialize()

    def test_compute_sorted_indices(self):
        yprevious = self.ace.y[self.ace._yi_sorted[0]]
        for yi in self.ace._yi_sorted[1:]:
            yhere = self.ace.y[yi]
            self.assertGreater(yhere, yprevious)

    def test_error_is_decreasing(self):
        err = self.ace._compute_error()
        self.assertFalse(self.ace._error_is_decreasing(err)[0])

    def test_compute_error(self):
        err = self.ace._compute_error()
        self.assertNotAlmostEqual(err, 0.0)

    def test_update_x_transforms(self):
        err = self.ace._compute_error()
        self.ace._update_x_transforms()
        self.assertTrue(self.ace._error_is_decreasing(err)[0])

    def test_update_y_transform(self):
        err = self.ace._compute_error()
        self.ace._update_x_transforms()
        self.ace._update_y_transform()
        self.assertTrue(self.ace._error_is_decreasing(err)[0])

    def test_sort_vector(self):
        data = [5, 1, 4, 6]
        increasing = [1, 2, 0, 3]
        dsort = ace.ace.sort_vector(data, increasing)
        self.assertItemsEqual(sorted(data), dsort)

    def test_unsort_vector(self):
        unsorted = [5, 1, 4, 6]
        data = [1, 4, 5, 6]
        increasing = [1, 2, 0, 3]
        dunsort = ace.ace.unsort_vector(data, increasing)
        self.assertItemsEqual(unsorted, dunsort)


if __name__ == "__main__":
    # import sys;sys.argv = ['', 'Test.testName']
    unittest.main()
