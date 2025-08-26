class Solution:
    def finalPrices(self, prices: List[int]) -> List[int]:
        # time: O(n), space: O(n)
        n = len(prices)
        stack = []
        for i in range(n):
            while stack and prices[stack[-1]] >= prices[i]:
                prices[stack.pop()] -= prices[i]
            stack.append(i)
        return prices

        # time: O(n^2), space: O(1)
        # n = len(prices)
        # for i in range(n - 1):
        #     for j in range(i + 1, n):
        #         if prices[i] >= prices[j]:
        #             prices[i] -= prices[j]
        #             break
        # return prices