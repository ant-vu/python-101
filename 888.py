class Solution:
    def fairCandySwap(self, aliceSizes: List[int], bobSizes: List[int]) -> List[int]:
        # time: O(m + n), space: O(m + n)
        diff = (sum(aliceSizes) - sum(bobSizes)) // 2
        A = set(aliceSizes)
        for b in bobSizes:
            if b + diff in A:
                return [b + diff, b]

        # time: O(nlogn), space: O(n)
        # aliceSizes.sort(), bobSizes.sort()
        # sumA, sumB = sum(aliceSizes), sum(bobSizes)
        # i, j = 0, 0
        # if sumA > sumB:
        #     diff = (sumA - sumB) // 2
        #     while i < len(aliceSizes) and j < len(bobSizes):
        #         if aliceSizes[i] - bobSizes[j] == diff:
        #             return [aliceSizes[i], bobSizes[j]]
        #         elif aliceSizes[i] - bobSizes[j] > diff:
        #             j += 1
        #         else:
        #             i += 1
        # else:
        #     diff = (sumB - sumA) // 2
        #     while i < len(bobSizes) and j < len(aliceSizes):
        #         if bobSizes[i] - aliceSizes[j] == diff:
        #             return [aliceSizes[j], bobSizes[i]]
        #         elif bobSizes[i] - aliceSizes[j] > diff:
        #             j += 1
        #         else:
        #             i += 1