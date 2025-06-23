class Solution:
    def compress(self, chars: List[str]) -> int:
        # time: O(n), space: O(1)
        l, r = len(chars) - 1, len(chars) - 1
        while l >= 0:
            while l >= 0 and chars[l] == chars[r]:
                l -= 1
            for _ in range(r - l - 1):
                chars.pop(l + 1)
            if r - l > 1:
                for c in str(r - l)[::-1]:
                    chars.insert(l + 2, c)
            r = l