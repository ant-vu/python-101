class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        # time: O(n), space: O(1)
        length = 0
        counting = False
        for c in s:
            if c != " ":
                if not counting:
                    counting = True
                    length = 1
                else:
                    length += 1
            else:
                counting = False
        return length

        # time: O(n), space: O(1)
        # return len(s.split()[-1])

        # time: O(n), space: O(1)
        # end = len(s) - 1
        # while end >= 0 and s[end] == " ":
        #     end -= 1
        # start = end
        # while start >= 0 and s[start] != " ":
        #     start -= 1
        # return end - start

        # time: O(n), space: O(1)
        # l = None
        # r = None
        # for i in range(len(s) - 1, -1, -1):
        #     if s[i].isalpha() and not r:
        #         r = i
        #     elif not s[i].isalpha() and r and not l:
        #         l = i
        # if l == None:
        #     l = -1
        # return r - l