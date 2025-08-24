class Solution:
    def checkIfExist(self, arr: List[int]) -> bool:
        # time: O(n), space: O(n)
        vis = set()
        for n in arr:
            if n / 2 in vis or n * 2 in vis:
                return True
            vis.add(n)
        return False