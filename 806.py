class Solution:
    def numberOfLines(self, widths: List[int], s: str) -> List[int]:
        # time: O(n), space: O(1)
        lines = 1
        curW = 0
        for l in s:
            w = widths[ord(l) - ord('a')]
            curW += w
            if curW > 100:
                lines += 1
                curW = w
        return lines, curW

        # time: O(n), space: O(n)
        # maps = {}
        # for l, w in zip('abcdefghijklmnopqrstuvwxyz', widths):
        #     maps[l] = w
        # lines = 1
        # curW = 0
        # for l in s:
        #     if maps[l] + curW > 100:
        #         lines += 1
        #         curW = 0
        #     curW += maps[l]
        # return lines, curW