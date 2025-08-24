class Solution:
    def canThreePartsEqualSum(self, arr: List[int]) -> bool:
        # time: O(n), space: O(1)
        tot = sum(arr)
        l, lTot = 0, 0
        while l < len(arr) and (lTot != tot // 3 or l == 0):
            lTot += arr[l]
            l += 1
        m, mTot = l, 0
        while m < len(arr) and (mTot != tot // 3 or m == l):
            mTot += arr[m]
            m += 1
        return m != len(arr) and lTot == mTot == sum(arr[m:])