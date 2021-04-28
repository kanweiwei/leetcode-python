import math
import unittest


class Solution:
    def judgeSquareSum(self, c: int) -> bool:
        a = 0
        while a * a <= c:
            b = math.sqrt(c - a * a)
            if b == int(b):
                return True

            a += 1

        return False


class TestSolution(unittest.TestCase):
    def test(self):
        res = Solution().judgeSquareSum(5)
        self.assertEqual(res, True)
