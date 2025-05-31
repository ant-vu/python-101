class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        # time: O(n^2logn), space: O(1)
        def is_common_prefix(strs, length):
            str1 = strs[0][:length]
            for i in range(1, len(strs)):
                if not strs[i].startswith(str1):
                    return False
            return True

        min_len = min(len(x) for x in strs)
        low = 1
        high = min_len
        while low <= high:
            mid = low + (high - low) // 2
            if is_common_prefix(strs, mid):
                low = mid + 1
            else:
                high = mid - 1
        return strs[0][:(low + high) // 2]

        # time: O(n^2), space: O(nlogn)
        # def LCP(left, right):
        #     min_len = min(len(left), len(right))
        #     for i in range(min_len):
        #         if left[i] != right[i]:
        #             return left[:i]
        #     return left[:min_len]
        
        # def divide_and_conquer(strs, left, right):
        #     if left == right:
        #         return strs[left]
        #     else:
        #         mid = left + (right - left) // 2
        #         lcp_left = divide_and_conquer(strs, left, mid)
        #         lcp_right = divide_and_conquer(strs, mid + 1, right)
        #         return LCP(lcp_left, lcp_right)
        
        # return divide_and_conquer(strs, 0, len(strs) - 1)

        # time: O(n^2), space: O(1)
        # for i in range(len(strs[0])):
        #     c = strs[0][i]
        #     for j in range(1, len(strs)):
        #         if i == len(strs[j]) or strs[j][i] != c:
        #             return strs[0][:i]
        # return strs[0]

        # time: O(n^2), space: O(1)
        # prefix = strs[0]
        # for i in range(1, len(strs)):
        #     while strs[i].find(prefix) != 0:
        #         prefix = prefix[:len(prefix) - 1]
        #         if prefix == "":
        #             return ""
        # return prefix

        # time: O(n^2), space: O(1)
        # if len(strs) == 1:
        #     return strs[0]

        # shortest = min(strs, key=len)
        # res = 0
        # for length in range(len(shortest) + 1):
        #     flag = True
        #     for s in strs:
        #         if s[:length] != shortest[:length]:
        #             flag = False
        #             break
        #     if flag:
        #         res = max(res, length)
        # return shortest[:res]