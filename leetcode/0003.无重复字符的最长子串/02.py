import unittest


class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        occ = set()
        n = len(s)
        rk, ans = -1, 0
        for i in range(n):
            if i != 0:
                occ.remove(s[i - 1])
            while rk + 1 < n and s[rk + 1] not in occ:
                occ.add(s[rk + 1])
                rk += 1
            ans = max(ans, rk - i + 1)
        return ans


class TestSolution(unittest.TestCase):
    def test(self):
        s = Solution().lengthOfLongestSubstring('lasdasdad')
        self.assertEqual(s, 4)


if __name__ == '__main__':
    unittest.main()
