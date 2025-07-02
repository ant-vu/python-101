class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        # time: O(n), space: O(n)
        monotonic_stack = []
        res = [0] * len(temperatures)
        for i in range(len(temperatures)):
            while monotonic_stack and temperatures[i] > temperatures[monotonic_stack[-1]]:
                idx = monotonic_stack.pop()
                res[idx] = i - idx
            monotonic_stack.append(i)
        return res