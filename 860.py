class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        # time: O(n), space: O(1)
        register = {5: 0, 10: 0}
        for b in bills:
            if b == 5:
                register[5] += 1
            elif b == 10:
                if register[5] >= 1:
                    register[5] -= 1
                    register[10] += 1
                else:
                    return False
            else:
                if register[5] >= 1 and register[10] >= 1:
                    register[5] -= 1
                    register[10] -= 1
                elif register[5] >= 3:
                    register[5] -= 3
                else:
                    return False
        return True