class NumArray:

    def __init__(self, nums: List[int]):
        # time: O(n), space: O(n)
        self.data = [0]
        cur = 0
        for n in nums:
            cur += n
            self.data.append(cur)

    def sumRange(self, left: int, right: int) -> int:
        # time: O(1), space: O(1)
        return self.data[right + 1] - self.data[left]


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(left,right)