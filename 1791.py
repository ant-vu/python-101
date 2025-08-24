class Solution:
    def findCenter(self, edges: List[List[int]]) -> int:
        # time: O(1), space: O(1)
        return edges[0][0] if edges[0][0] in edges[1] else edges[0][1]

        # time: O(1), space: O(1)
        # return set(edges[0]).intersection(set(edges[1])).pop()

        # time: O(mn), space: O(m)
        # cnt = [0] * (len(edges) + 2)
        # for i in edges:
        #     for j in i:
        #         cnt[j] += 1
        # return cnt.index(max(cnt))