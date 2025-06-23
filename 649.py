class Solution:
    def predictPartyVictory(self, senate: str) -> str:
        # time: O(n), space: O(1)
        senate = list(senate)
        i = 0
        while len(set(senate)) > 1:
            flag = True
            if senate[i] == "R":
                for j in range(i + 1, len(senate)):
                    if senate[j] == "D":
                        senate.pop(j)
                        flag = False
                        break
                if flag:
                    for j in range(i):
                        if senate[j] == "D":
                            senate.pop(j)
                            i -= 1
                            break
            else:
                for j in range(i + 1, len(senate)):
                    if senate[j] == "R":
                        senate.pop(j)
                        flag = False
                        break
                if flag:
                    for j in range(i):
                        if senate[j] == "R":
                            senate.pop(j)
                            i -= 1
                            break
            i += 1
            if i >= len(senate):
                i = 0
        return "Radiant" if senate[0] == "R" else "Dire"