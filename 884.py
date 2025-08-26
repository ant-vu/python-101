class Solution:
    def uncommonFromSentences(self, s1: str, s2: str) -> List[str]:
        # time: O(m+n), space: O(m+n)
        count = {}
        for word in s1.split() + s2.split():
            count[word] = 1 + count.get(word, 0)
        return [key for key, value in count.items() if value == 1]

        # time: O(m+n), space: O(m+n)
        # count1 = {}
        # for word in s1.split():
        #     count1[word] = 1 + count1.get(word, 0)
        # count2 = {}
        # for word in s2.split():
        #     count2[word] = 1 + count2.get(word, 0)
        # uncommon = []
        # for key, value in count1.items():
        #     if value == 1 and key not in count2:
        #         uncommon.append(key)
        # for key, value in count2.items():
        #     if value == 1 and key not in count1:
        #         uncommon.append(key)
        # return uncommon