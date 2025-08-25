class Solution:
    def hasMatch(self, s: str, p: str) -> bool:
        # time: O(m+n), space: O(n)
        left, right = p.split('*')
        if (s.find(left) == -1) or (s.find(right, s.find(left) + len(left)) == -1):
            return False
        return True