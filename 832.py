class Solution:
    def flipAndInvertImage(self, image: List[List[int]]) -> List[List[int]]:
        # time: O(m * n), space: O(1)
        m, n = len(image), len(image[0])
        for r in range(m):
            for i in range((m + 1) // 2):
                image[r][i], image[r][~i] = image[r][~i], image[r][i]
        for r in range(m):
            for c in range(n):
                image[r][c] = 0 if image[r][c] else 1
        return image