class Solution:
    def toHex(self, num: int) -> str:
        # time: O(1), space: O(1)
        if num == 0:
            return "0"
        elif num < 0:
            num += 2 ** 32
        h, r = "0123456789abcdef", []
        while num:
            r.append(h[num & 15])
            num //= 16
        return "".join(r[::-1])