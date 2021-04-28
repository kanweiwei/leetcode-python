import unittest
import math


class Solution:
    def judgeSquareSum(self, c: int) -> bool:
        left = 0
        right = math.floor(math.sqrt(c))
        while left <= right:
            s = left * left + right * right
            if s == c:
                return True
            elif s > c:
                right -= 1
            else:
                left += 1
        return False


class TestSolution(unittest.TestCase):
    def test(self):
        res = Solution().judgeSquareSum(5)
        self.assertEqual(res, True)
