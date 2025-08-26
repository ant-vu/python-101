class Solution:
    def countGoodTriplets(self, arr: List[int], a: int, b: int, c: int) -> int:
        # time: O(n^2+1000n), space: O(1000)
        count = 0
        n = len(arr)
        total = [0] * 1001
        for j in range(n - 1):
            for k in range(j + 1, n):
                if abs(arr[j] - arr[k]) <= b:
                    lj, rj = arr[j] - a, arr[j] + a
                    lk, rk = arr[k] - c, arr[k] + c
                    l = max(0, lj, lk)
                    r = min(1000, rj, rk)
                    if l <= r:
                        count += total[r] if l == 0 else total[r] - total[l - 1]
            for k in range(arr[j], 1001):
                total[k] += 1
        return count

        # time: O(n^3), space: O(1)
        # count = 0
        # n = len(arr)
        # for i in range(n - 2):
        #     for j in range(i + 1, n - 1):
        #         for k in range(j + 1, n):
        #             if abs(arr[i] - arr[j]) <= a and abs(arr[j] - arr[k]) <= b and abs(arr[i] - arr[k]) <= c:
        #                 count += 1
        # return count