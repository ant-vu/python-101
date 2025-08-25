class Solution:
    def heightChecker(self, heights: List[int]) -> int:
        # time: O(n+k), space: O(n)
        def countingSort(arr):
            cnts = {}
            minVal, maxVal = min(arr), max(arr)
            for val in arr:
                cnts[val] = 1 + cnts.get(val, 0)
            idx = 0
            for val in range(minVal, maxVal + 1):
                while cnts.get(val, 0) > 0:
                    arr[idx] = val
                    idx += 1
                    cnts[val] -= 1

        sortedHeights = heights[:]
        countingSort(sortedHeights)
        return sum(1 for i in range(len(heights)) if heights[i] != sortedHeights[i])

        # time: O(nlogn), space: O(n)
        # sortedHeights = sorted(heights)
        # return sum(1 for i in range(len(heights)) if heights[i] != sortedHeights[i])