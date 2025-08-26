class Solution:
    def countGoodSubstrings(self, s: str) -> int:
        # time: O(n), space: O(1)
        res = 0
        window = deque()
        for c in s:
            if len(window) < 3:
                window.append(c)
            if len(window) == 3:
                if window[0] != window[1] != window[2] and window[0] != window[2]:
                    res += 1
                window.popleft()
        return res