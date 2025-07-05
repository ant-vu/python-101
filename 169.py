class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        # time: O(n), space: O(1)
        res, majority = 0, 0
        for n in nums:
            if majority == 0:
                res = n
            majority += 1 if n == res else -1
        return res

        # time: O(n), space: O(n)
        # cnt = {}
        # majority = len(nums) // 2
        # for n in nums:
        #     cnt[n] = cnt.get(n, 0) + 1
        #     if cnt[n] > majority:
        #         return n

        # time: O(n), space: O(n)
        # cnt = {}
        # for n in nums:
        #     cnt[n] = cnt.get(n, 0) + 1
        # max_cnt = max(cnt.values())
        # for k, v in cnt.items():
        #     if v == max_cnt:
        #         return k