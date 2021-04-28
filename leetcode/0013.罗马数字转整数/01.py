import unittest


def getValue(s: str) -> int:
    d = dict({
        'I': 1,
        'V': 5,
        'X': 10,
        'L': 50,
        'C': 100,
        'D': 500,
        'M': 1000
    })
    return d[s]


class Solution:
    def romanToInt(self, s: str) -> int:
        si = 0
        preNum = getValue(s[0:1])
        i = 1
        while i < len(s):
            cur = getValue(s[i:i + 1])
            if preNum < cur:
                si -= preNum
            else:
                si += preNum
            i += 1
            preNum = cur
        si += preNum
        return si


class Test(unittest.TestCase):
    def test(self):
        r = Solution().romanToInt('III')
        self.assertEqual(r, 3)

    def test1(self):
        r = Solution().romanToInt('IV')
        self.assertEqual(r, 4)
