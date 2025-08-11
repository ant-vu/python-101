class Solution:
    def productQueries(self, n: int, queries: List[List[int]]) -> List[int]:
        # time: O(n), space: O(n)
        a = 1
        while a * 2 <= n:
            a *= 2
        total = n
        powers = []
        while total > 0:
            print(a, total)
            if total >= a:
                total -= a
                powers.append(a)
            a //= 2
        powers = powers[::-1]
        answers = []
        for q in queries:
            tmp = 1
            for i in range(q[0], q[1] + 1):
                tmp *= powers[i]
            answers.append(tmp % ((10 ** 9) + 7))
        return answers