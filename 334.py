class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:
        # time: O(n), space: O(1)
        smallest = float("inf")
        second_smallest = float("inf")
        for n in nums:
            if n <= smallest:
                smallest = n
            elif n <= second_smallest:
                second_smallest = n
            else:
                return True
        return False