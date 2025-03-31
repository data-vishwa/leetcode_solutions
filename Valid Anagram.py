class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        from collections import Counter
        # Just count the chars in s and t
        if Counter(s) == Counter(t):
            return True
        else:
            return False
