class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        # time: O(n), space: O(1)
        totalGas = 0
        curGas = 0
        startIdx = 0
        for i in range(len(gas)):
            gasGain = gas[i] - cost[i]
            totalGas += gasGain
            curGas += gasGain
            if curGas < 0:
                curGas = 0
                startIdx = i + 1
        if totalGas < 0:
            return -1
        return startIdx

        # time: O(n), space: O(1)
        # if sum(cost) > sum(gas):
        #     return -1
        # curGas = 0
        # startIdx = 0
        # for i in range(len(gas)):
        #     curGas += gas[i] - cost[i]
        #     if curGas < 0:
        #         curGas = 0
        #         startIdx = i + 1
        # return startIdx