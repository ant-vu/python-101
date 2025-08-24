class Solution:
    def diStringMatch(self, s: str) -> List[int]:
        # time: O(n), space: O(1)
        l, r = 0, len(s)
        res = []
        for c in s:
            if c == 'I':
                res.append(l)
                l += 1
            else:
                res.append(r)
                r -= 1
        return res + [l]