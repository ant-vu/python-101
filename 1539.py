class Solution:
    def findKthPositive(self, arr: List[int], k: int) -> int:
        # time: O(logn), space: O(1)
        l, r = 0, len(arr)
        while l < r:
            m = l + (r - l) // 2
            if arr[m] - m - 1 < k:
                l = m + 1
            else:
                r = m
        return r + k

        # time: O(n), space: O(n)
        # arr = set(arr)
        # res = 1
        # while k:
        #     if res not in arr:
        #         k -= 1
        #         if k == 0:
        #             return res
        #     res += 1
        # return res 