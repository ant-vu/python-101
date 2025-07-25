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
        # end = len(s) - 1
        # while s[end] == " ":
        #     end -= 1
        # start = end
        # while start >= 0 and s[start] != " ":
        #     start -= 1
        # return end - start

        # time: O(n), space: O(1)
        # length = 0
        # wordStart = False
        # for i in range(len(s) - 1, -1, -1):
        #     if s[i].isalpha():
        #         length += 1
        #         wordStart = True
        #     elif s[i] == " " and wordStart:
        #         break
        # return length

        # time: O(n), space: O(n)
        # return len(s.split()[-1])