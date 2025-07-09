class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        # time: O(n), space: O(n)
        res = []
        if not nums:
            return res
        start = nums[0]
        end = nums[0]
        for n in nums[1:]:
            if n == end + 1:
                end = n
            else:
                if start == end:
                    res.append(str(start))
                else:
                    res.append(str(start) + "->" + str(end))
                start = n
                end = n
        if start == end:
            res.append(str(start))
        else:
            res.append(str(start) + "->" + str(end))
        return res

        # time: O(n), space: O(n)
        # if len(nums) == 1:
        #     return [str(nums[0])]
        # ranges = []
        # i = 0
        # while i < len(nums) - 1:
        #     cur = str(nums[i])
        #     flg = False
        #     while i < len(nums) - 1 and nums[i] == nums[i + 1] - 1:
        #         i += 1
        #         flg = True
        #     if flg:
        #         ranges.append(cur + "->" + str(nums[i]))
        #     else:
        #         ranges.append(cur)
        #     i += 1
        # if len(nums) >= 2 and nums[-2] != nums[-1] - 1:
        #     ranges.append(str(nums[-1]))
        # return ranges