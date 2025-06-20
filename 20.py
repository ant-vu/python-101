class Solution:
    def isValid(self, s: str) -> bool:
        # time: O(n), space: O(n)
        def is_pair(last, cur):
            if last == "(" and cur == ")" or last == "{" and cur == "}" or last == "[" and cur == "]":
                return True
            return False

        stack = []
        for i in range(len(s)):
            if stack:
                if is_pair(stack[-1], s[i]):
                    stack.pop()
                    continue
            stack.append(s[i])
        return not stack

        # time: O(n), space: O(n)
        # stack = []
        # mapping = {')': '(', '}': '{', ']': '['}
        # for char in s:
        #     if char not in mapping:
        #         stack.append(char)
        #     elif not stack or stack.pop() != mapping[char]:
        #         return False
        # return not stack