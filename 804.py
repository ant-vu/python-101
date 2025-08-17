class Solution:
    def uniqueMorseRepresentations(self, words: List[str]) -> int:
        # time: O(n * k), space: O(n * k)
        maps = [".-","-...","-.-.","-..",".","..-.","--.","....","..",".---","-.-",".-..","--","-.","---",".--.","--.-",".-.","...","-","..-","...-",".--","-..-","-.--","--.."]
        return len({"".join(maps[ord(l) - ord('a')] for l in w) for w in words})

        # time: O(n * k), space: O(n * k)
        # maps = [".-","-...","-.-.","-..",".","..-.","--.","....","..",".---","-.-",".-..","--","-.","---",".--.","--.-",".-.","...","-","..-","...-",".--","-..-","-.--","--.."]
        # res = set()
        # for w in words:
        #     code = ""
        #     for l in w:
        #         code += maps[ord(l) - ord('a')]
        #     res.add(code)
        # return len(res)