class Solution:
    def findRestaurant(self, list1: List[str], list2: List[str]) -> List[str]:
        # time: O(m + n), space: O(m)
        idxMap = {word: i for i, word in enumerate(list1)}
        minSum = inf
        res = []
        for j, word in enumerate(list2):
            if word in idxMap:
                idxSum = j + idxMap[word]
                if idxSum < minSum:
                    minSum = idxSum
                    res = [word]
                elif idxSum == minSum:
                    res.append(word)
        return res

        # time: O(m + n), space: O(m * x), x = avg str len
        # seen = {}
        # for i, s in enumerate(list1):
        #     if s not in seen:
        #         seen[s] = i
        # idxSum = inf
        # for i, s in enumerate(list2):
        #     if s in seen:
        #         idxSum = min(idxSum, seen[s] + i)
        # res = []
        # for i, s in enumerate(list2):
        #     if s in seen:
        #         if seen[s] + i == idxSum:
        #             res.append(s)
        # return res