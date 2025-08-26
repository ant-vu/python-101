class Solution:
    def numEquivDominoPairs(self, dominoes: List[List[int]]) -> int:
        # time: O(n), space: O(1)
        num = [0] * 100
        ret = 0
        for x, y in dominoes:
            val = x * 10 + y if x <= y else y * 10 + x
            ret += num[val]
            num[val] += 1
        return ret

        # time: O(n), space: O(1)
        # pairs = 0
        # count = {}
        # n = len(dominoes)
        # for i in range(n):
        #     tmp = sorted(dominoes[i])
        #     tmp2 = (tmp[0], tmp[1])
        #     if tmp2 not in count:
        #         count[tmp2] = 1
        #     else:
        #         pairs += count[tmp2]
        #         count[tmp2] += 1
        # return pairs