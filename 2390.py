class Solution:
    def removeStars(self, s: str) -> str:
        # time: O(n), space: O(n)
        stack = []
        for c in s:
            if c == "*":
                stack.pop()
            else:
                stack.append(c)
        return "".join(stack)