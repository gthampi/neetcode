class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        if len(s) != len(t):
            return False
        count_s, count_t = {}, {}
        for sc, tc in zip(s, t):
            count_s[sc] = count_s.get(sc, 0) + 1
            count_t[tc] = count_t.get(tc, 0) + 1
        return count_s == count_t

