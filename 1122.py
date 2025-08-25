class Solution:
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
        # time: O(n+k), space: O(n)
        maxVal = max(arr1)
        cnts = [0] * (maxVal + 1)
        for val in arr1:
            cnts[val] += 1
        res = []
        for val in arr2:
            while cnts[val] > 0:
                res.append(val)
                cnts[val] -= 1
        for val in range(maxVal + 1):
            while cnts[val] > 0:
                res.append(val)
                cnts[val] -= 1
        return res

        # time: O(n+k), space: O(n)
        # def countingSort(arr):
        #     cnts = {}
        #     minVal, maxVal = min(arr), max(arr)
        #     for val in arr:
        #         cnts[val] = 1 + cnts.get(val, 0)
        #     idx = 0
        #     for val in arr2:
        #         while cnts.get(val, 0) > 0:
        #             arr[idx] = val
        #             idx += 1
        #             cnts[val] -= 1
        #     for val in sorted(cnts):
        #         while cnts.get(val, 0) > 0:
        #             arr[idx] = val
        #             idx += 1
        #             cnts[val] -= 1

        # sortedArr1 = arr1[:]
        # countingSort(sortedArr1)
        # return sortedArr1