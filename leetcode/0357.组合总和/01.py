import unittest
from typing import List


class Solution:
    def combinationSum4(self, nums: List[int], target: int) -> int:
        dp = [1] + [0] * target
        for i in range(1, target + 1):
            for num in nums:
                if num <= i:
                    dp[i] += dp[i - num]

        return dp[target]


class Test(unittest.TestCase):
    def test(self):
        n = Solution().combinationSum4([1, 2, 3], 4)
        self.assertEqual(n, 7)
