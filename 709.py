class Solution:
    def toLowerCase(self, s: str) -> str:
        # time: O(n), space: O(n)
        listS = list(s)
        for i, l in enumerate(listS):
            if 'A' <= l <= 'Z':
                listS[i] = chr(ord(l) + 32)
        return "".join(listS)