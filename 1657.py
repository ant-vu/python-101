class Solution:
    def closeStrings(self, word1: str, word2: str) -> bool:
        # time: O(n), space: O(n)
        cnt1, cnt2 = {}, {}
        for i in word1:
            cnt1[i] = cnt1.get(i, 0) + 1
        for i in word2:
            cnt2[i] = cnt2.get(i, 0) + 1
        cnt3, cnt4 = {}, {}
        for i in cnt1.values():
            cnt3[i] = cnt3.get(i, 0) + 1
        for i in cnt2.values():
            cnt4[i] = cnt4.get(i, 0) + 1
        return (cnt1 == cnt2 or cnt3 == cnt4) and cnt1.keys() == cnt2.keys()