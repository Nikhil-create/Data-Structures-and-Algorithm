class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False 

        s_set = set(s)
        for c in s_set:
            if s.count(c) != t.count(c):
                return False
        return True