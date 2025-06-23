class Solution:
    def compress(self, chars: List[str]) -> int:
        # time: O(n), space: O(1)
        i = 0
        res = 0
        while i < len(chars):
            group_length = 1
            while i + group_length < len(chars) and chars[i + group_length] == chars[i]:
                group_length += 1
            chars[res] = chars[i]
            res += 1
            if group_length > 1:
                str_repr = str(group_length)
                chars[res : res + len(str_repr)] = list(str_repr)
                res += len(str_repr)
            i += group_length
        return res

        # time: O(n), space: O(1)
        # l, r = len(chars) - 1, len(chars) - 1
        # while l >= 0:
        #     while l >= 0 and chars[l] == chars[r]:
        #         l -= 1
        #     for _ in range(r - l - 1):
        #         chars.pop(l + 1)
        #     if r - l > 1:
        #         for c in str(r - l)[::-1]:
        #             chars.insert(l + 2, c)
        #     r = l