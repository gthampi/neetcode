# https://leetcode.com/problems/valid-parentheses/description/

class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        rel_map = {'(': ')', '[': ']', '{': '}'}
        stack = []
        for c in s:
            if c in rel_map:
                stack.append(c)
            else:
                if not stack or c != rel_map[stack.pop()]:
                    return False
        return len(stack) == 0