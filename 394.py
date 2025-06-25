class Solution:
    def decodeString(self, s: str) -> str:
        # time: O(n), space: O(n)
        stack = []
        for c in s:
            if c != "]":
                stack.append(c)
            else:
                tmp = ""
                while stack and stack[-1] != "[":
                    tmp = stack.pop() + tmp
                stack.pop()
                tmp2 = ""
                while stack and stack[-1].isdecimal():
                    tmp2 = stack.pop() + tmp2
                for c2 in int(tmp2) * tmp:
                    stack.append(c2)
        return "".join(stack)