class Solution:
    def imageSmoother(self, img: List[List[int]]) -> List[List[int]]:
        # time: O(m * n), space: O(m * n) or O(1)
        res = copy.deepcopy(img)
        for r in range(len(img)):
            for c in range(len(img[0])):
                tot = 0
                cnt = 0
                for r2 in range(max(r - 1, 0), min(r + 2, len(img))):
                    for c2 in range(max(c - 1, 0), min(c + 2, len(img[0]))):
                        tot += img[r2][c2]
                        cnt += 1
                res[r][c] = tot // cnt
        return res