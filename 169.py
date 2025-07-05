class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        # time: O(n), space: O(n)
        cnt = {}
        for n in nums:
            cnt[n] = cnt.get(n, 0) + 1
        max_cnt = max(cnt.values())
        for k, v in cnt.items():
            if v == max_cnt:
                return k