class Solution:
    def removeOuterParentheses(self, s: str) -> str:
        # time: O(n), space: O(n)
        res, cntL = [], 0
        for c in s:
            if c == '(' and cntL >= 1:
                res.append(c)
            elif c == ')' and cntL >= 2:
                res.append(c)
            cntL += 1 if c == '(' else -1
        return ''.join(res)

        # time: O(n), space: O(n)
        # res = []
        # i = 0
        # while i < len(s):
        #     st = []
        #     cntL, cntR = 0, 0
        #     while i < len(s) and (cntL != cntR or cntL == 0):
        #         if s[i] == '(':
        #             cntL += 1
        #         else:
        #             cntR += 1
        #         st.append(s[i])
        #         i += 1
        #     res.append(''.join(st[1:-1]))
        # return ''.join(res)