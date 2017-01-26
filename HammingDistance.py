# The Hamming distance between two integers is the number of positions at which the corresponding bits are different.
#
# Given two integers x and y, calculate the Hamming distance.
#
# Note:
# 0 <= x, y < 231.
#
# Example:
#
# Input: x = 1, y = 4
#
# Output: 2
#
# Explanation:
# 1   (0 0 0 1)
# 4   (0 1 0 0)
#
#
# The above arrows point to positions where the corresponding bits are different.

import unittest


class Solution(object):

    @staticmethod
    def hamming_distance(x, y):
        """
        :type x: int
        :type y: int
        :rtype: int
        """
        # Verify types and values
        if type(x) not in [int, long] or type(y) not in [int, long]:
            return -1
        if x < 0 or y < 0:
            return -1

        different_bits = x ^ y
        distance = 0
        while different_bits:
            distance += (different_bits % 2 == 1)
            different_bits /= 2
        return distance


class TestHammingDistance(unittest.TestCase):

    def setUp(self):
        self.solution = Solution()
        print "Test: " + self._testMethodName

    def test_all_range_no_error(self):
        for x in range(231):
            for y in range(231):
                try:
                    self.solution.hamming_distance(x, y)
                except:
                    self.fail("Raised an Exception with a valid case")

    def test_outside_range(self):
        x = 100000000000
        y = 904384093854
        expected_value = 21
        try:
            result = self.solution.hamming_distance(x, y)
        except:
            self.fail("Invalid case, but must have handled it")
        self.assertEqual(result, expected_value, "Expected value is not matched. Actual value: " + str(result) +
                                                 ". Expected: " + str(expected_value))

    def test_invalid_data(self):
        data = [['a', 'b'], [[123, 4], [231, 4]], [(123, 321), (231, 123)], [1j, 2j]]
        expected_value = -1
        for pair in data:
            result = self.solution.hamming_distance(pair[0], pair[1])
            self.assertEqual(result, expected_value, "Invalid cases, result should be -1. Actual: " + str(result))

    def tearDown(self):
        self.solution = None

if __name__ == '__main__':
    unittest.main()
