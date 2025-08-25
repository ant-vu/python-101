class Solution:
    def rotateString(self, s: str, goal: str) -> bool:
        # time: O(n), space: O(n)
        if len(s) != len(goal):
            return False
        return s in 2 * goal

        # time: O(n^2), space: O(n)
        # if len(s) != len(goal):
        #     return False
        # for _ in range(len(s)):
        #     if s == goal:
        #         return True
        #     s = s[1:] + s[0]
        # return False