class Solution:
    def calculate(self, s: str) -> int:
        # time: O(n), space: O(n)
        res = 0
        cur = 0
        sign = 1
        stack = [sign]
        for c in s:
            if c.isdigit():
                cur = cur * 10 + int(c)
            elif c == "(":
                stack.append(sign)
            elif c == ")":
                stack.pop()
            elif c == "+" or c == "-":
                res += sign * cur
                sign = (1 if c == "+" else -1) * stack[-1]
                cur = 0
        return res + sign * cur

        # time: O(n), space: O(n), RE
        # return eval(s)