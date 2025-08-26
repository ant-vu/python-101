class Solution:
    def containsPattern(self, arr: List[int], m: int, k: int) -> bool:
        # time: O(n), space: O(1)
        streak = 0
        n = len(arr)
        for i in range(n - m):
            streak = streak + 1 if arr[i] == arr[i + m] else 0
            if streak == m * (k - 1):
                return True
        return False

        # time: O(n * m * k), space: O(m * k)
        # n = len(arr)
        # for i in range(n - (m * k) + 1):
        #     window = arr[i:i+(m*k)]
        #     isPattern = True
        #     for j in range(0, len(window) - m, m):
        #         if window[j:j+m] != window[j+m:j+m+m]:
        #             isPattern = False
        #     if isPattern:
        #         return True
        # return False