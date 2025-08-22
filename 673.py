class Solution:
    def findNumberOfLIS(self, nums: List[int]) -> int:
        # time: O(n^2), space: O(n)
        def calculate_dp(i):
            if length[i] != 0:
                return
            length[i] = 1
            count[i] = 1
            for j in range(i):
                if nums[j] < nums[i]:
                    calculate_dp(j)
                    if length[j] + 1 > length[i]:
                        length[i] = length[j] + 1
                        count[i] = 0
                    if length[j] + 1 == length[i]:
                        count[i] += count[j]
        
        n = len(nums)
        length = [0] * n
        count = [0] * n
        max_length = 0
        result = 0
        for i in range(n):
            calculate_dp(i)
            max_length = max(max_length, length[i])
        for i in range(n):
            if length[i] == max_length:
                result += count[i]
        return result

        # time: O(n^2), space: O(n)
        # n = len(nums)
        # length = [1] * n
        # count = [1] * n
        # for i in range(n):
        #     for j in range(i):
        #         if nums[j] < nums[i]:
        #             if length[j] + 1 > length[i]:
        #                 length[i] = length[j] + 1
        #                 count[i] = 0
        #             if length[j] + 1 == length[i]:
        #                 count[i] += count[j]
        # max_length = max(length)
        # result = 0
        # for i in range(n):
        #     if length[i] == max_length:
        #         result += count[i]
        # return result