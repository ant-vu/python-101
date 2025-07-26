class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        # time: O(n^2), space: O(n)
        n = len(nums)
        nums.sort()
        triplets = []
        for i in range(n):
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            l = i + 1
            r = n - 1
            while l < r:
                if nums[i] + nums[l] + nums[r] == 0:
                    triplets.append([nums[i], nums[l], nums[r]])
                    l += 1
                    while nums[l] == nums[l - 1] and l < r:
                        l += 1
                elif nums[i] + nums[l] + nums[r] < 0:
                    l += 1
                else:
                    r -= 1
        return triplets

        # time: O(n^2), space: O(n)
        # n = len(nums)
        # nums.sort()
        # triplets = set()
        # for i in range(n):
        #     l = i + 1
        #     r = n - 1
        #     while l < r:
        #         if nums[i] + nums[l] + nums[r] == 0:
        #             triplets.add((nums[i], nums[l], nums[r]))
        #             l += 1
        #         elif nums[i] + nums[l] + nums[r] < 0:
        #             l += 1
        #         else:
        #             r -= 1
        # return [list(x) for x in triplets]