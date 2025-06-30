class Solution:
    def totalCost(self, costs: List[int], k: int, candidates: int) -> int:
        # time: O(nlogn), space: O(n)
        for i in range(len(costs)):
            costs[i] = (costs[i], i)
        if candidates * 2 >= len(costs):
            tmp = costs
        else:
            tmp = costs[:candidates] + costs[-candidates:]
        heapify(tmp)
        res = 0
        l, r = candidates, len(costs) - candidates - 1
        for _ in range(k):
            node = heappop(tmp)
            if l <= r:
                if abs(node[1] - l) <= abs(node[1] - r):
                    heappush(tmp, costs[l])
                    l += 1
                else:
                    heappush(tmp, costs[r])
                    r -= 1
            res += node[0]
        return res