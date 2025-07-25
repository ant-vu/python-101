class Solution:
    def canReach(self, arr: List[int], start: int) -> bool:
        # time: O(n), space: O(n)
        if 0 <= start < len(arr) and arr[start] >= 0:
            arr[start] = -arr[start]
            return arr[start] == 0 or self.canReach(arr, start + arr[start]) or self.canReach(arr, start - arr[start])
        return False

        # time: O(n), space: O(n)
        # n = len(arr)
        # hitZero = False
        # seen = set()
        # def recursive(arr, start):
        #     nonlocal hitZero
        #     seen.add(start)
        #     if arr[start] == 0:
        #         hitZero = True
        #         return
        #     if start + arr[start] < n and start + arr[start] not in seen:
        #         recursive(arr, start + arr[start])
        #     if start - arr[start] >= 0 and start - arr[start] not in seen:
        #         recursive(arr, start - arr[start])
        # recursive(arr, start)
        # return hitZero