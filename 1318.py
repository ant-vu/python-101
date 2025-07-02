class Solution:
    def minFlips(self, a: int, b: int, c: int) -> int:
        # time: O(n), space: O(1)
        a2, b2, c2 = bin(a)[2:], bin(b)[2:], bin(c)[2:]
        x, y, z = len(a2), len(b2), len(c2)
        a2 = "0" * (max(x, y, z) - x) + a2
        b2 = "0" * (max(x, y, z) - y) + b2
        c2 = "0" * (max(x, y, z) - z) + c2
        flips = 0
        for i in range(len(c2)):
            if c2[i] == "0":
                if a2[i] == "1" and b2[i] == "1":
                    flips += 2
                elif a2[i] == "1" or b2[i] == "1":
                    flips += 1
            elif c2[i] == "1":
                if a2[i] == "0" and b2[i] == "0":
                    flips += 1
        return flips