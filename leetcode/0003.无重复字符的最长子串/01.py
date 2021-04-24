import unittest


class Solution:
    # 01 暴力解法，双层循环 O(n^2), 会超出时间限制
    def lengthOfLongestSubstring(self, s: str) -> int:
        n = 0
        for i in range(0, len(s)+1):
            for y in range(i, len(s)+1):
                li = s[i:y]
                hashset = set(li)
                if len(hashset) == len(li):
                    n = max(len(li), n)

        return n


class TestSolution(unittest.TestCase):
    def test(self):
        s = Solution().lengthOfLongestSubstring(' ')
        self.assertEqual(s, 1)


if __name__ == '__main__':
    unittest.main()
