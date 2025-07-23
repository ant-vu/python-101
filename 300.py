class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        # time: O(nlog(n)), space: O(n)
        res = []
        for n in nums:
            if not res or n > res[-1]:
                res.append(n)
            else:
                l = 0
                r = len(res) - 1
                idx = -1
                while l <= r:
                    m = l + (r - l) // 2
                    if res[m] == n:
                        idx = m
                        break
                    elif res[m] < n:
                        l = m + 1
                    else:
                        r = m - 1
                if idx == -1:
                    idx = l
                res[idx] = n
        return len(res)