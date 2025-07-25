class Solution:
    def fullJustify(self, words: List[str], maxWidth: int) -> List[str]:
        # time: O(m * n), space: O(m * n)
        res = []
        i = 0
        n = len(words)
        while i < n:
            j = i
            lineLen = 0
            while j < n and lineLen + len(words[j]) + (j - i) <= maxWidth:
                lineLen += len(words[j])
                j += 1
            spaceCount = maxWidth - lineLen
            gaps = j - i - 1
            line = ""
            if j == n or gaps == 0:
                for k in range(i, j):
                    line += words[k] + (" " if k != j - 1 else "")
                line += " " * (maxWidth - len(line))
            else:
                spaceEach = spaceCount // gaps
                extra = spaceCount % gaps
                for k in range(i, j):
                    line += words[k]
                    if k != j - 1:
                        toAdd = spaceEach + (1 if extra > 0 else 0)
                        line += " " * toAdd
                        if extra > 0:
                            extra -= 1
            res.append(line)
            i = j
        return res

        # time: O(m * n), space: O(m * n)
        # lines = []
        # curLine = []
        # curLen = 0
        # for w in words:
        #     if not curLine:
        #         curLine = [w]
        #         curLen = len(w)
        #     elif curLen + len(w) >= maxWidth:
        #         lines.append(curLine)
        #         curLine = [w]
        #         curLen = len(w)
        #     else:
        #         curLine.append(w)
        #         curLen += len(w) + 1
        # if curLine:
        #     lines.append(curLine)
        # res = []
        # for l in lines[:-1]:
        #     spaces = maxWidth - len("".join(l))
        #     if len(l) > 1:
        #         tmp = [0] * (len(l) - 1)
        #         idx = 0
        #         while spaces > 0:
        #             tmp[idx] += 1
        #             idx += 1
        #             if idx == len(tmp):
        #                 idx = 0
        #             spaces -= 1
        #         string = ""
        #         sIdx = 0
        #         while sIdx < len(tmp):
        #             string += l[sIdx] + " " * tmp[sIdx]
        #             sIdx += 1
        #         string += l[-1]
        #         res.append(string)
        #     else:
        #         res.append(l[0] + " " * (maxWidth - len(l[0])))
        # lastLine = " ".join(lines[-1]) + " " * (maxWidth - len(" ".join(lines[-1])))
        # return res + [lastLine]