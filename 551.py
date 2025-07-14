class Solution:
    def checkRecord(self, s: str) -> bool:
        # time: O(n), space: O(1)
        return s.count("A") < 2 and s.find("LLL") == -1