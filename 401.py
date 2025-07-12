class Solution:
    def readBinaryWatch(self, turnedOn: int) -> List[str]:
        # time: O(1), space: O(1)
        if turnedOn < 0 or 8 < turnedOn:
            return []
        res = []
        for h in range(12):
            for m in range(60):
                if bin(h).count("1") + bin(m).count("1") == turnedOn:
                    res.append("{}:{:02d}".format(h, m))
        return res