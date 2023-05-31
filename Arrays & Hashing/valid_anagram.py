class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        if len(s) != len(t):
            return False
        s, t = sorted(s), sorted(t)
        for sc, tc in zip(s, t):
            if sc != tc:
                return False
        return True
