class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        # time: O(n), space: O(1)
        count = 0
        curNum = nums[0]
        for n in nums:
            if count == 0:
                curNum = n
            if n == curNum:
                count += 1
            else:
                count -= 1
        return curNum

        # time: O(n), space: O(1)
        # count = 0
        # curNum = nums[0]
        # for n in nums:
        #     if n == curNum:
        #         count += 1
        #     else:
        #         count -= 1
        #         if count < 0:
        #             count = 0
        #             curNum = n
        # return curNum

        # time: O(n), space: O(n)
        # counter = {}
        # curNum = nums[0]
        # majority = 1
        # for n in nums:
        #     counter[n] = counter.get(n, 0) + 1
        #     if counter[n] > majority:
        #         curNum = n
        #         majority = counter[n]
        # return curNum