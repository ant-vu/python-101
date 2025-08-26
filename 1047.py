class Solution:
    def removeDuplicates(self, s: str) -> str:
        # time: O(n), space: O(n)
        stack = []
        for c in s:
            if stack and c == stack[-1]:
                stack.pop()
            else:
                stack.append(c)
        return ''.join(stack)