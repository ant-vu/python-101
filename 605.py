class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        # time: O(n), space: O(1)
        if len(flowerbed) == 1:
            return True if n == 0 or flowerbed[0] == 0 and n == 1 else False
        if len(flowerbed) == 2:
            return True if n == 0 or flowerbed[0] == 0 and flowerbed[1] == 0 and n == 1 else False
        if flowerbed[0] == 0 and flowerbed[1] == 0:
            flowerbed[0] = 1
            n -= 1
        if flowerbed[-1] == 0 and flowerbed[-2] == 0:
            flowerbed[-1] = 1
            n -= 1
        for i in range(1, len(flowerbed) - 1):
            if flowerbed[i - 1] == 0 and flowerbed[i] == 0 and flowerbed[i + 1] == 0:
                flowerbed[i] = 1
                n -= 1
        return n <= 0