class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        from collections import Counter
        seen = Counter(t)
        for i in s:
            if seen[i] > 0:
                seen[i] -= 1
            else:
                return False
        return True