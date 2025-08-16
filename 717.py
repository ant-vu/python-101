class Solution:
    def isOneBitCharacter(self, bits: List[int]) -> bool:
        # time: O(n), space: O(1)
        if bits[-1] == 0:
            i = 0
            while i < len(bits) - 1:
                if bits[i] == 0:
                    i += 1
                elif bits[i] == 1 and bits[i + 1] == 0 and i + 1 < len(bits) - 1:
                    i += 2
                elif bits[i] == 1 and bits[i + 1] == 1 and i + 1 < len(bits) - 1:
                    i += 2
                else:
                    return False
            return True
        return False