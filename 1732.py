class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        # time: O(n), space: O(1)
        gain = [0] + gain
        for i in range(1, len(gain)):
            gain[i] += gain[i - 1]
        return max(gain)