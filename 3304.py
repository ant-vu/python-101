class Solution:
    def kthCharacter(self, k: int) -> str:
        # time: O(k), space: O(k)
        word = 'a'
        while len(word) < k:
            new = ''
            for letter in word:
                if letter == 'z':
                    new += 'a'
                else:
                    new += chr(ord(letter) + 1)
            word += new
        return word[k - 1]