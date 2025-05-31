class Solution:
    def isValid(self, s: str) -> bool:
        # time: O(n), space: O(n)
        stack = []
        mapping = {')': '(', '}': '{', ']': '['}
        for char in s:
            if char not in mapping:
                stack.append(char)
            elif not stack or stack.pop() != mapping[char]:
                return False
        return not stack