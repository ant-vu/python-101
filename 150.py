class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        # time: O(n), space: O(n)
        s = []
        for t in tokens:
            if t not in "+-*/":
                s.append(int(t))
                continue
            r = s.pop()
            l = s.pop()
            if t == "+":
                s.append(l + r)
            elif t == "-":
                s.append(l - r)
            elif t == "*":
                s.append(l * r)
            else:
                s.append(int(l / r))
        return s[0]