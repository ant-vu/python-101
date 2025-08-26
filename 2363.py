class Solution:
    def mergeSimilarItems(self, items1: List[List[int]], items2: List[List[int]]) -> List[List[int]]:
        # time: O(nlogn), space: O(n)
        maps = {}
        for value, weight in items1 + items2:
            maps[value] = weight + maps.get(value, 0)
        return sorted(maps.items())