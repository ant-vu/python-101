class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        # time: O(n+m), space: O(n)
        cnt = [0] * (n + 1)
        for i, j in trust:
            cnt[i] -= 1
            cnt[j] += 1
        for i in range(1, n + 1):
            if cnt[i] == n - 1:
                return i
        return -1

        # time: O(n^2), space: O(nm)
        # d = {}
        # for x, y in trust:
        #     if x not in d:
        #         d[x] = []
        #     d[x].append(y)
        # cand = []
        # for i in range(1, n + 1):
        #     if i not in d:
        #         cand.append(i)
        # for c in cand:
        #     flg = True
        #     for i in range(1, n + 1):
        #         if i != c:
        #             if i not in d or c not in d[i]:
        #                 flg = False
        #     if flg:
        #         return c
        # return -1