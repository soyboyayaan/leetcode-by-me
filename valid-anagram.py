class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        else:
            for char in s:
                if s.count(char) != t.count(char):
                    return False
            return True