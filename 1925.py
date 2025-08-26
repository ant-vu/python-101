class Solution:
    def countTriples(self, n: int) -> int:
        # time: O(n^2), space: O(1)
        triples = 0
        for i in range(1, n):
            for j in range(1, n):
                k = (i ** 2 + j ** 2) ** 0.5
                if int(k) == k and k <= n:
                    triples += 1
        return triples